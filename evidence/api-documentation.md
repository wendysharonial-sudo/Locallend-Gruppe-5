# API-Dokumentation

## Verantwortlich

Maryam – API & Anfrage-System

## Beschreibung

Die API stellt Daten im JSON-Format bereit und verwaltet Ausleihanfragen für LocalLend.

Alle API-Antworten haben eine einheitliche Struktur:

```json
{
  "success": true,
  "message": "Kurze Beschreibung der Antwort",
  "data": {}
}
```

---

## Endpunkt: `/api/items`

### Methode

GET

### Beschreibung

Gibt alle verfügbaren Gegenstände als JSON zurück.

### Beispielantwort

```json
{
  "success": true,
  "message": "Items loaded successfully",
  "data": [
    {
      "id": 1,
      "name": "Bohrmaschine",
      "category": "Werkzeug",
      "status": "available"
    },
    {
      "id": 2,
      "name": "Leiter",
      "category": "Werkzeug",
      "status": "available"
    }
  ]
}
```

---

## Endpunkt: `/api/requests`

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

---

## Endpunkt: `/api/create_request`

### Methode

GET

### Beschreibung

Erstellt eine neue Ausleihanfrage.

Neue Anfragen erhalten automatisch den Status `pending`, bis der Verleiher über die Anfrage entscheidet.

### Beispielantwort

```json
{
  "success": true,
  "message": "Request created successfully",
  "data": {
    "id": 4,
    "item": "Laptop",
    "borrower": "Maryam",
    "status": "pending"
  }
}
```

---

## Endpunkt: `/api/accept_request`

### Methode

GET

### Beschreibung

Nimmt eine Ausleihanfrage an.

Der Status der Anfrage wird auf `accepted` gesetzt.

### Beispielantwort

```json
{
  "success": true,
  "message": "Request accepted successfully",
  "data": {
    "id": 1,
    "status": "accepted"
  }
}
```

---

## Endpunkt: `/api/reject_request`

### Methode

GET

### Beschreibung

Lehnt eine Ausleihanfrage ab.

Der Status der Anfrage wird auf `rejected` gesetzt.

### Beispielantwort

```json
{
  "success": true,
  "message": "Request rejected successfully",
  "data": {
    "id": 2,
    "status": "rejected"
  }
}
```

---

## Endpunkt: `/api/delete_request`

### Methode

GET

### Beschreibung

Löscht eine Ausleihanfrage beispielhaft.

Der Status der Anfrage wird auf `deleted` gesetzt.

### Beispielantwort

```json
{
  "success": true,
  "message": "Request deleted successfully",
  "data": {
    "id": 3,
    "status": "deleted"
  }
}
```

---

## Endpunkt: `/api/status`

### Methode

GET

### Beschreibung

Gibt den aktuellen Status der API zurück.

Dieser Endpunkt dient zur Überprüfung, ob die API erreichbar ist. Zusätzlich zeigt er den API-Namen, die Version, den Laufzeitstatus und alle verfügbaren Endpunkte.

### Beispielantwort

```json
{
  "success": true,
  "message": "API is running",
  "data": {
    "api": "LocalLend API",
    "version": "1.0",
    "status": "running",
    "available_endpoints": [
      "/api/items",
      "/api/requests",
      "/api/create_request",
      "/api/accept_request",
      "/api/reject_request",
      "/api/delete_request",
      "/api/status"
    ]
  }
}
```

---

## Erklärung der wichtigsten Felder

| Feld | Bedeutung |
|---|---|
| success | Zeigt, ob die Anfrage erfolgreich war |
| message | Beschreibt kurz das Ergebnis |
| data | Enthält die eigentlichen Daten |
| id | Eindeutige Nummer eines Gegenstands oder einer Anfrage |
| item | Angefragter Gegenstand |
| borrower | Name der ausleihenden Person |
| category | Kategorie des Gegenstands |
| status | Aktueller Status eines Gegenstands oder einer Anfrage |

---

## Statuswerte

| Status | Bedeutung |
|---|---|
| pending | Anfrage wurde erstellt und wartet auf Entscheidung |
| accepted | Anfrage wurde angenommen |
| rejected | Anfrage wurde abgelehnt |
| deleted | Anfrage wurde gelöscht |
| available | Gegenstand ist verfügbar |

---

## Anfrage-Workflow

1. Ein Benutzer erstellt eine Ausleihanfrage.
2. Die Anfrage erhält den Status `pending`.
3. Die Anfrage kann angenommen werden.
4. Bei Annahme erhält sie den Status `accepted`.
5. Die Anfrage kann abgelehnt werden.
6. Bei Ablehnung erhält sie den Status `rejected`.
7. Eine Anfrage kann außerdem gelöscht werden.
8. Beim Löschen erhält sie den Status `deleted`.

---

## Verwendete Technologien

- Python
- Flask
- JSON
- Git
- GitHub

---

## JSON-Erklärung

JSON steht für **JavaScript Object Notation**.

JSON ist ein strukturiertes Datenformat, das häufig für den Datenaustausch zwischen Backend und Frontend verwendet wird.

Ein JSON-Objekt besteht aus Schlüssel-Wert-Paaren.

### Beispiel

```json
{
  "id": 1,
  "name": "Bohrmaschine",
  "status": "available"
}
```

JSON ermöglicht den Datenaustausch zwischen Backend und Frontend.

---

## Beitrag von Maryam

- API-Endpunkte erstellt
- JSON-Daten bereitgestellt
- Einheitliche API-Antwortstruktur umgesetzt
- Ausleihanfragen verwaltet
- Anfrage erstellen implementiert
- Anfrage annehmen implementiert
- Anfrage ablehnen implementiert
- Anfrage löschen implementiert
- Statusverwaltung umgesetzt
- API getestet
- Anfrage-Workflow dokumentiert
- API-Dokumentation erstellt und gepflegt wie lange braucht man um das einzutippen