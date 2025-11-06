# ZADANIE DOMOWE 1 - Prosty kalkulator

print("Cześć! Użyj prostego kalkulatora do podstawowych obliczeń.")

try:
    a = int(input("Podaj liczbę całkowitą a: "))
except ValueError:
    print("Podaj liczbę całkowitą!")
    a = int(input("Podaj liczbę całkowitą a: "))

try:
    b = int(input("Podaj liczbę całkowitą b: "))
except ValueError:
    print("Podaj liczbę całkowitą!")
    b = int(input("Podaj liczbę całkowitą b: "))

znak = str(input("Podaj znak działania między a i b. Wybierz spośród: +, -, *, /, ^, %:  "))

if znak == '+':
    print("Wynik dodawania to: ", a + b)

elif znak == '-':
    print("Wynik odejmowania a - b to: ", a - b)
    print("Wynik odejmowania b - a to: ", b - a)

elif znak == '*':
    print("Wynik mnożenia to: ", a * b)

elif znak == '/':

    try:
        print("Wynik dzielenia a/b to: ", a / b)
    except Exception as e:
        print("Dla a/b niemożliwe dzielenie przez 0!")
    
    try:
        print("Wynik dzielenia b/a to: ", b / a)
    except Exception as e:
        print("Dla b/a niemożliwe dzielenie przez 0!")
    
elif znak == '^':
    print("Wynik potęgowania a^b to: ", a ** b)
    print("Wynik potęgowania b^a to: ", b ** a)

elif znak == '%':
    print("Reszta z dzielenia a/b to: ", a % b)
    print("Reszta z dzielenia b/a to: ", b % a)
    
else:
    print("Błędny znak działania. Spróbuj jeszcze raz i podaj spośród: +, -, *, /, ^, %.")
