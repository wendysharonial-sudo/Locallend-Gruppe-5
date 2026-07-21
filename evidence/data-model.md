# Data Model - LocalLend

## Ziel des Datenmodells 

Das Datenmodell beschreibt, welche Daten die Anwendung speichern muss und wie diese miteinander verbunden sind.

Für LocalLend werden drei zentrale Datenbereiche benötigt:

- Nutzer
- Gegenstände
- Ausleihanfragen

Diese drei Bereiche bilden die Grundlage für den gesamten Happy Path der Anwendung.

---

# Übersicht der Tabellen

| Tabelle | Zweck |
|----------|-------|
| users | Speichert registrierte Nutzer |
| items | Speichert Gegenstände, die verliehen werden können |
| requests | Speichert Ausleihanfragen zwischen Nutzern und Gegenständen |

---

# Beziehungen zwischen den Tabellen

Ein Nutzer kann mehrere Gegenstände einstellen.

Ein Gegenstand gehört genau einem Nutzer.

Ein Nutzer kann mehrere Ausleihanfragen stellen.

Eine Ausleihanfrage bezieht sich immer genau auf einen Gegenstand.

```
users
  │
  ├──── items

users
  │
  └──── requests

items
  │
  └──── requests
```

---

# Tabelle: users

Speichert alle registrierten Nutzer der Plattform.

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| user_id | INTEGER | Eindeutige Nutzer-ID (Primary Key) |
| first_name | TEXT | Vorname |
| last_name | TEXT | Nachname |
| email | TEXT | E-Mail-Adresse |
| password | TEXT | Verschlüsseltes Passwort |

## Primärschlüssel

- user_id

## Begründung

Jeder Nutzer benötigt eine eindeutige ID.

Die E-Mail dient gleichzeitig als eindeutiger Login.

Das Passwort wird verschlüsselt gespeichert.

---

# Tabelle: items

Speichert alle Gegenstände, die Nutzer verleihen möchten.

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| item_id | INTEGER | Eindeutige Gegenstands-ID (Primary Key) |
| user_id | INTEGER | Besitzer des Gegenstands (Foreign Key) |
| title | TEXT | Name des Gegenstands |
| description | TEXT | Beschreibung |
| category | TEXT | Kategorie |
| availability | TEXT | Aktueller Verfügbarkeitsstatus |

## Primärschlüssel

- item_id

## Fremdschlüssel

- user_id → users.user_id

## Begründung

Jeder Gegenstand gehört genau einem Nutzer.

Dadurch weiß das System jederzeit, wem der Gegenstand gehört.

Das Feld **availability** zeigt den aktuellen Zustand des Gegenstands.

Mögliche Werte:

- available
- borrowed

Wird eine Anfrage angenommen, wird der Gegenstand auf **borrowed** gesetzt.

Nach der Rückgabe erhält er wieder den Status **available**.

---

# Tabelle: requests

Speichert alle Ausleihanfragen zwischen Nutzern und Gegenständen.

| Feld | Datentyp | Beschreibung |
|------|----------|--------------|
| request_id | INTEGER | Eindeutige Anfrage-ID (Primary Key) |
| item_id | INTEGER | Angefragter Gegenstand (Foreign Key) |
| borrower_id | INTEGER | Nutzer, der die Anfrage stellt (Foreign Key) |
| status | TEXT | Status der Anfrage |
| request_date | DATETIME | Zeitpunkt der Anfrage |
| message | TEXT | Optionale Nachricht |

## Primärschlüssel

- request_id

## Fremdschlüssel

- item_id → items.item_id

- borrower_id → users.user_id

## Begründung

Die Tabelle requests verwaltet den kompletten Ausleihprozess.

Über item_id wird gespeichert, welcher Gegenstand ausgeliehen werden soll.

Über borrower_id wird gespeichert, welcher Nutzer die Anfrage gestellt hat.

Der Status beschreibt den aktuellen Stand der Anfrage.

Mögliche Statuswerte:

- pending
- accepted
- rejected
- returned

Bedeutung:

- pending → Anfrage wurde gestellt.
- accepted → Anfrage wurde angenommen.
- rejected → Anfrage wurde abgelehnt.
- returned → Gegenstand wurde erfolgreich zurückgegeben.

---

# Zusammenfassung des Datenmodells

Das Datenmodell basiert auf drei zentralen Tabellen.

## users

Verwaltet alle registrierten Nutzer.

## items

Verwaltet alle angebotenen Gegenstände.

Über das Feld **availability** erkennt das System sofort, ob ein Gegenstand ausgeliehen werden kann.

## requests

Verwaltet sämtliche Ausleihanfragen.

Der Status dokumentiert den gesamten Ablauf einer Ausleihe – von der Anfrage bis zur Rückgabe.

---

# Happy Path

Dieses Datenmodell unterstützt den vollständigen Ablauf von LocalLend:

1. Nutzer registriert sich.
2. Nutzer erstellt einen Gegenstand.
3. Ein anderer Nutzer durchsucht verfügbare Gegenstände.
4. Nutzer stellt eine Ausleihanfrage.
5. Der Verleiher akzeptiert oder lehnt die Anfrage ab.
6. Bei Annahme erhält der Request den Status **accepted** und der Gegenstand den Status **borrowed**.
7. Nach der Rückgabe erhält der Request den Status **returned**.
8. Der Gegenstand wird wieder auf **available** gesetzt und kann erneut ausgeliehen werden.

## ER- Diagramm

Das folgende Diagramm zeigt die Beziehungen zwischen den Tabellen `users`, `items` und `requests`.

![ER-Diagramm](./ER-diagramm.png)

