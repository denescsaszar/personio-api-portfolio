# Personio API Portfolio — Technical Implementation Specialist

Hands-on Portfolio mit realen Implementierungs-Szenarien für die Personio REST API.
Jedes Ticket simuliert ein echtes Kundenproblem, das als Technical Implementation Specialist gelöst wird.

## Stack

- **Sprache:** Python 3.11
- **HTTP Client:** requests (keine SDK — direkter REST API Zugriff)
- **API:** Personio REST API v1/v2
- **Datenformate:** JSON

## Ticket-Übersicht

| # | Szenario | Personio API Bereich | Status |
|---|----------|---------------------|--------|
| 01 | Employee Data Sync | Auth, Employees, Pagination | In Progress |
| 02 | Attendance-Integration | Attendance Periods | Planned |
| 03 | Absence-Management | Absence Periods, Types | Planned |
| 04 | Webhook-Setup & Event-Processing | Webhooks | Planned |
| 05 | Recruiting-Pipeline & ATS-Anbindung | Recruiting API | Planned |
| 06 | Payroll-Datenexport & Transformation | Compensations | Planned |
| 07 | Bulk Employee Onboarding | Employees (POST) | Planned |
| 08 | AI-gestütztes Monitoring & Reporting | Reports, Automation | Planned |

## Lernprogression

1. **Grundlagen (Ticket 01-03):** Auth, CRUD, Pagination, Datenstrukturen
2. **Event-Driven (Ticket 04):** Webhooks, Real-time Sync
3. **HR-Tech (Ticket 05-06):** Recruiting, Payroll, Systemintegration
4. **Skalierung (Ticket 07-08):** Bulk-Operationen, Monitoring, AI-Tools

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # API Credentials eintragen
```
