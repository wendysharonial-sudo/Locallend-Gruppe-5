---

title: Tuba Celik

parent: Individual Contributions

nav_order: 1

---

{: .no_toc }

# Tuba Celik

<details open markdown="block">

<summary>Inhaltsverzeichnis</summary>

+ ToC

{: toc }

{: .text-delta }

</details>

## Meta-Ziele

### Zielnote

1,0

### Persönliche Ziele

- Praktische Erfahrungen in der Webentwicklung mit Flask sammeln.

- Backend-Funktionalitäten für eine echte Webanwendung selbstständig implementieren.

- Das Zusammenspiel zwischen Flask-Routen, HTML-Templates, Sessions und Datenbank besser verstehen.

- Sicherer im Umgang mit Git, Branches, Commits, Pulls und Merge-Konflikten werden.

- Einen nachvollziehbaren Beitrag zum Happy Path und zur technischen Funktionsfähigkeit von LocalLend leisten.

---

## Eidesstattliche Erklärung

**[Tuba Celik, Matrikelnr.: 77206594559]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions


| # | My contribution | Why I am proud of it | Which challenge I overcame |
| --- | --- | --- | --- |
| 1 | Implementierung von Registrierung, Login, Logout und Session-Verwaltung im Backend | Dieser Beitrag ist zentral, weil LocalLend ohne Benutzerverwaltung keinen sinnvollen Nutzerfluss hätte. Durch Registrierung und Login können Nutzerkonten erstellt und angemeldete Nutzer über Sessions erkannt werden. | Ich musste verstehen, wie Flask GET- und POST-Anfragen verarbeitet, wie `request.form` funktioniert, wie Passwörter sicher gehasht werden und wie Sessions mit `session["user_id"]` und `session.clear()` verwaltet werden. |
| 2 | Verbindung der Flask-Routen mit Datenbank und Templates, insbesondere für Profil, Browse, Items und Add-Item | Dadurch wurden Yves' HTML-Seiten und Wendys Datenbankmodell mit meinem Backend verbunden. Die App zeigt nicht nur statische Seiten, sondern arbeitet mit echten Datenbankobjekten. | Ich musste unterschiedliche Feldnamen zwischen HTML, Datenbankmodell und Backend zusammenführen, zum Beispiel `name` aus dem Formular mit `title` im Item-Modell, sowie alte Dummy-Listen durch Datenbankabfragen ersetzen. |
| 3 | Integration der Teamänderungen über Git und Bereinigung von Merge-Konflikten | Ich bin darauf stolz, weil ich nicht nur einzelne Funktionen entwickelt habe, sondern aktiv geholfen habe, die Arbeiten von Yves, Wendy und Maryam in einen gemeinsamen, lauffähigen Stand zu bringen. | Ich musste mehrere Git-Probleme lösen, darunter Pull-/Rebase-Probleme, Konflikte in `.gitignore` und `app.py` sowie die saubere Zusammenführung von Frontend-, Datenbank- und API-Änderungen. |

## Design Decisions that I led

1. [DD-03: User Authentication with Flask Sessions](../../../evidence/design-decisions/dd-03.md)

2. [DD-04: Password Hashing for Secure User Accounts](../../../evidence/design-decisions/dd-04.md)

---
## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| --- | --- | --- |
| Implementierung von Registrierung und Login im Flask-Backend | [Git Commit – Add login and register backend](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/515b72f) | Flask Documentation, Werkzeug Security Documentation |
| Umsetzung und Dokumentation der Session-basierten Benutzeranmeldung | [Git Commit – Document login session design decision](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/4cb56dc) | Flask Documentation – Sessions |
| Umsetzung und Dokumentation des sicheren Passwort-Hashings | [Git Commit – Document password hashing decision](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/2b463e6) | Werkzeug Security Documentation |
| Verbindung der Browse-Seite mit den Gegenständen aus der Datenbank | [Git Commit – Connect browse page with database items](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/d814c40) | Flask-SQLAlchemy Documentation |
| Fertigstellung der Backend-Integration und der API-Routen | [Git Commit 1 – Finalize backend integration and API routes](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/f430791), [Git Commit 2 – Improve API endpoints and database integration](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/9b9d418) | Flask Documentation, Flask-SQLAlchemy Documentation |
| Verbindung der Profilseite mit Benutzer-, Gegenstands- und Anfragedaten | [Git Commit 1 – Connect profile page with database data](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/2c2d708), [Git Commit 2 – Fix item ownership and profile data handling](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/ee8e038) | Flask Documentation, SQLAlchemy Documentation |
| Verbesserung der Registrierung, Browse-Seite und Gegenstandsdetailansicht | [Git Commit – Improve item detail, browse page and register feedback](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/94528c8) | Flask Documentation, Jinja Documentation |
| Fertigstellung des Anfrage-Workflows mit Nutzerinteraktionen | [Git Commit – Finalize request workflow and user interactions](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/a20cf9c) | Flask Documentation, SQLAlchemy Documentation |
| Korrektur der eingehenden Besitzeranfragen im Profil | [Git Commit – Fix owner requests in profile](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/2e8e71e) | Flask Documentation, Jinja Documentation |
| Vervollständigung des Ausleih- und Rückgabeprozesses einschließlich automatischer Statusänderungen | [Git Commit – Complete borrowing and return workflow](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/669b585) | Flask Documentation, SQLAlchemy Documentation |
| Erweiterung der Gegenstandskategorien und Verbesserung der Browse-Oberfläche | [Git Commit – Improve item categories and browse interface](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/090abe7) | Jinja Documentation |
| Anpassung der Startseiten-Navigation an den Login-Status | [Git Commit – Improve landing page navigation](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/af78dde) | Flask Documentation – Sessions, Jinja Documentation |
| Integration der Frontend-, API- und Datenbankänderungen der Teammitglieder | [Frontend-Integration](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/e946f59), [API-Integration](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/f6464d1), [Datenbank-Integration](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/31425c8) | Git Documentation |
| Dokumentation des individuellen Beitrags und technischer Designentscheidungen | [Git Commit 1 – Add individual contribution documentation](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/cab7e6a), [Git Commit 2 – Improve individual contribution documentation](https://github.com/wendysharonial-sudo/Locallend-Gruppe-5/commit/f2c9918) | Kursvorlage des Dozenten |
---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | ChatGPT | Unterstützung bei Registrierung, Login und Session-Verwaltung | app.py | Erklärung und Implementierung von Flask-Routen und Sessions |
| 02 | ChatGPT | Unterstützung bei Passwort-Hashing | app.py | Verwendung von `generate_password_hash()` und `check_password_hash()` |
| 03 | ChatGPT | Unterstützung bei SQLAlchemy und Datenbankabfragen | app.py, database/models.py | Umstellung auf SQLAlchemy-2.0-Syntax |
| 04 | ChatGPT | Unterstützung beim Debugging und Verbinden von Templates mit dem Backend | app.py, HTML-Dateien | Fehleranalyse und Integration von Datenbank und Frontend |
| 05 | ChatGPT | Unterstützung bei Git und Merge-Konflikten | Git-Workflow | Hilfe bei Branches, Pulls und Konfliktlösung |
| 06 | ChatGPT | Unterstützung bei der Projektdokumentation | Individual Contribution, Design Decisions | Strukturierung und Formulierung der Dokumentation |









