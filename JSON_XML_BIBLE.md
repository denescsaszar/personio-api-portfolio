# JSON & XML BIBLE
# Komplette Referenz für Datenstrukturen & Transformation

---

## 1. JSON Grundlagen

### Was ist JSON?
JSON = JavaScript Object Notation
Leichtgewichtiges Dateiformat für Datenaustausch zwischen Systemen.
Personio, Workday, die meisten modernen APIs → JSON.

### Datentypen
```json
{
  "string":  "Hallo Welt",
  "number":  42,
  "float":   3.14,
  "boolean": true,
  "null":    null,
  "array":   [1, 2, 3],
  "object":  {"key": "value"}
}
```

### Verschachtelte Objekte (Nesting)
```json
{
  "employee": {
    "name": "Max",
    "address": {
      "city": "Berlin",
      "zip": "10115"
    }
  }
}
```

In Python zugreifen:
```python
data["employee"]["address"]["city"]  # → "Berlin"
```

---

## 2. JSON in Python

### Parsen (String → Dict)
```python
import json

json_string = '{"name": "Max", "age": 30}'
data = json.loads(json_string)   # String → Dict
print(data["name"])              # → "Max"
```

### Serialisieren (Dict → String)
```python
data = {"name": "Max", "age": 30}
json_string = json.dumps(data)              # Dict → String
json_pretty = json.dumps(data, indent=2)    # Formatiert ausgeben
```

### Mit requests (API Calls)
```python
# Request mit JSON Body senden:
response = requests.post(url, json={"key": "value"})
# requests setzt automatisch Content-Type: application/json

# JSON Response empfangen:
data = response.json()   # Parsed automatisch
```

---

## 3. Personio JSON — Das verschachtelte Schema

Personio nutzt ein besonderes Schema: jedes Feld ist ein Objekt mit `label` und `value`.

### Einfaches Feld:
```json
"first_name": {
  "label": "Vorname",
  "value": "Max"
}
```
Zugriff: `attrs["first_name"]["value"]` → `"Max"`

### Relation (verknüpftes Objekt):
```json
"department": {
  "label": "Abteilung",
  "value": {
    "type": "Department",
    "attributes": {
      "name": "Engineering"
    }
  }
}
```
Zugriff: `attrs["department"]["value"]["attributes"]["name"]` → `"Engineering"`

### Warum der Unterschied?
- Einfaches Feld → `value` ist ein String/Zahl
- Relation → `value` ist ein weiteres Objekt (mit eigenem `attributes`)
- Das erkennst du daran ob `value` ein String oder ein Dict ist

---

## 4. JSON Parsing Pattern (Personio)

```python
def parse_employee(raw_employee):
    attrs = raw_employee["attributes"]
    return {
        # Einfache Felder:
        "id":         attrs["id"]["value"],
        "first_name": attrs["first_name"]["value"],
        "last_name":  attrs["last_name"]["value"],
        "email":      attrs["email"]["value"],
        "status":     attrs["status"]["value"],

        # Relation — eine Ebene tiefer:
        "department": attrs["department"]["value"]["attributes"]["name"],
    }
```

### Sicheres Parsen (mit .get()):
```python
# Unsicher — wirft KeyError wenn Feld fehlt:
attrs["email"]["value"]

# Sicher — gibt None zurück wenn Feld fehlt:
attrs.get("email", {}).get("value")
```

---

## 5. XML Grundlagen

### Was ist XML?
XML = Extensible Markup Language
Älteres Format — SAP, SOAP APIs, ältere Enterprise Systeme → XML.
Wichtig für Integrationen mit Legacy-Systemen wie SAP SuccessFactors.

### Struktur
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Root>
    <Element attribute="wert">
        <Child>Text Inhalt</Child>
    </Element>
</Root>
```

**Wichtige Begriffe:**
| Begriff | Erklärung | Beispiel |
|---|---|---|
| Tag | Element-Name | `<FirstName>` |
| Text | Inhalt eines Elements | `Max` |
| Attribute | Eigenschaften eines Tags | `id="1"` |
| Root | Oberstes Element | `<Applicants>` |
| Child | Untergeordnetes Element | `<FirstName>` |

---

## 6. XML vs JSON — Vergleich

Gleiche Daten, zwei Formate:

### JSON (Personio):
```json
{
  "first_name": "Max",
  "last_name": "Mustermann",
  "email": "max@techstart.de",
  "department": "Engineering"
}
```

### XML (SAP SuccessFactors):
```xml
<Applicant id="1">
    <FirstName>Max</FirstName>
    <LastName>Mustermann</LastName>
    <EmailAddress>max@techstart.de</EmailAddress>
    <Department>Engineering</Department>
