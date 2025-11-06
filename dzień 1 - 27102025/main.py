# ============================================================
# BLOK 1 (2h): Wprowadzenie do Pythona w kontekście testów API
# ============================================================

################## przyklad 1
# # HELLO WORLD — pierwszy wydruk w Pythonie
print("[1] Hello world + print")
print("Hello, world!")
print("Dzisiaj uczymy się Pythona do testów API.")
print()



# ################## przyklad 2
# # ZMIENNE I TYPY DANYCH — int, float, str, bool, None
print("[2] Zmienne i typy danych")
a = 10              # int — liczba całkowita
b = 3.14            # float — liczba zmiennoprzecinkowa
name = "Jan"        # str — tekst (string)
is_active = True    # bool — wartość logiczna
result = None       # None — brak wartości

print("a:", a, "| typ:", type(a))
print("b:", b, "| typ:", type(b))
print("name:", name, "| typ:", type(name))
print("is_active:", is_active, "| typ:", type(is_active))
print("result:", result, "| typ:", type(result))
print()

x = "10"
y = 10
#print(x+y)  # będzie błąd, dlatego należy sprowadzić wszystkie zmienne do tego samego typu:
print(int(x) + y)
print(x + str(y))
#jedynie typy numeryczne (int i float są kompatybilne)

# ################## przyklad 3
# # OPERATORY ARYTMETYCZNE — praktyczne podstawy
print("[3] Operatory arytmetyczne")
x = 10
y = 3
print("x + y =", x + y)     # dodawanie
print("x - y =", x - y)     # odejmowanie
print("x * y =", x * y)     # mnożenie
print("x / y =", x / y)     # dzielenie (float)
print("x // y =", x // y)   # dzielenie całkowite
print("x % y =", x % y)     # reszta z dzielenia do weryfikowanie krotnosci, np czy cos jest parzyste )reszta z dzielenia = 0)
print("x ** y =", x ** y)   # potęgowanie
print()



# ################## przyklad 4
# # PORÓWNANIA I LOGIKA — ==, !=, >, <, and/or/not
print("[4] Operatory porównań i logiczne")
a = 5
b = 8
print("a == b:", a == b)    # równe?
print("a != b:", a != b)    # różne?
print("a > b:",  a > b)
print("a < b:",  a < b)

x = True
y = False
print("x and y:", x and y)  # oba True?
print("x or y:",  x or y)   # przynajmniej jedno True?
print("not x:",   not x)    # negacja
print()

#KALKULATOR
a = float(input("podaj a")) 
b = float(input("podaj b"))
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b)
print(b / a)
print(a // b)
print(b // a)
print(a % b)
print(b % a)
print("a == b", a == b)
print("a != b", a != b)



# ################## przyklad 5
# # IF / ELSE — na przykładzie status_code (przedsmak testów API)
print("[5] Instrukcje warunkowe if/else")
status_code = 200  # spróbuj zmienić na 500, 404 itd.
if status_code == 200:
    print("✅ API OK")
elif status_code == 404:
    print("NOT FOUND")
else:
    print("❌ API DOWN (kod:", status_code, ")")
print()


wiek = int(input("Podaj swój wiek: "))
if wiek >= 18 and wiek < 24:
    print("Jesteś pełnoletni i nie możesz jeździć samochodem.")
elif wiek >= 24:
    print("Jesteś pełnoletni i możesz jeździć samochodem.")
else:
    print("Jeteś niepełnoletni.")


wiek = 70
if wiek < 18:
    print("Nie mozesz wejsc na koncert")
elif wiek >= 18:
    print("Witaj na koncercie, bilet normalny")
elif wiek >= 70:
    print("Witaj seniorze, masz znizke")


# ################## przyklad 6
# # # PIERWSZY REQUEST — check_api_status (GET + status_code)
print("[7] Pierwszy request: GET + status_code (check_api_status)")
try:
    import requests
    url = "https://api.github.com"  # przykładowy, stabilny endpoint publiczny
    response = requests.get(url, timeout=10)
    print("URL:", url)
    print("Kod odpowiedzi:", response.status_code)
    if response.status_code == 200:
        print("✅ API OK")
    else:
        print("❌ API down (kod:", response.status_code, ")")
except Exception as e:
    print("Błąd podczas requestu:", e)
print()


a = 5
b = 0
try:
    print(a/b)
except Exception as e:
    print(e)

# ZADANIE DOMOWE:
# konto na GitHub, utworzyc repo, podeslac tam zadanie domowe z classrooma

# ################## przyklad 7
# # TRY / EXCEPT — kontrolowana obsługa błędów połączeń
# print("[8] Obsługa wyjątków (try/except) dla requestu")
# import requests
# url = "https://api.nieistnieje.pl"  # celowo błędny, by pokazać wyjątek
# try:
#     r = requests.get(url, timeout=3)
#     print("Kod odpowiedzi:", r.status_code)
# except requests.exceptions.RequestException as e:
#     # Łapiemy wszystkie błędy warstwy requests (DNS, timeout, połączenie itp.)
#     print("Oczekiwany błąd połączenia:", repr(e))
# print()



# ################## przyklad 8
# # MINI-ĆWICZENIE — sprawdź kilka adresów w pętli i wypisz wynik
# print("[9] Mini-ćwiczenie: pętla po URL-ach")
# import requests
# urls = [
#     "https://api.github.com",
#     "https://google.com",
#     "https://nieistnieje.pl"  # powinien wywołać błąd
# ]
# for u in urls:
#     try:
#         r = requests.get(u, timeout=5)
#         print(u, "->", r.status_code)
#     except requests.exceptions.RequestException:
#         print(u, "-> błąd połączenia")
# print()



# ################## przyklad 9
# # FUNKCJA check_status(url) -> bool — do ponownego użycia
def check_status(url: str, timeout: int = 5) -> bool:
    """
    Zwraca True, jeśli endpoint zwraca 200. W przeciwnym razie False.
    Przydatne jako prosta 'asercja' w skryptach monitorujących.
    """
    import requests
    try:
        r = requests.get(url, timeout=timeout)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False

print("[10] Funkcja check_status(url) -> bool")
print("GitHub API:", check_status("https://api.github.com"))
print("Nieistnieje:", check_status("https://nieistnieje.pl"))
print()



# ################## przyklad 10
# # (OPCJONALNIE) POMIAR CZASU ODPOWIEDZI — r.elapsed
print("[11] (opcjonalnie) Pomiar czasu odpowiedzi")
import requests
url = "https://api.github.com"
r = requests.get(url, timeout=10)
# r.elapsed to timedelta — mierzony przez requests
print("Status:", r.status_code, "| Czas odpowiedzi [s]:", r.elapsed.total_seconds())
print()



# ################## przyklad 11
# # (OPCJONALNIE) PROSTA ASERCJA — content-type zawiera JSON
print("[12] (opcjonalnie) Prosta asercja content-type")
import requests
r = requests.get("https://api.github.com", timeout=10)
ctype = r.headers.get("content-type", "")
print("content-type:", ctype)
assert "json" in ctype.lower(), f"Nie-JSON content-type: {ctype}"
print("✅ Nagłówki wyglądają OK (JSON)")
print()

