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

| \# | My contribution | Why I am proud of it | Which challenge I overcame |

| :-- | :-- | :-- | :-- |

| 1 | Implementierung von Registrierung, Login, Logout und Session-Verwaltung im Backend | Dieser Beitrag ist zentral, weil LocalLend ohne Benutzerverwaltung keinen sinnvollen Nutzerfluss hat. Durch Registrierung und Login können Nutzerkonten erstellt und angemeldete Nutzer über Sessions erkannt werden. | Ich musste verstehen, wie Flask GET- und POST-Anfragen verarbeitet, wie `request.form` funktioniert, wie Passwörter sicher gehasht werden und wie Sessions mit `session["user_id"]` und `session.clear()` verwaltet werden. |

| 2 | Verbindung der Flask-Routen mit Datenbank und Templates, insbesondere für Profil, Browse, Items und Add-Item | Dadurch wurden Yves' HTML-Seiten und Wendys Datenbankmodell mit meinem Backend verbunden. Die App zeigt nicht nur statische Seiten, sondern arbeitet mit echten Datenbankobjekten. | Ich musste unterschiedliche Feldnamen zwischen HTML, Datenbankmodell und Backend zusammenführen, zum Beispiel `name` aus dem Formular mit `title` im Item-Modell, sowie alte Dummy-Listen durch Datenbankabfragen ersetzen. |

| 3 | Integration der Teamänderungen über Git und Bereinigung von Merge-Konflikten | Ich bin darauf stolz, weil ich nicht nur einzelne Funktionen gebaut habe, sondern aktiv geholfen habe, die Arbeiten von Yves, Wendy und Maryam in einen lauffähigen gemeinsamen Stand zu bringen. | Ich musste mehrere Git-Probleme lösen, darunter Pull/Rebase-Probleme, Konflikte in `.gitignore` und `app.py`, sowie die saubere Zusammenführung von Frontend-, Datenbank- und API-Änderungen. |

## Design Decisions that I led

1. [DD-03: User Authentication with Flask Sessions](../../../evidence/design-decisions/dd-03.md)

2. [DD-04: Password Hashing for Secure User Accounts](../../../evidence/design-decisions/dd-04.md)

---
## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Implementierung von Registrierung und Login im Backend | app.py, Commit „Add login and register backend“ | Flask Documentation, Werkzeug Security Documentation |
| Implementierung von Logout und Session-Verwaltung | app.py, Verwendung von `session["user_id"]`, `session["user_name"]` und `session.clear()` | Flask Documentation |
| Integration des User-Modells mit dem Backend | app.py, database/models.py | SQLAlchemy Documentation |
| Implementierung der Profilseite und Profil-Route | app.py, profile.html | Flask Documentation |
| Implementierung der Add-Item-Funktion | app.py, add_item.html | Flask Documentation, SQLAlchemy Documentation |
| Verbindung der Browse-Seite mit der Datenbank | app.py, browse.html | SQLAlchemy Documentation |
| Umstellung auf SQLAlchemy-2.0-Syntax (`db.select`, `db.session.execute`, `db.session.get`) | app.py | SQLAlchemy Documentation |
| Implementierung der Item-Detailseite und Fehlerbehandlung | app.py, item_detail.html | Flask Documentation |
| Unterstützung bei der JSON-API-Integration | app.py | Flask Documentation |
| Integration von Änderungen anderer Teammitglieder | Branch `tuba-backend`, Merge von `yves-frontend` und `wendy-db-integration` | Git Documentation |
| Lösung von Merge-Konflikten in app.py und .gitignore | Git-Historie, Branch `tuba-backend` | Git Documentation |
| Dokumentation von Designentscheidungen und individuellem Beitrag | design-decision-login.md, design-decision-passwords.md, individual-contribution-tuba.md | Projektvorlage |
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









