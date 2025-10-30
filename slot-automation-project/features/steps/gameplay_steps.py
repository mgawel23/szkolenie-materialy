from behave import given, when, then
from slot_game_automation.models.player import Player
from slot_game_automation.api.api_client import ApiClient

# Tutaj, w świecie rzeczywistym, czytalibyśmy konfigurację z pliku config.ini
API_URL = "https://api.example-slot-provider.com/v1"

@given('gracz jest zalogowany i ma na koncie {balance:d} kredytów')
def step_impl(context, balance):
    context.player = Player(initial_balance=balance)
    context.api_client = ApiClient(base_url=API_URL)
    
    # Symulujemy logowanie
    token = context.api_client.authenticate("user", "password")
    context.player.set_auth_token(token)
    print(f"Gracz zalogowany z saldem: {context.player.balance}")


@when('wykonuje spin za {bet:d} kredytów')
def step_impl(context, bet):
    print(f"Wykonywanie spinu za: {bet} kredytów")
    # TODO: Do implementacji - wywołanie metody z ApiClient
    # context.spin_response = context.api_client.post_spin(...)
    pass


@then('jego nowe saldo powinno wynosić {new_balance:d} kredytów')
def step_impl(context, new_balance):
    # TODO: Do implementacji - asercja sprawdzająca saldo
    # assert context.player.balance == new_balance
    print("Sprawdzanie nowego salda...")
    pass

@then('odpowiedź serwera powinna zawierać informację o wyniku spinu')
def step_impl(context):
    # TODO: Do implementacji - asercja sprawdzająca odpowiedź
    print("Sprawdzanie odpowiedzi serwera...")
    pass


# --- Pozostałe kroki do implementacji ---

@when('próbuje wykonać spin za {bet:d} kredytów')
def step_impl(context, bet):
    # TODO
    pass

@then('system powinien zwrócić błąd o niewystarczających środkach')
def step_impl(context):
    # TODO
    pass

@then('saldo gracza powinno pozostać bez zmian')
def step_impl(context):
    # TODO
    pass