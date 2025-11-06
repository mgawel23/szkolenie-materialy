# ZADANIE DOMOWE 2 - Mini Monitor API

# Skrypt:
# - pobiera dane z kilku publicznych API (GET),
# - analizuje ich odpowiedzi (status, nagłówki, JSON),
# - zlicza wyniki i wypisuje podsumowanie.

import requests
from typing import Dict, Optional, Tuple

urls = [
    "https://api.github.com",
    "https://httpbin.org/json",
    "https://jsonplaceholder.typicode.com/posts/1t",
    "https://to_nie_istnieje.abc"
]


def fetch_json(url: str, timeout = 5, retries = 3) -> Tuple[Optional[Dict], int, Dict, Optional[Exception]]:
    
    licznik = 0
    error = None

    while licznik < retries:
        licznik += 1
        print(f"Dla {url} próba nr: {licznik}")   
        try:
            resp = requests.get(url, timeout=timeout)
            status = resp.status_code
            headers = resp.headers
            # Próbuje pobrać JSON
            try:
                j = resp.json()
                # Pobrało JSON
                return j, status, headers, None
            except ValueError as ve:
                # Błąd JSON - nie pobrało
                return None, status, headers, ve
       
        except requests.exceptions.RequestException as e:
            print(f" --> Problem z połączeniem: {e}")  # Problem z połączeniem, np. zły URL, brak połączenia internetowego
    
    return None, -1, {}, error

tries_ok = 0
tries_fail = 0

for url in urls:
    print(f"Teraz sprawdzam: {url} ...")
    json, status, headers, error = fetch_json(url)
    
    if status == 200 and error is None and json is not None:
        print(f"✅ OK --> Status: {status}")
        tries_ok += 1
    else:
        print(f"❌ FAIL --> Status: {status}, Błąd: {error}")
        tries_fail += 1

for url in urls:
        print(url, "OK = ", tries_ok, "| FAIL = ", tries_fail)