</Applicant>
```

### Unterschiede:
| | JSON | XML |
|---|---|---|
| Syntax | `{}` Klammern | `<tags>` |
| Datentypen | String, Number, Boolean, Array, Object, Null | Nur Text (alles ist String) |
| Attribute | Nein | Ja (`id="1"`) |
| Lesbarkeit | Kompakter | Ausführlicher |
| Verbreitung | Moderne APIs | Legacy/Enterprise (SAP) |
| Python Library | `json` (built-in) | `xml.etree.ElementTree` (built-in) |

---

## 7. XML in Python — ElementTree

### Import (kein pip nötig!):
```python
import xml.etree.ElementTree as ET
```

### XML String parsen:
```python
xml_string = """
<Applicants>
    <Applicant id="1">
        <FirstName>Max</FirstName>
        <Email>max@test.de</Email>
    </Applicant>
</Applicants>
"""

root = ET.fromstring(xml_string)
```

### Elemente finden:
```python
# Alle Applicant Elemente:
applicants = root.findall("Applicant")

# Erstes Element:
first = root.find("Applicant")

# Text lesen:
applicants[0].find("FirstName").text   # → "Max"

# Attribut lesen:
applicants[0].get("id")                # → "1"
```

### Sicheres Lesen (None-Check):
```python
element = applicant.find("FirstName")
value = element.text if element is not None else None
# Verhindert AttributeError wenn Tag fehlt
```

---

## 8. XML → JSON Transformation (was APMonster macht)

Das ist das Kernkonzept von Ticket 03 — und was talentsconnect intern täglich macht:

```python
import xml.etree.ElementTree as ET
import json

FIELD_MAPPING = {
    "FirstName":      "first_name",
    "LastName":       "last_name",
    "EmailAddress":   "email",
    "JobTitle":       "position",
}

def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    results = []

    for applicant in root.findall("Applicant"):
        record = {}
        for sap_field, personio_field in FIELD_MAPPING.items():
            element = applicant.find(sap_field)
            value = element.text if element is not None else None
            record[personio_field] = value

        results.append(record)

    return json.dumps(results, indent=2)
```

---

## 9. Validierung von Datenstrukturen

Bevor Daten in ein Zielsystem gesendet werden → Pflichtfelder prüfen!

```python
REQUIRED_FIELDS = ["first_name", "last_name", "email", "position"]

def validate(record):
    missing = [f for f in REQUIRED_FIELDS if not record.get(f)]
    return len(missing) == 0, missing

# Verwendung:
is_valid, missing = validate({"first_name": "Max", "email": "max@test.de"})
# → (False, ["last_name", "position"])
```

---

## 10. Häufige Fehler & Lösungen

### JSON:
```python
# KeyError — Feld existiert nicht:
data["fehlend"]              # ❌ wirft KeyError
data.get("fehlend")          # ✓ gibt None zurück
data.get("fehlend", "default")  # ✓ gibt Default zurück

# TypeError — falscher Typ:
data["age"] + 1              # ❌ wenn age ein String ist
int(data["age"]) + 1         # ✓ erst konvertieren

# JSONDecodeError — kein valides JSON:
json.loads("kein json")      # ❌ wirft Exception
# Lösung: try/except verwenden
```

### XML:
```python
# AttributeError — Element nicht gefunden:
root.find("NichtVorhanden").text    # ❌ .text auf None
element = root.find("NichtVorhanden")
value = element.text if element is not None else None  # ✓

# ParseError — ungültiges XML:
ET.fromstring("<nicht geschlossen>")  # ❌
# Lösung: try/except verwenden

# Encoding — Sonderzeichen:
# XML Header: <?xml version="1.0" encoding="UTF-8"?>
# Stellt sicher dass ü, ä, ö korrekt verarbeitet werden
```

---

## 11. Interview-Checkliste JSON & XML

**"Was ist der Unterschied zwischen JSON und XML?"**
> JSON: modernes Format, kompakter, für Web-APIs.
> XML: älteres Format, ausführlicher, für Enterprise/SAP.
> Beide transportieren strukturierte Daten — das Format ist nur die Verpackung.

**"Wie parsest du verschachteltes JSON?"**
> Mit `["key1"]["key2"]["key3"]` oder sicher mit `.get()`.
> Bei Personio: `attrs["department"]["value"]["attributes"]["name"]`

**"Wie transformierst du XML in JSON?"**
> ElementTree zum Parsen, FIELD_MAPPING für Feldnamen,
> dann Dict bauen und `json.dumps()` ausgeben.

**"Was machst du wenn ein Pflichtfeld fehlt?"**
> Validierung vor dem Import — fehlende Felder loggen,
> den Datensatz nicht importieren und einen Fehler-Report ausgeben.
> Nie fehlerhafte Daten ins Zielsystem schreiben!

**"Was ist APMonster?"**
> talentsconnects internes Integrations-Middleware.
> Empfängt Bewerbungen von JobShop, transformiert ins Zielformat
> (Personio JSON, SAP XML, Workday, etc.) und sendet an das ATS.
> Validiert dabei Pflichtfelder und handelt Fehler.
