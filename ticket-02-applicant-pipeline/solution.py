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
    if MOCK_MODE:
        print(f"\n--- Bewerber anlegen (Test) ---")
        print(f"✓ Neuer Bewerber angelegt: {first_name} {last_name} | {email} | {position}")
        return {"success": True, "mock": True}

    response = requests.post(
        f"{BASE_URL}/company/applicants",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "position": position,
        }
    )
    response.raise_for_status()
    return response.json()



def generate_pipeline_report(applicants):
    print("=== PERSONIO APPLICANT PIPELINE REPORT ===")
    print(f"Quelle: Personio API (TechStart GmbH)\n")

    total = len(applicants)
    status_counts = Counter(a["status"] for a in applicants)
    open_count = status_counts.get("open", 0)
    hired_count = status_counts.get("hired", 0)
    rejected_count = status_counts.get("rejected", 0)

    print(f"Gesamtzahl Bewerber: {total}")
    print(f"Offen:       {open_count}  ({open_count/total*100:.0f}%)")
    print(f"Eingestellt: {hired_count}  ({hired_count/total*100:.0f}%)")
    print(f"Abgelehnt:   {rejected_count}  ({rejected_count/total*100:.0f}%)\n")

    print("--- Pipeline nach Position ---")
    for position, count in Counter(a["position"] for a in applicants).most_common():
        print(f"{position}: {count}")

    print("\n--- Pipeline nach Quelle ---")
    for source, count in Counter(a["source"] for a in applicants).most_common():
        print(f"{source}: {count}")

    conversion = hired_count / total * 100
    print(f"\nConversion Rate (hired/total): {conversion:.1f}%")


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
