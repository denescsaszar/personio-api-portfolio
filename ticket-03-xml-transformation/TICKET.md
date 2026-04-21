# Ticket 03 — XML to JSON Transformation (SAP → Personio)

## Kundeninformation

| Feld | Details |
|------|---------|
| **Kunde** | Siemens AG |
| **Mitarbeiter** | ~300.000 |
| **ATS-System** | SAP SuccessFactors |
| **Ziel-System** | Personio (via talentsconnect JobShop) |
| **Melder** | Klaus Weber, HR Systems Manager |
| **Priorität** | Hoch |

## Was der Kunde berichtet

> "Wir nutzen SAP SuccessFactors als unser zentrales HR-System. Unsere Bewerberdaten
> liegen im SAP XML-Format vor. Wir wollen diese Daten in Personio importieren —
> aber Personio spricht JSON, SAP spricht XML. Wir brauchen eine Transformation
> die zuverlässig und validiert funktioniert."

## Was wir wissen

- SAP SuccessFactors gibt Bewerberdaten als XML zurück
- Personio erwartet JSON (verschachtelte Attribute-Struktur)
- Felder müssen gemappt werden — SAP und Personio nutzen verschiedene Feldnamen
- Pflichtfelder müssen validiert werden bevor der Import läuft
- Das ist exakt was APMonster intern macht

## Deine Aufgabe als Implementation Specialist

1. **XML parsen** — SAP XML Struktur mit `xml.etree.ElementTree` einlesen
2. **Felder mappen** — SAP Feldnamen → Personio Feldnamen transformieren
3. **JSON generieren** — Personio-kompatibles JSON ausgeben
4. **Validieren** — Pflichtfelder prüfen bevor Import
5. **Transformations-Report** — Zeige was gemappt wurde, was fehlt

## SAP vs Personio Feldmapping

| SAP XML Feld | Personio JSON Feld |
|---|---|
| `<FirstName>` | `first_name` |
| `<LastName>` | `last_name` |
| `<EmailAddress>` | `email` |
| `<JobTitle>` | `position` |
| `<ApplicationDate>` | `application_date` |
| `<RecruitingStatus>` | `status` |
| `<SourceType>` | `source` |

## Neue Python Konzepte

- **`xml.etree.ElementTree`** — Python built-in XML Parser (kein pip install nötig!)
- **`ET.fromstring(xml_string)`** — XML String parsen
- **`root.findall("Applicant")`** — Alle Elemente eines Typs finden
- **`element.find("FirstName").text`** — Wert eines XML-Elements lesen

## Erwarteter Output

```
=== SAP → PERSONIO XML TRANSFORMATION ===
Datum: 2026-04-21
Quelle: SAP SuccessFactors (Siemens AG)

Gesamt verarbeitet: 10
✓ Erfolgreich transformiert: 8
✗ Fehler (fehlende Pflichtfelder): 2

--- Feldmapping ---
SAP FirstName      → Personio first_name      ✓
SAP LastName       → Personio last_name        ✓
SAP EmailAddress   → Personio email            ✓
SAP JobTitle       → Personio position         ✓
SAP ApplicationDate → Personio application_date ✓
SAP RecruitingStatus → Personio status         ✓
SAP SourceType     → Personio source           ✓

--- Transformierte Datensätze ---
[001] Maria Schmidt | maria@siemens.de | Software Engineer | open
[002] Klaus Müller  | klaus@siemens.de | DevOps Engineer   | hired
...

--- Fehler ---
[009] Fehlende Pflichtfelder: email, position
[010] Fehlende Pflichtfelder: last_name
```
