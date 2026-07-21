# API-Erklärung

**Verantwortlich:** Maryam Joumma

---

## Zweck

Dieses Dokument erklärt die Funktionsweise der LocalLend-API, die Verwendung von JSON sowie den Ablauf des Anfrage- und Verleihsystems.

---

## Was ist eine API?

API steht für **Application Programming Interface (Programmierschnittstelle)**.

Eine API ermöglicht die Kommunikation zwischen verschiedenen Teilen einer Anwendung. Im Projekt **LocalLend** stellt die API Informationen über Gegenstände und Ausleihanfragen bereit.

| API-Funktion | Beschreibung |
|--------------|--------------|
| Gegenstände | Informationen über verfügbare Gegenstände |
| Anfragen | Verwaltung von Ausleihanfragen |
| Status | Aktualisierung des Anfrage-Status |

Anstatt eine normale Webseite zurückzugeben, liefert die API strukturierte Daten im **JSON-Format**.

---

## Was ist JSON?

JSON (**JavaScript Object Notation**) ist ein standardisiertes Datenformat für den Datenaustausch zwischen Frontend und Backend.

**Beispiel:**

```json
{
  "id": 1,
  "name": "Bohrmaschine",
  "status": "verfügbar"
}
```

---

## Frontend und Backend

| Frontend | Backend |
|-----------|----------|
| Benutzeroberfläche | Flask-Anwendung |
| Formulare | API-Endpunkte |
| Navigation | Datenverarbeitung |
| Darstellung der Daten | Datenbankzugriffe |

Das Frontend sendet Anfragen an das Backend. Das Backend verarbeitet diese und gibt die Daten als JSON-Antwort zurück.

---

## Datenfluss

```text
Benutzer
    ↓
Frontend
    ↓
API-Endpunkt
    ↓
Flask-Backend
    ↓
JSON-Antwort
    ↓
Frontend
```

---

## Die Funktion `jsonify()`

Mit `jsonify()` werden Python-Daten als JSON-Antwort zurückgegeben.

```python
return jsonify({
    "success": True,
    "message": "Gegenstände erfolgreich geladen",
    "data": items
})
```

---

## Ablauf des Anfrage-Systems

| Schritt | Status |
|----------|--------|
| Anfrage erstellt | `pending` |
| Anfrage akzeptiert | `accepted` |
| Anfrage abgelehnt | `rejected` |
| Anfrage gelöscht | `deleted` |

---

## Fazit

Die LocalLend-API stellt strukturierte JSON-Daten bereit und ermöglicht die Kommunikation zwischen Frontend und Backend. Sie verwaltet Gegenstände, Ausleihanfragen und deren Status.