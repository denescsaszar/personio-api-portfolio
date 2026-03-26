# Personio API Portfolio — Technical Implementation Specialist

Hands-on Portfolio mit realen Implementierungs-Szenarien für die Personio REST API.
Jedes Ticket simuliert ein echtes Kundenproblem, das als Technical Implementation Specialist gelöst wird.

## Stack

- **Sprache:** Python 3.11
- **HTTP Client:** requests (keine SDK — direkter REST API Zugriff)
- **API:** Personio REST API v1/v2
- **Datenformate:** JSON

## Ticket-Übersicht

| #   | Szenario                             | Personio API Bereich        | Status      |
| --- | ------------------------------------ | --------------------------- | ----------- |
| 01  | Employee Data Sync                   | Auth, Employees, Pagination | In Progress |
| 02  | Attendance-Integration               | Attendance Periods          | Planned     |
| 03  | Absence-Management                   | Absence Periods, Types      | Planned     |
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
