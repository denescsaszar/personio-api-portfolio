# Ticket 03 — XML to JSON Transformation (SAP → Personio)
# Personio API Portfolio
#
# Aufgabe: Implementiere die Funktionen unten.
# Neu: xml.etree.ElementTree zum Parsen von SAP XML Daten.

import xml.etree.ElementTree as ET
import json
from datetime import datetime
from mock_sap_data import MOCK_SAP_XML

# --- Feldmapping SAP → Personio ---

FIELD_MAPPING = {
    "FirstName":         "first_name",
    "LastName":          "last_name",
    "EmailAddress":      "email",
    "JobTitle":          "position",
    "ApplicationDate":   "application_date",
    "RecruitingStatus":  "status",
    "SourceType":        "source",
}

REQUIRED_FIELDS = ["first_name", "last_name", "email", "position"]


# --- Funktionen ---

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    applicants = root.findall("Applicant")
    print(f"XML geparst: {len(applicants)} Datensätze gefunden")
    return applicants


def map_fields(sap_applicant):
    result = {}
    for sap_field, personio_field in FIELD_MAPPING.items():
        element = sap_applicant.find(sap_field)
        value = element.text if element is not None else None
        result[personio_field] = value if value else None
    return result

def validate_applicant(applicant):
    missing = [
        field for field in REQUIRED_FIELDS
        if not applicant.get(field)
    ]
    is_valid = len(missing) == 0
    return is_valid, missing


def transform_all(xml_string):
    applicants = parse_xml(xml_string)
    successful = []
    errors = []

    for applicant in applicants:
        mapped = map_fields(applicant)
        is_valid, missing = validate_applicant(mapped)

        if is_valid:
            successful.append(mapped)
        else:
            errors.append({
                "data": mapped,
                "missing_fields": missing
            })

    return successful, errors


def generate_transformation_report(successful, errors):
    total = len(successful) + len(errors)
    print(f"Gesamt verarbeitet: {total}")
    print(f"✓ Erfolgreich transformiert: {len(successful)}")
    print(f"✗ Fehler (fehlende Pflichtfelder): {len(errors)}\n")

    print("--- Feldmapping ---")
    for sap_field, personio_field in FIELD_MAPPING.items():
        print(f"SAP {sap_field:<20} → Personio {personio_field:<20} ✓")

    print("\n--- Transformierte Datensätze ---")
    for i, a in enumerate(successful, 1):
        print(f"[{i:03d}] {a['first_name']} {a['last_name']:<15} | {a['email']:<30} | {a['position']:<20} | {a['status']}")

    if errors:
        print("\n--- Fehler ---")
        for e in errors:
            name = f"{e['data'].get('first_name', '?')} {e['data'].get('last_name', '?')}"
            print(f"✗ {name:<20} | Fehlende Pflichtfelder: {', '.join(e['missing_fields'])}")


def main():
    print("=== SAP → PERSONIO XML TRANSFORMATION ===")
    print(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Quelle: SAP SuccessFactors (Siemens AG)\n")

    successful, errors = transform_all(MOCK_SAP_XML)
    generate_transformation_report(successful, errors)


if __name__ == "__main__":
    main()
