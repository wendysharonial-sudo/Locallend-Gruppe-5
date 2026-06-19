# API-Dokumentation

## Verantwortlich
Maryam – API & Anfrage-System

## Beschreibung

Die API stellt Daten im JSON-Format bereit und verwaltet Ausleihanfragen.

---

## Endpunkt: /api/items

Methode: GET

Beschreibung:
Gibt eine Liste aller verfügbaren Gegenstände zurück.

Beispiel:

[
    {
        "id": 1,
        "name": "Bohrmaschine",
        "status": "available"
    },
    {
        "id": 2,
        "name": "Leiter",
        "status": "available"
    }
]

---

## Endpunkt: /api/requests

Methode: GET

Beschreibung:
Gibt alle Ausleihanfragen zurück.

Statuswerte:

- pending
- accepted
- rejected

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

---

# Anfrage-Workflow

1. Ein Benutzer erstellt eine Anfrage.
2. Die Anfrage erhält den Status "pending".
3. Die Anfrage kann angenommen werden.
4. Dann erhält sie den Status "accepted".
5. Die Anfrage kann auch abgelehnt werden.
6. Dann erhält sie den Status "rejected".

# Verwendete Technologie

- Python
- Flask
- JSON
- Git
- GitHub

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