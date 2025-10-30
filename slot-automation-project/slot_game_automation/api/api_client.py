import requests

class ApiClient:
    """
    Klient do komunikacji z API gry.
    """
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def authenticate(self, username, password):
        """
        Metoda do autentykacji gracza.
        TODO: Do implementacji podczas zajęć.
        """
        # Tutaj będzie logika zapytania POST do /login
        print("Autentykacja gracza...")
        # Zwracamy przykładowy token
        return "fake_auth_token_123"

    def post_spin(self, token, bet_amount):
        """
        Wysyła zapytanie o wykonanie spinu.
        TODO: Do implementacji podczas zajęć.
        """
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"bet": bet_amount}
        
        # Tutaj będzie logika zapytania POST do /spin
        print(f"Wysyłanie zapytania o spin z zakładem: {bet_amount}")

        # Zwracamy przykładową, uproszczoną odpowiedź
        # W realnym scenariuszu tu byłoby `self.session.post(...)`
        response_data = {
            "status": "success",
            "new_balance": 90,
            "win": 0,
            "reels": [["CHERRY", "BAR", "LEMON"], ["SEVEN", "CHERRY", "BAR"]]
        }
        return response_data