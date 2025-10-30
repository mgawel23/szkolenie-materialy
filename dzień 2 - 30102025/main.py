# ============================================================
# BLOK 2 (2h): Warunki, pętle i praca z danymi z API / logów
# ============================================================

# ------------------------------------------------------------
# PRZYKŁAD 1 — powtórka z if / elif / else
# ------------------------------------------------------------

print("[1] Instrukcje warunkowe if / elif / else")

status_code = 503

if status_code == 200:
    print("✅ API działa poprawnie")
elif status_code == 404:
    print("❌ Błąd: zasób nie znaleziony (404)")
elif status_code >= 500:
    print("💥 Błąd serwera (5xx)")
else:
    print("⚠️ Inny kod:", status_code)

print()




# ------------------------------------------------------------
# MINI-ĆWICZENIE — prosta pętla for
# ------------------------------------------------------------

print("Prosta pętla for — wypisanie liczb od 1 do 10")

for i in range(1, 11):
    print("Liczba:", i)

print()




# ------------------------------------------------------------
# PRZYKŁAD 2 — pętla for + lista adresów
# ------------------------------------------------------------

print("[2] Pętla for po liście URL-i")

urls = [
    "https://api.github.com",
    "https://google.com",
    "https://nieistnieje.pl"
]

import requests

for adres in urls:
    try:
        r = requests.get(adres, timeout=3)
        print(adres, "->", r.status_code)
    except requests.exceptions.RequestException:
        print(adres, "-> błąd połączenia")

print()

### zadanie:
# 1) Dodaj do listy jeszcze jeden adres, np. https://httpbin.org/status/404.
# 2) Zmień kod tak, aby jeśli status to 200 — wypisał "OK", a jeśli inny — "problem".




# ------------------------------------------------------------
# MINI-ĆWICZENIE — pętla while
# ------------------------------------------------------------

print("Pętla while — dopóki licznik < 5")

licznik = 0
while licznik < 5:
    print("Iteracja nr:", licznik)
    licznik += 1

print("Koniec pętli while")
print()




# ------------------------------------------------------------
# PRZYKŁAD 3 — while: ponów próbę jeśli API nie odpowiada
# ------------------------------------------------------------

print("[3] Pętla while — powtarzanie prób połączenia")

url = "https://httpbin.org/status/503"
max_proby = 3
licznik = 0
udalo_sie = False

while licznik < max_proby and not udalo_sie:
    licznik += 1
    print("Próba nr:", licznik)
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            print("✅ API działa!")
            udalo_sie = True
        else:
            print("❌ Błąd:", r.status_code)
    except requests.exceptions.RequestException:
        print("Błąd połączenia, spróbuję ponownie...")

print("Koniec prób.")
print()


### zadanie:
# 1) Zmień liczbę prób na 5 i dodaj opóźnienie 1 sekundy (import time; time.sleep(1))
# 2) Dodaj wydruk „Test zakończony sukcesem” lub „Test nieudany” po zakończeniu pętli.




# ------------------------------------------------------------
# MINI-ĆWICZENIE — lista i iteracja po elementach
# ------------------------------------------------------------

print("Iteracja po liście imion")

imiona = ["Ala", "Jan", "Ola", "Tomek"]

for imie in imiona:
    print("Cześć,", imie + "!")

print()




# ------------------------------------------------------------
# PRZYKŁAD 4 — listy i słowniki: analiza danych (symulacja logów)
# ------------------------------------------------------------

print("[4] Praca na listach i słownikach — logi API")

logi = [
    {"czas": "10:00", "status": 200, "endpoint": "/users"},
    {"czas": "10:01", "status": 404, "endpoint": "/orders"},
    {"czas": "10:02", "status": 200, "endpoint": "/users"},
    {"czas": "10:03", "status": 500, "endpoint": "/payments"},
    {"czas": "10:04", "status": 200, "endpoint": "/orders"},
]

# Liczymy ile było udanych i błędnych odpowiedzi
ok = 0
bledy = 0

for wpis in logi:
    if wpis["status"] == 200:
        ok += 1
    else:
        bledy += 1

print("✅ OK:", ok)
print("❌ Błędy:", bledy)
print()


### zadanie:
# 1) Policz, ile było błędów 404, a ile 500 (użyj osobnych liczników).
# 2) Dodaj filtr: wypisz tylko te wpisy, gdzie endpoint to "/orders".




# ------------------------------------------------------------
# PRZYKŁAD 5 — parsowanie JSON-a z API (GET + dane)
# ------------------------------------------------------------

print("[5] Parsowanie JSON-a z API")

try:
    r = requests.get("https://api.github.com", timeout=5)
    print("Kod odpowiedzi:", r.status_code)
    dane = r.json()
    print("Klucze JSON:", list(dane.keys())[:5])
