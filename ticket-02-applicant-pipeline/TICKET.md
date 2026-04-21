# Ticket 02 — Applicant Pipeline Sync

## Kundeninformation

| Feld | Details |
|------|---------|
| **Kunde** | TechStart GmbH |
| **Mitarbeiter** | ~120 |
| **Plan** | Personio Core + Recruiting |
| **Melder** | David Neumann, Recruiter |
| **Priorität** | Hoch |

## Was der Kunde berichtet

> "Wir bekommen Bewerbungen über verschiedene Kanäle — Karriereseite, LinkedIn, Empfehlungen.
> Aber wir haben keinen Überblick: Wie viele Bewerber sind gerade in der Pipeline?
> Wie viele wurden abgelehnt, wie viele eingestellt? Und wenn wir einen neuen Bewerber
> manuell anlegen wollen, müssen wir das immer im UI machen. Gibt es eine API dafür?"

## Was wir wissen

- TechStart nutzt Personio Recruiting (ATS-Modul)
- Bewerbungen kommen aus verschiedenen Quellen (Karriereseite, direkt, Empfehlung)
- Relevante Felder: Name, E-Mail, Position, Status, Quelle, Bewerbungsdatum
- Mögliche Status: `open`, `rejected`, `hired`
- Das Team will einen täglichen Pipeline-Report

## Deine Aufgabe als Implementation Specialist

1. **Alle Bewerber abrufen** mit Pagination (`GET /v1/company/applicants`)
2. **Neuen Bewerber anlegen** via POST Request (`POST /v1/company/applicants`)
3. **JSON parsen** — Personio Applicant-Struktur in flaches Dict transformieren
4. **Pipeline Report generieren** — Aufschlüsselung nach Status und Quelle, Conversion Rate

## Personio API Konzepte

- **Applicants:** `GET /v1/company/applicants` mit `limit` + `offset` Pagination
- **Create:** `POST /v1/company/applicants` mit JSON Body
- **Status Filter:** Parameter `recruiting_status` für gezielten Abruf
- **Attribute:** Gleiche verschachtelte Struktur wie bei Employees

## Erwarteter Output

```
=== PERSONIO APPLICANT PIPELINE REPORT ===
Datum: 2026-04-21
Quelle: Personio API (TechStart GmbH)

Gesamtzahl Bewerber: 15
Offen:      8  (53%)
Eingestellt: 4  (27%)
Abgelehnt:  3  (20%)

--- Pipeline nach Position ---
Software Engineer:    5
Product Manager:      4
Marketing Manager:    3
DevOps Engineer:      3

--- Pipeline nach Quelle ---
Karriereseite:  6
LinkedIn:       5
Empfehlung:     4

Conversion Rate (hired/total): 26.7%

--- Bewerber anlegen (Test) ---
✓ Neuer Bewerber angelegt: Maria Testova | maria@test.de | Software Engineer
```
