# API-Testdokumentation

## Verantwortlich

**Maryam – API & Request-System**

## Zweck

Die API-Endpunkte wurden lokal getestet, um sicherzustellen, dass sie gültige JSON-Antworten zurückgeben und die erwartete Funktionalität korrekt umsetzen.

---

## Getestete API-Endpunkte

### /api/items

**Methode:** GET

**Erwartetes Ergebnis:**

Gibt alle verfügbaren Gegenstände als JSON-Daten zurück.

**Status:** Erfolgreich getestet

---

### /api/requests

**Methode:** GET

**Erwartetes Ergebnis:**

Gibt alle Ausleihanfragen inklusive ihres aktuellen Status zurück.

**Status:** Erfolgreich getestet

---

### /api/create_request

**Methode:** GET

**Erwartetes Ergebnis:**

Erstellt eine neue Ausleihanfrage mit dem Status `pending`.

**Status:** Erfolgreich getestet

---

### /api/accept_request

**Methode:** GET

**Erwartetes Ergebnis:**

Ändert den Status einer Anfrage auf `accepted`.

**Status:** Erfolgreich getestet

---

### /api/reject_request

**Methode:** GET

**Erwartetes Ergebnis:**

Ändert den Status einer Anfrage auf `rejected`.

**Status:** Erfolgreich getestet

---

### /api/delete_request

**Methode:** GET

**Erwartetes Ergebnis:**

Ändert den Status einer Anfrage auf `deleted`.

**Status:** Erfolgreich getestet

---

### /api/status

**Methode:** GET

**Erwartetes Ergebnis:**

Liefert Informationen über die API sowie eine Übersicht aller verfügbaren Endpunkte.

**Status:** Erfolgreich getestet

---

## Testergebnisse

Alle implementierten API-Endpunkte lieferten gültige JSON-Antworten zurück.

Die Antwortstruktur war bei allen Endpunkten konsistent aufgebaut und enthielt die folgenden Felder:

- success
- message
- data

Die Statuswerte

- pending
- accepted
- rejected
- deleted
- available

wurden in allen Tests korrekt verarbeitet und zurückgegeben.

---

## Verwendete Technologien

- Python
- Flask
- JSON
- Browser-Tests
- Git
- GitHub

---


## Fazit

Die LocalLend-API wurde erfolgreich getestet und alle implementierten Endpunkte funktionierten wie erwartet.

Sowohl der Anfrageprozess als auch die Verwaltung der verschiedenen Statuswerte konnten durch manuelle Tests im Browser erfolgreich überprüft werden.

Die Testergebnisse bestätigen die korrekte Kommunikation zwischen Frontend und Backend sowie die zuverlässige Bereitstellung von JSON-Daten über die API.