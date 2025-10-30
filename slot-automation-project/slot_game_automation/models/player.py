class Player:
    """
    Model reprezentujący gracza i jego stan.
    """
    def __init__(self, player_id=None, initial_balance=0):
        self.player_id = player_id
        self.balance = initial_balance
        self.auth_token = None
        print(f"Utworzono gracza z saldem: {self.balance}")

    def set_auth_token(self, token):
        """Ustawia token autoryzacyjny dla sesji gracza."""
        self.auth_token = token

    def update_balance(self, amount):
        """Aktualizuje saldo gracza."""
        self.balance += amount
        print(f"Zaktualizowano saldo. Nowe saldo: {self.balance}")