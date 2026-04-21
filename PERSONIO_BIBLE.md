# PERSONIO BIBLE
# Komplette Referenz für die Personio API & Technical Implementation

---

## 1. Was ist Personio?

Personio ist eine HR-SaaS Plattform für KMU (kleine & mittelständische Unternehmen).
Kernfunktionen: Mitarbeiterverwaltung, Recruiting (ATS), Abwesenheiten, Payroll, Berichte.

**Personio Pläne:**
| Plan | REST API | Beschreibung |
|---|---|---|
| Core | ❌ | Basis HR, nur Marketplace-Integrationen |
| Core Pro | ✅ | Voller REST API Zugang + OAuth |
| Recruiting Add-on | ✅ | Separater Recruiting API Endpoint |

---

## 2. Authentifizierung

### Client Credentials Flow
```
POST /v1/auth
Body: { "client_id": "xxx", "client_secret": "yyy" }

Response:
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1..."
  }
}
```

**Wichtig:**
- Token ist **24 Stunden** gültig
- Danach neuen Token holen
- Token immer als `Authorization: Bearer <token>` Header senden

### In Python:
```python
response = requests.post(
    f"{BASE_URL}/auth",
    json={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
)
token = response.json()["data"]["token"]
```

---

## 3. Pagination

Personio gibt maximal **200 Einträge pro Request** zurück.
Bei mehr Daten → Pagination mit `limit` und `offset`.

```
GET /v1/company/employees?limit=200&offset=0    → Einträge 1-200
GET /v1/company/employees?limit=200&offset=200  → Einträge 201-400
GET /v1/company/employees?limit=200&offset=400  → leer → fertig
```

### Pattern in Python:
```python
all_results = []
offset = 0
limit = 200

while True:
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": limit, "offset": offset}
    )
    data = response.json()["data"]
    if not data:
        break
    all_results.extend(data)
    offset += limit
```

---

## 4. Personio JSON Struktur

### Das verschachtelte Attribut-Schema
Personio gibt KEINE einfachen Felder zurück — alles ist verschachtelt:

```json
{
  "type": "Employee",
  "attributes": {
    "id": {
      "label": "ID",
      "value": 1
    },
    "first_name": {
      "label": "Vorname",
      "value": "Max"
    },
    "department": {
      "label": "Abteilung",
      "value": {
        "type": "Department",
        "attributes": {
          "name": "Engineering"
        }
      }
    }
  }
}
```

### Zugriffsmuster:
```python
attrs = employee["attributes"]

# Einfaches Feld:
attrs["first_name"]["value"]           # → "Max"

# Relation (Department, Position, etc.):
attrs["department"]["value"]["attributes"]["name"]  # → "Engineering"
```

### Warum so kompliziert?
Personio-Felder können custom sein (jede Firma kann eigene Felder anlegen).
Das Schema `{"label": "...", "value": "..."}` erlaubt flexible Erweiterung.

---

## 5. Wichtige Endpoints

### Employees (HR API)
```
GET  /v1/company/employees              → Alle Mitarbeiter
GET  /v1/company/employees/{id}         → Einzelner Mitarbeiter
POST /v1/company/employees              → Neuer Mitarbeiter
PATCH /v1/company/employees/{id}        → Mitarbeiter updaten
```

### Applicants (Recruiting API)
```
GET  /v1/company/applicants             → Alle Bewerber
GET  /v1/company/applicants/{id}        → Einzelner Bewerber
POST /v1/company/applicants             → Neuer Bewerber anlegen
```

### Absences
```
GET  /v1/company/time-offs              → Abwesenheiten
POST /v1/company/time-offs              → Abwesenheit anlegen
```

### Attendance
```
GET  /v1/company/attendances            → Anwesenheiten
POST /v1/company/attendances            → Anwesenheit buchen
```

---

## 6. HTTP Status Codes

| Code | Bedeutung | Was tun? |
|---|---|---|
| 200 | OK | Alles gut |
| 201 | Created | Ressource wurde angelegt |
| 400 | Bad Request | Request Body prüfen |
| 401 | Unauthorized | Token abgelaufen → neu authentifizieren |
| 403 | Forbidden | Keine Berechtigung für diesen Endpoint |
| 404 | Not Found | ID existiert nicht |
| 422 | Unprocessable Entity | Validierungsfehler (Pflichtfelder fehlen) |
| 429 | Too Many Requests | Rate Limit — warten und retry |
| 500 | Server Error | Personio Problem — später nochmal versuchen |

---

## 7. Error Handling Pattern

```python
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Wirft Exception bei 4xx/5xx
    return response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Fehler: {e.response.status_code}")
    print(f"Details: {e.response.text}")
except requests.exceptions.ConnectionError:
    print("Verbindungsfehler — API nicht erreichbar")
except requests.exceptions.Timeout:
    print("Timeout — Request hat zu lange gedauert")
```

---

## 8. talentsconnect & APMonster Integration

### Die Architektur
```
Karriereseite (Siemens, EDEKA, Fraport)
        ↓
talentsconnect JobShop (Direct-to-Talent)
        ↓
APMonster (internes Integrations-Middleware)
        ↓
    ┌───┴───┐
Personio  SAP  Workday  Davinci  (ATS Systeme)
```

### Was APMonster macht:
1. **Empfängt** Bewerbungen von JobShop
2. **Transformiert** Daten ins Zielformat (JSON, XML, proprietär)
3. **Validiert** Pflichtfelder
4. **Sendet** an das jeweilige ATS
5. **Handelt** Fehler und Retries

### Personio Recruiting API (was du in Ticket 02 gebaut hast):
```python
POST /v1/company/applicants
Headers: Authorization: Bearer <token>
Body: {
    "first_name": "Maria",
    "last_name": "Testova",
    "email": "maria@test.de",
    "position": "Software Engineer"
}
```

---

## 9. Häufige Interview-Fragen

**"Wie funktioniert die Personio Authentifizierung?"**
> Client Credentials Flow — POST mit client_id + client_secret → Bearer Token (24h).
> Token in jedem Request als Authorization Header.

**"Warum ist die Personio JSON Struktur so verschachtelt?"**
> Personio erlaubt custom Felder. Das Schema mit label/value ermöglicht es,
> dass jede Firma eigene Felder anlegen kann ohne das Schema zu brechen.

**"Was passiert wenn der Token abläuft?"**
> API gibt 401 zurück. Lösung: Token-Refresh-Logik einbauen —
> bei 401 automatisch neu authentifizieren und Request wiederholen.

**"Wie handelt man Rate Limits?"**
> Bei 429 Response: exponential backoff — erst 1s warten, dann 2s, dann 4s.
> Oder requests auf mehrere Zeitfenster verteilen.

**"Was ist der Unterschied zwischen Core und Core Pro?"**
> Core: nur Marketplace-Integrationen (vorgefertigte Connectoren).
> Core Pro: voller REST API Zugang für custom Integrationen.

---

## 10. Debugging Checkliste

```
□ Token vorhanden und nicht abgelaufen?
□ Authorization Header korrekt? ("Bearer " + token)
□ URL korrekt? (kein doppeltes //)
□ HTTP Methode richtig? (GET vs POST vs PATCH)
□ JSON Body valide? (json.dumps() testen)
□ Pflichtfelder alle vorhanden?
□ response.raise_for_status() aufgerufen?
□ response.json() - ist es wirklich JSON?
```