except Exception as e:
    print("Błąd pobierania:", e)

print()


### zadanie:
# 1) Wypisz wartość pola "current_user_url" z pobranego JSON-a.
# 2) Dodaj sprawdzenie: jeśli "json" nie ma w nagłówku content-type, wypisz ostrzeżenie.




# ------------------------------------------------------------
# PRZYKŁAD 6 — analiza listy transakcji
# ------------------------------------------------------------

print("[6] Analiza listy transakcji (pętla + warunki)")

transakcje = [
    {"id": 1, "typ": "PAYMENT", "kwota": 120.5, "waluta": "PLN"},
    {"id": 2, "typ": "REFUND", "kwota": -20.5, "waluta": "PLN"},
    {"id": 3, "typ": "PAYMENT", "kwota": 15.0, "waluta": "EUR"},
    {"id": 4, "typ": "PAYMENT", "kwota": 200.0, "waluta": "PLN"},
    {"id": 5, "typ": "CHARGEBACK", "kwota": -200.0, "waluta": "PLN"},
]

suma_pln = 0
for t in transakcje:
    if t["typ"] == "PAYMENT" and t["waluta"] == "PLN":
        suma_pln += t["kwota"]

print("Suma płatności w PLN:", suma_pln)
print()


### zadanie:
# 1) Oblicz łączną sumę wszystkich transakcji (bez względu na typ).
# 2) Wypisz tylko te transakcje, których kwota > 100.




# ------------------------------------------------------------
# PRZYKŁAD 7 — wyszukiwanie w logach: szukamy błędów
# ------------------------------------------------------------

print("[7] Wyszukiwanie błędów w logach")

logi = [
    {"czas": "12:00", "poziom": "INFO", "zdarzenie": "LOGIN"},
    {"czas": "12:01", "poziom": "WARN", "zdarzenie": "SLOW_RESPONSE"},
    {"czas": "12:02", "poziom": "ERROR", "zdarzenie": "TIMEOUT"},
    {"czas": "12:03", "poziom": "INFO", "zdarzenie": "LOGOUT"},
]

for wpis in logi:
    if wpis["poziom"] == "ERROR":
        print("❗Błąd znaleziony:", wpis)

print()


### zadanie:
# 1) Policz ile było komunikatów INFO, WARN i ERROR.
# 2) Dodaj dodatkowe sprawdzenie: jeśli ERROR wystąpił — wypisz "Test NIEZALICZONY".




# ------------------------------------------------------------
# PRZYKŁAD 8 — pętla po słowniku
# ------------------------------------------------------------

print("[8] Pętla po słowniku — analiza nagłówków")

naglowki = {
    "Content-Type": "application/json",
    "Server": "GitHub.com",
    "RateLimit-Limit": "60",
}

for klucz in naglowki:
    print(klucz, ":", naglowki[klucz])

print()


### zadanie:
# 1) Wypisz tylko te nagłówki, które zawierają słowo "Limit".
# 2) Policz, ile jest wszystkich nagłówków.




# ------------------------------------------------------------
# PRZYKŁAD 9 — pętla z break i continue
# ------------------------------------------------------------

print("[9] break / continue — kontrola przepływu pętli")

statusy = [200, 200, 404, 500, 200]

for kod in statusy:
    if kod == 404:
        print("Ominięto 404 (continue)")
        continue
    if kod == 500:
        print("Zatrzymanie pętli na 500 (break)")
        break
    print("Przetwarzam kod:", kod)

print("Pętla zakończona.")
print()


### zadanie:
# 1) Dodaj licznik, ile kodów 200 zostało przetworzonych.
# 2) Po pętli wypisz „Przetworzono X OK, Y błędów”.




# ------------------------------------------------------------
# PRZYKŁAD 10 — mini test API: sprawdzanie wielu endpointów
# ------------------------------------------------------------

print("[10] Mini test API — skanowanie endpointów")

adresy = [
    "https://api.github.com",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://nieistnieje.pl"
]

ok = 0
fail = 0

for a in adresy:
    try:
        r = requests.get(a, timeout=3)
        if r.status_code == 200:
            print(a, "-> ✅ OK")
            ok += 1
        else:
            print(a, "-> ❌ Problem (", r.status_code, ")")
            fail += 1
    except requests.exceptions.RequestException:
        print(a, "-> brak odpowiedzi")
        fail += 1

print("Podsumowanie: OK =", ok, "| FAIL =", fail)
print()

### zadanie:
# 1) Dodaj na końcu komunikat: jeśli OK > FAIL, wypisz „Test zaliczony”.
# 2) Jeśli odwrotnie — „Test NIEZALICZONY”.
