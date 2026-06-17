## DD-01 Flexible Nutzerrollen

## Metadata

| Key | Value |
|--------|--------|
| Status | Decided |
| Datum | 18.06.2026 |
| Team | LocalLend - Gruppe 5 |
| Lead | unbekannt |

---

## Problem

Während der Produktentwicklung stellt sich die Frage, ob Nutzer bereits bei der der Registrierung dauerhaft als "Verleiher" oder "Leiher" festgelegt werden soll.
Da sich unsere Zielgruppe aus Studierenden und Anwohnern zusammensetzt, die sowohl Gegenstände verleihen  als auch ausleihen können, musste entschieden werden, wie Nutzerrollen in der Anwendung modelliert werden.

---

## Decision

Wir haben uns dafür entschieden, Nutzer nicht dauerhaft einer Rolle zuzuordnen.

Jeder Nutzer kann sowohl Gegenstände verleihen als auch Gegenstände ausleihen.

Die Rolle ergibt sich jeweils aus der aktuellen Aktion innerhalb der Plattform.

Diese Lösung erhöht die Flexibilität der Anwendung und bildet das tatsächliche Verhalten der Zielgruppe besser ab.

---

## Regard Options

| Option | Vorteile | Nachteile |
|----------|----------|----------|
| Feste Rollen (Verleiher oder Leiher) | Einfache Umsetzung | Unflexibel für Nutzer |
| Flexible Rollen | Hohe Flexibilität, realitätsnah | Etwas komplexere Logik |

### Entscheidung

Wir wählen die Option **Flexible Rollen**, da sie die Anforderungen unserer Zielgruppe besser unterstützt und die Nutzung der Plattform vereinfacht.

# DD-02 Fokus auf Werkzeuge und technische Geräte

## Metadata

| Key | Value |
|--------|--------|
| Status | Decided |
| Datum | 18.06.2026 |
| Team | LocalLend – Gruppe 5 |
| Lead | Wendy Sharonia Lontsi Doumtsop |

---

## Problem

Zu Beginn der Produktentwicklung musste entschieden werden, welche Art von Gegenständen über die Plattform angeboten werden sollen.

Grundsätzlich könnte LocalLend für beliebige Gegenstände genutzt werden, beispielsweise Kleidung, Bücher, Haushaltsartikel oder Werkzeuge.

Ein zu breiter Fokus würde jedoch den Projektumfang erhöhen und die Benutzeroberfläche sowie die Datenstruktur komplexer machen.

---

## Decision

Wir haben uns entschieden, den Fokus der Plattform auf Werkzeuge und technische Geräte zu legen.

Beispiele hierfür sind:

- Bohrmaschinen
- Leitern
- Beamer
- Werkzeugkoffer
- Messgeräte

Durch diese Spezialisierung bleibt die Anwendung übersichtlich und konzentriert sich auf einen klar definierten Anwendungsfall.

---

## Regarded Options

| Option | Vorteile | Nachteile |
|----------|----------|----------|
| Plattform für beliebige Gegenstände | Größere Zielgruppe | Höhere Komplexität und größerer Projektumfang |
| Fokus auf Werkzeuge und technische Geräte | Klarer Anwendungsfall, einfacher umzusetzen | Kleinere Zielgruppe |

### Entscheidung

Wir wählen die Option **Fokus auf Werkzeuge und technische Geräte**, da sie einen klaren Anwendungsbereich bietet und den Umfang des Projekts auf ein für die Lehrveranstaltung geeignetes Maß begrenzt.

# DD-03 Verwendung von SQLite als Datenbank

## Metadata

| Key | Value |
|--------|--------|
| Status | Decided |
| Datum | 18.06.2026 |
| Team | LocalLend – Gruppe 5 |
| Lead | Wendy Sharonia Lontsi Doumtsop |

---

## Problem

Für die Speicherung von Nutzern, Gegenständen und Ausleihanfragen wird eine relationale Datenbank benötigt.

Zu Beginn des Projekts musste entschieden werden, welches Datenbanksystem eingesetzt werden soll.

Die Wahl der Datenbank beeinflusst die Entwicklung, Installation und Wartung der Anwendung.

---

## Decision

Wir haben uns für SQLite als Datenbanksystem entschieden.

SQLite wird direkt als Datei innerhalb des Projekts gespeichert und benötigt keinen separaten Datenbankserver.

Dadurch kann die Anwendung einfach entwickelt, getestet und zwischen den Teammitgliedern ausgetauscht werden.

---

## Regarded Options

| Option | Vorteile | Nachteile |
|----------|----------|----------|
| SQLite | Einfache Einrichtung, keine zusätzliche Serverinstallation, ideal für kleine Projekte | Weniger geeignet für sehr große Anwendungen |
| MySQL | Leistungsfähig, weit verbreitet | Zusätzliche Installation und Konfiguration erforderlich |
| PostgreSQL | Sehr leistungsfähig und flexibel | Höherer Einrichtungsaufwand |

### Entscheidung

Wir wählen SQLite, da es die Anforderungen unseres Projekts vollständig erfüllt und gleichzeitig die einfachste Lösung für Entwicklung und Zusammenarbeit im Rahmen der Lehrveranstaltung darstellt.

# DD-04 Verwendung von Flask als Webframework

## Metadata

| Key | Value |
|--------|--------|
| Status | Decided |
| Datum | 18.06.2026 |
| Team | LocalLend – Gruppe 5 |
| Lead | Tuba Celik |

---

## Problem

Für die Entwicklung der Webanwendung wird ein Framework benötigt, das die Umsetzung von Webseiten, Formularen und Anwendungslogik unterstützt.

Zu Beginn des Projekts musste entschieden werden, welches Python-Webframework eingesetzt werden soll.

Die Wahl des Frameworks beeinflusst die Struktur des Projekts, die Lernkurve für das Team und den Entwicklungsaufwand.

---

## Decision

Wir haben uns für Flask als Webframework entschieden.

Flask ist ein leichtgewichtiges Python-Framework, das sich besonders für kleinere bis mittelgroße Webanwendungen eignet.

Es bietet die notwendigen Funktionen zur Umsetzung unserer Anwendung und ermöglicht gleichzeitig eine einfache und übersichtliche Projektstruktur.

---

## Regarded Options

| Option | Vorteile | Nachteile |
|----------|----------|----------|
| Flask | Einfach zu erlernen, flexibel, für kleine Projekte geeignet | Weniger integrierte Funktionen |
| Django | Viele integrierte Funktionen, skalierbar | Höhere Komplexität und Lernaufwand |
| FastAPI | Modern und leistungsfähig | Für unser Projekt nicht erforderlich |

### Entscheidung

Wir wählen Flask, da es die Anforderungen unseres Projekts vollständig erfüllt, leicht verständlich ist und gleichzeitig den Vorgaben der Lehrveranstaltung entspricht.