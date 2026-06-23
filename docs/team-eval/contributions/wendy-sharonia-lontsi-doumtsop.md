---

title: Wendy Sharonia Lontsi Doumtsop
parent: Individual Contributions
nav_order: 1

---

{: .no_toc } 
# Wendy Sharonia Lontsi Doumtsop

<details open markdown="block"> 
<summary>Table of contents</summary>
+ ToC  
{: toc } 
{: .text-delta } 
</details>

## Meta-Goals

### Target grade

Mein Ziel für dieses Modul ist die Note **1,3 oder besser**.

### Personal goals

- Meine Kenntnisse in Datenbankmodellierung vertiefen
- Den praktischen Umgang mit Flask und SQLAlchemy erlernen
- Erfahrungen mit Git und kollaborativer Softwareentwicklung sammeln 
- Backend-Entwicklung in einem realen Projekt anwenden 
- Technische Entscheidungen dokumentieren und begründen können

---

## Eidesstattische Erklärung

**[Wendy Sharonia Lontsi Doumtsop, Matrikelnummer: 77209106458]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen. Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten – einschließlich KI-generierter Inhalte – ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit „nicht ausreichend“ führt. Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame | | --- | --- | --- | --- | | 1 | Entwicklung des Datenmodells mit den Tabellen `users`, `items` und `requests` | Das Datenmodell bildet die Grundlage der gesamten Anwendung und verbindet alle zentralen Funktionen von LocalLend. | Ich musste Beziehungen zwischen Tabellen korrekt modellieren und Foreign Keys sinnvoll einsetzen. | | 2 | Integration von SQLAlchemy und Aufbau der Datenbankanbindung | Dadurch konnten Datenbank und Anwendung sauber miteinander verbunden werden. | Die Einarbeitung in SQLAlchemy und die Anpassung an die aktuelle SQLAlchemy-Syntax waren zunächst herausfordernd. | 3 | Erstellung und Pflege der technischen Dokumentation (Data Model, ER-Diagramm, Design Decisions und Team Evaluation) | Eine gute Dokumentation macht die technische Architektur nachvollziehbar und erleichtert die Zusammenarbeit im Team. | Technische Inhalte mussten verständlich dokumentiert und die Dokumentation kontinuierlich an den aktuellen Projektstand angepasst werden. |

## Design Decisions that I led

1. [DD-01: Datenbankzugriff – Reines SQL oder SQLAlchemy](../../../evidence/design-decisions/dd-01.md)

2. [DD-02: Speicherung der Verfügbarkeit eines Gegenstands](../../../evidence/design-decisions/dd-02.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used | | --- | --- | --- | | Entwicklung des Datenmodells für LocalLend | Branch `wendy-database`, Datei `database/models.py`, Datei `evidence/data-model.md` | SQLAlchemy Documentation | | Erstellung des ER-Diagramms | Datei `evidence/ER-Diagramm.png` | dbdiagram.io | | Integration von SQLAlchemy in die Anwendung | Branch `wendy-db-integration`, Datei `database/models.py` | Flask-SQLAlchemy Documentation | | Implementierung der API-Endpunkte für Datenbankobjekte | Route `/api/items`, JSON-Ausgabe der Datenbankeinträge | Flask Documentation | | Erstellung der Design Decision DD-01 | Datei `design-decisions/dd-01.md` | SQLAlchemy Documentation | | Erstellung der Design Decision DD-02 | Datei `design-decisions/dd-02.md` | Eigene Datenmodellanalyse | | Dokumentation des Datenmodells | Datei `evidence/data-model.md` | SQLAlchemy Documentation |
| Erstellung und Aktualisierung des ER-Diagramms | Datei `evidence/ER-Diagramm.png` | dbdiagram.io |
| Erstellung der Team Evaluation Dokumentation | Dateien im Ordner `docs/team-eval/` | Kursvorlage des Dozenten |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts | | --- | --- | --- | --- | --- | | 01 | ChatGPT | Unterstützung bei der Erstellung der Projektdokumentation | Data Model, Design Decisions, Individual Contribution | Formulierungshilfe und Strukturierung technischer Inhalte | | 02 | ChatGPT | Unterstützung bei Git- und SQLAlchemy-Fragen | Datenbankintegration und Backend | Erklärung von Befehlen und Fehlermeldungen |
