# API-Erklärung

## Verantwortlich

Maryam – API und Anfrage-System

## Ziel

Die API stellt ausgewählte Daten der LocalLend-Anwendung im JSON-Format bereit. Dadurch können Informationen unabhängig von den HTML-Seiten abgerufen werden.

Die API erfüllt außerdem die Projektanforderung eines headless API-Endpunkts.

---

## Funktionsweise

Die API wurde mit Flask umgesetzt.

Jeder API-Endpunkt ist über eine eigene Route erreichbar. Wird ein Endpunkt aufgerufen, liest SQLAlchemy die benötigten Daten aus der SQLite-Datenbank.

Die Daten werden anschließend in Python verarbeitet und mit `jsonify()` als JSON zurückgegeben.

---

## API-Endpunkte

### `/api/items`

Dieser Endpunkt gibt alle vorhandenen Gegenstände zurück.

Für jeden Gegenstand werden folgende Informationen ausgegeben:

- ID
- Titel
- Kategorie
- Beschreibung
- Verfügbarkeit

---

### `/api/requests`

Dieser Endpunkt gibt alle Ausleihanfragen zurück.

Für jede Anfrage werden folgende Informationen ausgegeben:

- Anfrage-ID
- Gegenstand
- Ausleiher
- Status

Der Status zeigt an, ob eine Anfrage noch offen (`pending`), angenommen (`accepted`) oder abgelehnt (`rejected`) wurde.

---

### `/api/status`

Dieser Endpunkt zeigt, ob die API erreichbar ist.

Zusätzlich werden allgemeine Informationen über die API und die verfügbaren Endpunkte zurückgegeben.

---

## Aufbau einer Antwort

Alle API-Antworten besitzen dieselbe Struktur.

- `success` zeigt, ob die Anfrage erfolgreich war.
- `message` enthält eine kurze Beschreibung.
- `data` enthält die eigentlichen Informationen.

Diese einheitliche Struktur erleichtert die Nutzung und das Testen der API.

---

## Fazit

Die API stellt Daten strukturiert im JSON-Format bereit und trennt die Datenbereitstellung von der Darstellung im Browser. Dadurch können die Endpunkte einfach getestet und dokumentiert werden.