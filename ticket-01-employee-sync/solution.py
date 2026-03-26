# Ticket 01 — Employee Data Sync
# Personio API Portfolio

import os
import requests
from datetime import datetime
from collections import Counter
from dotenv import load_dotenv
from mock_employees import MOCK_EMPLOYEES

load_dotenv()

# --- Konfiguration ---

BASE_URL = os.getenv("PERSONIO_BASE_URL", "https://api.personio.de/v1")
CLIENT_ID = os.getenv("PERSONIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("PERSONIO_CLIENT_SECRET")
MOCK_MODE = True


# --- Funktionen ---

def authenticate():
    if MOCK_MODE:
        print("Auth: Mock-Modus aktiv")
        return "mock-token-12345"

    response = requests.post(
        f"{BASE_URL}/auth",
        json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
    )
    response.raise_for_status()
    return response.json()["data"]["token"]


def fetch_all_employees(token):
    if MOCK_MODE:
        print(f"Mock: {len(MOCK_EMPLOYEES)} Mitarbeiter geladen")
        return MOCK_EMPLOYEES

    all_employees = []
    offset = 0
    limit = 200

    while True:
        response = requests.get(
            f"{BASE_URL}/company/employees",
            headers={"Authorization": f"Bearer {token}"},
            params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        data = response.json()["data"]

        if not data:
            break

        all_employees.extend(data)
        offset += limit

    print(f"Live: {len(all_employees)} Mitarbeiter geladen")
    return all_employees


def parse_employee(raw_employee):
    # TODO: Implementiere das Parsing
    pass


def generate_sync_report(employees):
    # TODO: Implementiere den Report
    pass


def main():
    print("=== PERSONIO EMPLOYEE SYNC ===")
    print(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Modus: {'MOCK' if MOCK_MODE else 'LIVE'}\n")

    # TODO:
    # 1. Authentifizieren
    # 2. Mitarbeiter abrufen
    # 3. Jeden Mitarbeiter parsen
    # 4. Report generieren


if __name__ == "__main__":
    main()
