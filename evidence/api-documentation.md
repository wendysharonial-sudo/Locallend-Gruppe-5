# API-Dokumentation

## Verantwortlich
Maryam – API & Anfrage-System

## Beschreibung

Die API stellt Daten im JSON-Format bereit und verwaltet Ausleihanfragen.

---

## Endpunkt: /api/items

### Beschreibung
Gibt alle verfügbaren Gegenstände als JSON zurück.
### Methode 
GET 
### Beispielantwort
```json
{
    "success": true,
    "message": "Items loaded successfully",
    "data": [
        {
            "id":1,
            "name": "Bohrmaschine",
            "category": "Werkzeug",
            "status": "available"
        },
        {
           "id": 2,
           "name": "Leiter"
           "categorie": "Werkzeug",
           "status": "available"
        }
    ]
}

## Endpunkt: /api/requests

### Methode

GET

### Beschreibung

Gibt alle Ausleihanfragen und deren aktuellen Status als JSON zurück.

### Beispielantwort

```json
{
  "success": true,
  "message": "Requests loaded successfully",
  "data": [
    {
      "id": 1,
      "item": "Bohrmaschine",
      "borrower": "Max",
      "status": "pending"
    },
    {
      "id": 2,
      "item": "Leiter",
      "borrower": "Anna",
      "status": "accepted"
    },
    {
      "id": 3,
      "item": "Beamer",
      "borrower": "Sara",
      "status": "rejected"
    }
  ]
}
```

### Erklärung der Felder

| Feld | Bedeutung |
|---|---|
| id | Eindeutige Nummer der Anfrage |
| item | Angefragter Gegenstand |
| borrower | Name des Ausleihers |
| status | Aktueller Status der Anfrage |

---

## Endpunkt: /api/create_request

Methode: GET

Beschreibung:
Erstellt eine neue Ausleihanfrage.

Beispiel:

{
    "id": 4,
    "item": "Laptop",
    "borrower": "Maryam",
    "status": "pending"
}

---

## Endpunkt: /api/accept_request

Methode: GET

Beschreibung:
Nimmt eine Anfrage an.

Beispiel:

{
    "id": 1,
    "status": "accepted"
}

---

## Endpunkt: /api/reject_request

Methode: GET

Beschreibung:
Lehnt eine Anfrage ab.

Beispiel:

{
    "id": 2,
    "status": "rejected"
}
## Endpunkt: /api/delete_request

Methode: GET

Beschreibung: 
Löscht eine Anfrage.

Beispiel:

{
    "id": 3,
    "status": "deleted"
}

---

## API Status Übersicht

Der Endpoint `/api/status´ dient zur Überprüfung des aktuellen API-Zustands.
Er liefert:

-API Name
-Version
-Laufzeitstatus
Liste aller verfügbaren Endpunkte 

Dieser Endpoint kann für Monitoring und Debuggig verwendet werden.

# Anfrage-Workflow

1. Ein Benutzer erstellt eine Anfrage.
2. Die Anfrage erhält den Status "pending".
3. Die Anfrage kann angenommen werden.
4. Dann erhält sie den Status "accepted".
5. Die Anfrage kann auch abgelehnt werden.
6. Dann erhält sie den Status "rejected".

## statuswerte
## Statuswerte

| Status | Bedeutung |
|----------|----------|
| pending | Anfrage wurde erstellt |
| accepted | Anfrage wurde angenommen |
| rejected | Anfrage wurde abgelehnt |
| deleted | Anfrage wurde gelöscht |
# Verwendete Technologie

- Python
- Flask
- JSON
- Git
- GitHub
## JSON Erklärung

JSON steht für javaScript object Notation.

Die API liefert Daten im JSON-Format.

Beispiel:
{
    "id": 1,
    "name":"Bohrmaschine"
    "status":"availabe"
}
JSON ermöglicht den Datenautausch zwischen Backend und Frontend.
# Beitrag von Maryam

- API-Endpunkte erstellt
- JSON-Daten bereitgestellt
- Ausleihanfragen verwaltet
- Anfrage erstellen implementiert
- Anfrage annehmen implementiert
- Anfrage ablehnen implementiert
- Statusverwaltung umgesetzt
- API getestet
- Anfrage-Workflow dokumentiert