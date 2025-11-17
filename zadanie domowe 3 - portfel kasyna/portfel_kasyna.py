import requests
from typing import Tuple, List
from time import sleep


BASE_URL = "https://690cb8c2a6d92d83e84f1d7a.mockapi.io/api"

class Player:
    def __init__(self, id: str, username: str, balance: float):
        self.id = id
        self.username = username
        self.balance = balance

    def __repr__(self) -> str:
        return f"Player(id={self.id}, username={self.username}, balance={self.balance}>"
    
    def add_money(self, amount: float):
        if amount <= 0:
            print("Nie można przelać 0 lub mniej!")
            return
        
        self.balance += amount
        print(f"Gracz {self.username} otrzymuje {amount} => Aktualne saldo: {self.balance}")
    
    def spend_money(self, amount):
        if amount <= 0:
            print("Nie można przelać 0 lub mniej!")
            return False
        elif amount > self.balance:
            print(f"Gracz {self.username} nie wyśle więcej niż ma! Ma na koncie jedynie: {self.balance}.")
            return False
        
        self.balance -= amount
        print(f"Gracz {self.username} otrzymuje {amount} => Aktualne saldo: {self.balance}")
        return True

def transfer_money(from_username, to_username, amomunt: float):
    try:
        amount = float(input("Podaj kwotę, którą chcesz przelać: "))
    except ValueError:
        print(f"Niepoprawna kwota: {amount} - anulowanie przelewu.")
        return
    
    if amount <= 0:
        print(f"Przelew niemożliwy - kwota przelewu musi być dodatnia.")
        return
    
    from_username = str(input(f"Podaj imię gracza, OD KTÓREGO chcesz przelać kwotę {amount}: ", {from_username.lower()}))
    to_username = str(input(f"Podaj imię gracza, KTÓREMU chcesz przelać kwotę {amount}: ", {to_username.lower()}))

    if from_username == to_username:
        print(f"Nie jest możliwy przelew dla samego siebie.")
        return

    transfer_possible = from_username.spend_money(amount)

    if transfer_possible:
        to_username.add_money(amount)
        print(f"Przelew od {from_username} to {to_username} udany!")    
    else:
        print(f"Przelew nieudany - gracz {from_username} ma na koncie za mało środków lub podana kwota: '{amount}' jest niedozwolona.")