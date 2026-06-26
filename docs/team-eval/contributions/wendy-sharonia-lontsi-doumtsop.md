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

Mein persönliches Ziel in diesem Modul ist es, das Projekt erfolgreich abzuschließen und eine sehr gute Leistung zu erzielen. Gleichzeitig möchte ich meine Kenntnisse in der Webentwicklung und Datenbankmodellierung erweitern sowie den praktischen Umgang mit Flask, SQLAlchemy und Git vertiefen. Außerdem ist mir eine gute und zuverlässige Zusammenarbeit im Team wichtig, damit wir gemeinsam ein erfolgreiches Projektergebnis erreichen und voneinander lernen können.
---

## Eidesstattische Erklärung

**[Wendy Sharonia Lontsi Doumtsop, Matrikelnummer: 77209106458]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen. Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten – einschließlich KI-generierter Inhalte – ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit „nicht ausreichend“ führt. Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions


| # | My contribution | Why I am proud of it | Which challenge I overcame |
| --- | --- | --- | --- |
| 1 | Entwicklung des Datenmodells mit den Tabellen `users`, `items` und `requests` | Besonders stolz bin ich darauf, die Grundlage für die Datenverwaltung von LocalLend geschaffen zu haben. Das Datenmodell verbindet die wichtigsten Funktionen der Anwendung und war entscheidend für die spätere Umsetzung des Backends. | Ich musste Beziehungen zwischen Tabellen korrekt modellieren und Foreign Keys sinnvoll einsetzen. |
| 2 | Integration von SQLAlchemy und Aufbau der Datenbankanbindung | Durch diese Aufgabe konnte ich mich intensiv in SQLAlchemy einarbeiten und erstmals eine vollständige Datenbankanbindung selbst umsetzen. Es motiviert mich, dass die Anwendung dadurch Daten dauerhaft speichern und verwalten kann. | Die Einarbeitung in SQLAlchemy und die Anpassung an die aktuelle SQLAlchemy-Syntax waren zunächst herausfordernd. |
| 3 | Erstellung und Pflege der technischen Dokumentation (Data Model, ER-Diagramm, Design Decisions und Team Evaluation) | Mir war wichtig, die technischen Entscheidungen unseres Projekts nachvollziehbar zu dokumentieren. Eine gute Dokumentation erleichtert nicht nur die Zusammenarbeit im Team, sondern hilft auch anderen, die Architektur und Entwicklungsschritte schnell zu verstehen. | Technische Inhalte mussten verständlich dokumentiert und die Dokumentation kontinuierlich an den aktuellen Projektstand angepasst werden. |

## Design Decisions that I led

1. [DD-01: Datenbankzugriff – Reines SQL oder SQLAlchemy](../../../evidence/design-decisions/dd-01.md)

2. [DD-02: Speicherung der Verfügbarkeit eines Gegenstands](../../../evidence/design-decisions/dd-02.md)

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| --- | --- | --- |
| Entwicklung des Datenmodells für LocalLend | [Git Commit](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/0d61d0f94e658cc140d818ede2d4f6643c1dd650) | SQLAlchemy Documentation |
| Erstellung des ER-Diagramms | [Git Commit 1](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/a20e8c48dad5a1e52ee26fa3f7bf135bfaa07105), [Git Commit 2 ](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/f12b24572b0e0310abb08bc5112e370ebac9bf10) | dbdiagram.io |
| Integration von SQLAlchemy in die Anwendung | [Git Commit 1 ](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/89fba40b157790d3880a84386cbf796e5b1a395c), [ Git Commit 2 ](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/becb6c5439b315b13383335d674522a20b0175a8) | Flask-SQLAlchemy Documentation |
| Implementierung der API-Endpunkte | [Git Commit](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/269c33f5b2e36f049d7bb8a56164a5f82c164647) | Flask Documentation |
| Erstellung der Design Decision DD-01 | [Git Commit](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/db4966985e0462777c9f12ba61f1a478131275dc) | SQLAlchemy Documentation |
| Erstellung der Design Decision DD-02 | [Git Commit](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/db4966985e0462777c9f12ba61f1a478131275dc) | Eigene Datenmodellanalyse |
| Dokumentation des Datenmodells | [Git Commit](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/9c645e8e827920d0f6a9aceccb40d931bb9b403b) | SQLAlchemy Documentation |
| Erstellung der Team Evaluation Dokumentation | [Git Commit](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/db4966985e0462777c9f12ba61f1a478131275dc) | Kursvorlage des Dozenten |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| --- | --- | --- | --- | --- |
| 01 | ChatGPT | Unterstützung bei der Erstellung der Projektdokumentation | Data Model, Design Decisions, Individual Contribution | Formulierungshilfe und Strukturierung technischer Inhalte |
| 02 | ChatGPT | Unterstützung bei Git- und SQLAlchemy-Fragen | Datenbankintegration und Backend | Erklärung von Befehlen und Fehlermeldungen |
