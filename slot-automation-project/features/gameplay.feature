```gherkin
Feature: Podstawowa mechanika gry slotowej

  Scenario: Gracz z wystarczającymi środkami wykonuje poprawny spin
    Given gracz jest zalogowany i ma na koncie 100 kredytów
    When wykonuje spin za 10 kredytów
    Then jego nowe saldo powinno wynosić 90 kredytów
    And odpowiedź serwera powinna zawierać informację o wyniku spinu

  Scenario: Gracz z niewystarczającymi środkami próbuje wykonać spin
    Given gracz jest zalogowany i ma na koncie 5 kredytów
    When próbuje wykonać spin za 10 kredytów
    Then system powinien zwrócić błąd o niewystarczających środkach
    And saldo gracza powinno pozostać bez zmian