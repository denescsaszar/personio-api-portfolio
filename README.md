# Personio API Portfolio — Technical Implementation Specialist

Hands-on Portfolio mit realen Implementierungs-Szenarien für die Personio REST API.
Jedes Ticket simuliert ein echtes Kundenproblem, das als Technical Implementation Specialist gelöst wird.

## Stack

- **Sprache:** Python 3.11
- **HTTP Client:** requests (keine SDK — direkter REST API Zugriff)
- **API:** Personio REST API v1/v2
- **Datenformate:** JSON, XML

## Ticket-Übersicht

| #   | Szenario                             | Personio API Bereich        | Status      |
| --- | ------------------------------------ | --------------------------- | ----------- |
| 01  | Employee Data Sync                   | Auth, Employees, Pagination | ✅ Done     |
| 02  | Applicant Pipeline Sync              | Recruiting API, POST        | ✅ Done     |
| 03  | XML Transformation (SAP → Personio)  | XML Parsing, Field Mapping  | ✅ Done     |
| 04  | Webhook-Setup & Event-Processing     | Webhooks                    | Planned     |
| 05  | Recruiting-Pipeline & ATS-Anbindung  | Recruiting API              | Planned     |
| 06  | Payroll-Datenexport & Transformation | Compensations               | Planned     |
| 07  | Bulk Employee Onboarding             | Employees (POST)            | Planned     |
| 08  | AI-gestütztes Monitoring & Reporting | Reports, Automation         | Planned     |

## Lernprogression

1. **Grundlagen (Ticket 01-03):** Auth, CRUD, Pagination, Datenstrukturen
2. **Event-Driven (Ticket 04):** Webhooks, Real-time Sync
3. **HR-Tech (Ticket 05-06):** Recruiting, Payroll, Systemintegration
4. **Skalierung (Ticket 07-08):** Bulk-Operationen, Monitoring, AI-Tools

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ticket 01 — Output

```
=== PERSONIO EMPLOYEE SYNC ===
Datum: 2026-03-26 22:18
Modus: MOCK

Auth: Mock-Modus aktiv
Mock: 12 Mitarbeiter geladen
=== PERSONIO EMPLOYEE SYNC REPORT ===
Quelle: Personio API (TechStart GmbH)

Gesamtzahl Mitarbeiter: 12
Aktive Mitarbeiter: 10
Inaktive Mitarbeiter: 2

--- Mitarbeiter nach Abteilung ---
Engineering: 4
Marketing: 3
HR: 2
Finance: 2
Sales: 1

--- Mitarbeiterliste ---
[001] Max Mustermann | Engineering | Senior Developer | max@techstart.de
[002] Anna Weber | Engineering | Junior Developer | anna@techstart.de
[003] Tom Fischer | Engineering | DevOps Engineer | tom@techstart.de
[004] Sarah Klein | Engineering | QA Engineer | sarah@techstart.de
[005] Lisa Schmidt | Marketing | Marketing Manager | lisa@techstart.de
[006] Jonas Braun | Marketing | Content Specialist | jonas@techstart.de
[007] Nina Hoffmann | Marketing | SEO Manager | nina@techstart.de
[008] Laura Krüger | HR | HR Operations Lead | laura@techstart.de
[009] David Neumann | HR | Recruiter | david@techstart.de
[010] Michael Wagner | Finance | Finance Manager | michael@techstart.de
[011] Julia Becker | Finance | Accountant | julia@techstart.de
[012] Patrick Müller | Sales | Account Executive | patrick@techstart.de
```

## Ticket 02 — Output

```
=== PERSONIO APPLICANT PIPELINE ===
Datum: 2026-04-21 12:42
Modus: MOCK

Auth: Mock-Modus aktiv
Mock: 15 Bewerber geladen
=== PERSONIO APPLICANT PIPELINE REPORT ===
Quelle: Personio API (TechStart GmbH)

Gesamtzahl Bewerber: 15
Offen:       8  (53%)
Eingestellt: 4  (27%)
Abgelehnt:   3  (20%)

--- Pipeline nach Position ---
Software Engineer: 5
Product Manager: 4
Marketing Manager: 3
DevOps Engineer: 3

--- Pipeline nach Quelle ---
Karriereseite: 6
LinkedIn: 5
Empfehlung: 4

Conversion Rate (hired/total): 26.7%

--- Bewerber anlegen (Test) ---
✓ Neuer Bewerber angelegt: Maria Testova | maria@test.de | Software Engineer
```

## Ticket 03 — Output

```
=== SAP → PERSONIO XML TRANSFORMATION ===
Datum: 2026-04-21 15:43
Quelle: SAP SuccessFactors (Siemens AG)

XML geparst: 10 Datensätze gefunden
Gesamt verarbeitet: 10
✓ Erfolgreich transformiert: 8
✗ Fehler (fehlende Pflichtfelder): 2

--- Feldmapping ---
SAP FirstName            → Personio first_name           ✓
SAP LastName             → Personio last_name            ✓
SAP EmailAddress         → Personio email                ✓
SAP JobTitle             → Personio position             ✓
SAP ApplicationDate      → Personio application_date     ✓
SAP RecruitingStatus     → Personio status               ✓
SAP SourceType           → Personio source               ✓

--- Transformierte Datensätze ---
[001] Maria Schmidt    | maria.schmidt@siemens.de  | Software Engineer | open
[002] Klaus Müller     | klaus.mueller@siemens.de  | Software Engineer | hired
[003] Sarah Weber      | sarah.weber@siemens.de    | Software Engineer | rejected
[004] Thomas Bauer     | thomas.bauer@siemens.de   | DevOps Engineer   | hired
[005] Anna Hoffmann    | anna.hoffmann@siemens.de  | DevOps Engineer   | open
[006] Felix Richter    | felix.richter@siemens.de  | Product Manager   | open
[007] Laura Braun      | laura.braun@siemens.de    | Product Manager   | open
[008] Nico Koch        | nico.koch@siemens.de      | Data Analyst      | open

--- Fehler ---
✗ Peter Lang  | Fehlende Pflichtfelder: email, position
✗ Julia None  | Fehlende Pflichtfelder: last_name
```
