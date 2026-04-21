# Ticket 02 — Applicant Pipeline Sync
# Personio API Portfolio
#
# Aufgabe: Implementiere die Funktionen unten.
# Nutze die Mock-Daten zum Testen (kein echtes Personio-Konto nötig).

import os
import requests
from datetime import datetime
from collections import Counter
from dotenv import load_dotenv
from mock_applicants import MOCK_APPLICANTS

load_dotenv()

# --- Konfiguration ---

BASE_URL = os.getenv("PERSONIO_BASE_URL", "https://api.personio.de/v1")
CLIENT_ID = os.getenv("PERSONIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("PERSONIO_CLIENT_SECRET")
MOCK_MODE = True  # Auf False setzen wenn echte API Credentials vorhanden


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

def fetch_all_applicants(token):
    if MOCK_MODE:
        print(f"Mock: {len(MOCK_APPLICANTS)} Bewerber geladen")
        return MOCK_APPLICANTS

    all_applicants = []
    offset = 0
    limit = 200

    while True:
        response = requests.get(
            f"{BASE_URL}/company/applicants",
            headers={"Authorization": f"Bearer {token}"},
            params={"limit": limit, "offset": offset}
        )
        response.raise_for_status()
        data = response.json()["data"]

        if not data:
            break

        all_applicants.extend(data)
        offset += limit

    print(f"Live: {len(all_applicants)} Bewerber geladen")
    return all_applicants


def parse_applicant(raw_applicant):
    attrs = raw_applicant["attributes"]
    return {
        "id": attrs["id"]["value"],
        "first_name": attrs["first_name"]["value"],
        "last_name": attrs["last_name"]["value"],
        "email": attrs["email"]["value"],
        "position": attrs["position"]["value"],
        "status": attrs["status"]["value"],
        "source": attrs["source"]["value"],
        "application_date": attrs["application_date"]["value"],
    }


def create_applicant(token, first_name, last_name, email, position):
    """
    Neuen Bewerber anlegen via POST Request.
    POST /v1/company/applicants mit JSON Body.

    Im MOCK_MODE: Gibt einen simulierten Response zurück.
    """
    # TODO: Implementiere den POST Request
    pass


def generate_pipeline_report(applicants):
    """
    Pipeline Report generieren:
    - Gesamtzahl, Aufschlüsselung nach Status (open/hired/rejected)
    - Aufschlüsselung nach Position und Quelle
    - Conversion Rate (hired / total)
    """
    # TODO: Implementiere den Report
    pass


def main():
    """Orchestriert den kompletten Pipeline-Prozess."""
    print("=== PERSONIO APPLICANT PIPELINE ===")
    print(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Modus: {'MOCK' if MOCK_MODE else 'LIVE'}\n")

    # TODO:
    # 1. Authentifizieren
    # 2. Alle Bewerber abrufen
    # 3. Jeden Bewerber parsen
    # 4. Pipeline Report generieren
    # 5. Test: Neuen Bewerber anlegen


if __name__ == "__main__":
    main()
