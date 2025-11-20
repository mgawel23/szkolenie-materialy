import requests
from typing import List, Dict, Any, Optional

BASE_URL = "https://690cb8c2a6d92d83e84f1d7a.mockapi.io/api"
TIMEOUT = 5

# KLASA PLAYER:
class Player:
    def __init__(self, id: str, username: str, balance: float):
        self.id = id
        self.username = username
        self.balance = float(balance)

    def __repr__(self) -> str:
        return f"Player(id={self.id}, username={self.username}, balance={self.balance:.2f})"
    
    def add_money(self, amount: float) -> bool:
        if amount <= 0:
            print("Nie można dodać 0 lub mniej!")
            return False
        self.balance += amount
        return True
    
    def spend_money(self, amount: float) -> bool:
        if amount <= 0:
            print("Kwota musi być dodatnia!")
            return False
        if amount > self.balance:
            print(f"Gracz {self.username} nie ma wystarczających środków (ma {self.balance:.2f}).")
            return False
        self.balance -= amount
        return True
    
    def change_to_dict_for_api(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'username': self.username,
            'balance': round(self.balance, 2)
        }

# KOMUNIKACJA Z API:

def get_all_users() -> Optional[List[Dict[str, Any]]]:
    try:
        url = f"{BASE_URL}/users"
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Błąd połączenia - nie można pobrać danych z API: {e}")
        return None
    
def put_user(user_data: Dict[str, Any]) -> bool:
    try:
        user_id = user_data["id"]
        url = f"{BASE_URL}/users/{user_id}"
        r = requests.put(url, json=user_data, timeout=TIMEOUT)
        r.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Błąd połączenia - nie można zaktualizować danych gracza {user_data.get('username')}: {e}")
        return False

# HELPERS:

def dict_to_player(d: Dict[str, Any]) -> Player:
    return Player(id=str(d.get("id", "")), username=str(d.get("username", "")), balance=float(d.get("balance", 0)))

def find_player_by_username(users: List[Dict[str, Any]], username: str) -> Optional[Player]:
    username_lower = username.lower()
    for u in users:
        if str(u.get("username", "")).lower() == username_lower:
            return dict_to_player(u)
    return None

# LOGIKA APLIKACJI:

def show_all_players():
    print("\n=== LISTA WSZYSTKICH GRACZY ===")
    users_data = get_all_users()

    if users_data is None:
        return
    
    if not users_data:
        print("Baza graczy jest pusta.")
        return
    
    print(f"{'ID':<5} | {'USERNAME':<20} | {'BALANCE':>10}")
    print("-" * 42)

    for user in users_data:
        balance = float(user.get('balance', 0))
        print(f"{str(user.get('id','')):<5} | {str(user.get('username','')):<20} | {balance:>10.2f}")

def check_balance():
    users_data = get_all_users()
    if users_data is None:
        return
    username = input("Podaj username: ").strip()
    if not username:
        print("Nie podano username.")
        return
    player = find_player_by_username(users_data, username)
    if player is None:
        print(f"Nie znaleziono gracza o username '{username}'.")
    else:
        print(f"Saldo gracza '{username}': {player.balance:.2f}")

def transfer_money():
    try:
        amount = float(input("Kwota do przelania: ").strip())
    except ValueError:
        print("Niepoprawna kwota - anulowano.")
        return
    if amount <= 0:
        print("Kwota musi być większa od 0.")
        return

    from_username = input("Nadawca (username): ").strip()
    to_username = input("Odbiorca (username): ").strip()

    if not from_username or not to_username:
        print("Należy podać oba username'y.")
        return
    if from_username.lower() == to_username.lower():
        print("Nie można przelać samemu do siebie.")
        return

    users_data = get_all_users()
    if users_data is None:
        return

    sender = find_player_by_username(users_data, from_username)
    receiver = find_player_by_username(users_data, to_username)

    if sender is None:
        print(f"Nie znaleziono nadawcy '{from_username}'.")
        return
    if receiver is None:
        print(f"Nie znaleziono odbiorcy '{to_username}'.")
        return

    # Walidacja środków
    if amount > sender.balance:
        print(f"Niewystarczające środki u nadawcy ({sender.username} ma {sender.balance:.2f}).")
        return

    print(f"Przelew {amount:.2f} z '{sender.username}' do '{receiver.username}'...")

    # Zmiany lokalne
    ok_spend = sender.spend_money(amount)
    if not ok_spend:
        print("Przelew przerwany podczas sprawdzania środków.")
        return
    receiver.add_money(amount)

    # Wysyłam PUTy
    from_payload = sender.change_to_dict_for_api()
    to_payload = receiver.change_to_dict_for_api()

    success_from = put_user(from_payload)
    success_to = put_user(to_payload)

    if success_from and success_to:
        print(f"OK. Nowe salda: {sender.username}={sender.balance:.2f}, {receiver.username}={receiver.balance:.2f}")
    else:
        print("Operacja częściowo nieudana." if (success_from or success_to) else "Operacja nieudana.")
        print(f"Status PUT nadawcy: {'OK' if success_from else 'FAILED'}, odbiorcy: {'OK' if success_to else 'FAILED'}")
        print(f"Lokalne salda (niekoniecznie zsynchronizowane): {sender.username}={sender.balance:.2f}, {receiver.username}={receiver.balance:.2f}")

def menu():
    while True:
        print("\n=== PORTFEL KASYNA ===")
        print("1) Wyświetl wszystkich graczy")
        print("2) Sprawdź stan konta gracza")
        print("3) Przelej pieniądze (username -> username)")
        print("4) Zakończ")
        choice = input("Wybór: ").strip()
        if choice == "1":
            show_all_players()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            transfer_money()
        elif choice == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz 1-4.")

if __name__ == "__main__":
    menu()