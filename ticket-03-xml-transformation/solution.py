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
    """
    SAP Felder → Personio Felder mappen anhand FIELD_MAPPING.

    Input:  Ein XML Element (ein SAP Bewerber)
    Output: Dict mit Personio Feldnamen

    Tipp: sap_applicant.find("FirstName").text
          Achtung: .text kann None sein wenn Feld fehlt!
    """
    # TODO: Implementiere das Feldmapping
    pass


def validate_applicant(applicant):
    """
    Prüft ob alle Pflichtfelder vorhanden und nicht leer sind.

    Input:  Dict mit gemappten Personio Feldern
    Output: (is_valid: bool, missing_fields: list)

    Tipp: Prüfe jeden Eintrag in REQUIRED_FIELDS
    """
    # TODO: Implementiere die Validierung
    pass


def transform_all(xml_string):
    """
    Orchestriert den kompletten Transformations-Prozess:
    1. XML parsen
    2. Jeden Bewerber mappen
    3. Jeden Bewerber validieren
    4. Gibt zwei Listen zurück: erfolgreiche und fehlerhafte

    Output: (successful: list, errors: list)
    """
    # TODO: Implementiere die Transformation
    pass


def generate_transformation_report(successful, errors):
    """
    Transformations-Report ausgeben:
    - Gesamtzahl, Erfolge, Fehler
    - Feldmapping Übersicht
    - Transformierte Datensätze
    - Fehler mit Details
    """
    # TODO: Implementiere den Report
    pass


def main():
    """Orchestriert den kompletten Transformations-Prozess."""
    print("=== SAP → PERSONIO XML TRANSFORMATION ===")
    print(f"Datum: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Quelle: SAP SuccessFactors (Siemens AG)\n")

    # TODO:
    # 1. XML transformieren (transform_all)
    # 2. Report generieren


if __name__ == "__main__":
    main()
