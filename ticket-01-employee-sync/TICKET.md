# Ticket 01 — Employee Data Sync

## Kundeninformation

| Feld | Details |
|------|---------|
| **Kunde** | TechStart GmbH |
| **Mitarbeiter** | ~120 |
| **Plan** | Personio Core |
| **Melder** | Lisa Krüger, HR Operations Lead |
| **Priorität** | Hoch |

## Was die Kundin berichtet

> "Wir nutzen Personio als HR-System, aber unser internes Mitarbeiterverzeichnis (Intranet)
> ist nie aktuell. Neue Mitarbeiter tauchen erst Tage später auf, Abteilungswechsel werden
> gar nicht übernommen. Wir brauchen einen automatischen Sync von Personio in unser System."

## Was wir wissen

- Die Kundin hat API-Credentials in Personio bereits erstellt (Settings > API > Credentials)
- Das Intranet akzeptiert JSON-Daten über eine interne API
- Es gibt ca. 120 aktive Mitarbeiter
- Relevante Felder: Name, E-Mail, Abteilung, Position, Eintrittsdatum, Status

## Deine Aufgabe als Implementation Specialist

1. **Authentifizierung** gegen die Personio API implementieren (Client Credentials → Bearer Token)
2. **Alle aktiven Mitarbeiter abrufen** (mit Pagination — max 200 pro Request)
3. **JSON-Antwort parsen** — verschachtelte Personio-Struktur in flaches Dict transformieren
4. **Sync-Report generieren** — Zusammenfassung nach Abteilung, Status, neue MA

## Personio API Konzepte

- **Auth:** `POST /v1/auth` mit `client_id` + `client_secret` → Bearer Token (24h gültig)
- **Employees:** `GET /v1/company/employees` mit `limit` + `offset` Pagination
- **Verschachtelte Attribute:** Employee-Felder liegen in `attributes.field_name.value`
- **Relationen:** Abteilung ist verschachtelt: `attributes.department.value.attributes.name`

## Erwarteter Output

```
=== PERSONIO EMPLOYEE SYNC REPORT ===
Datum: 2026-03-26
Quelle: Personio API (TechStart GmbH)

Gesamtzahl Mitarbeiter: 12
Aktive Mitarbeiter: 10
Inaktive Mitarbeiter: 2

--- Mitarbeiter nach Abteilung ---
Engineering: 4
Marketing: 3
HR: 2
Finance: 1

--- Mitarbeiterliste ---
[001] Max Mustermann | Engineering | Senior Developer | max@techstart.de
[002] Lisa Schmidt | Marketing | Marketing Manager | lisa@techstart.de
...
```
