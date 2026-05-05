# LocalLend – Gruppe 5

## 1. Team Composition

**Team Name:** Gruppe 5 – LocalLend  

**Repository Access:**  
Unser GitHub-Repository ist auf "public" gestellt und die Dokumentation ist über GitHub Pages erreichbar.

**Git Repository:**  
https://github.com/Nejy190501/Locallend_Gruppe-5

---

## Contributors & Meta-Goals

| Contributor | Zielnote | Persönliches Ziel | Geplanter Beitrag |
|---|---|---|---|
| Tuba Celik | 1.7 | Verstehen, wie man mit Flask eine strukturierte Webanwendung entwickelt und Backend-Logik sauber implementiert | Entwicklung der Flask-Routen und Umsetzung der Anfragen-Logik |
| Jean Yves Nkwane | 1.0 | Verbesserung der Fähigkeiten in HTML, CSS und der Arbeit mit Jinja2 zur Gestaltung von Benutzeroberflächen | Gestaltung und Umsetzung der Benutzeroberfläche mit Jinja2-Templates |
| Wendy Sharonia Lontsi Doumtsop | 1.7 | Erlernen von relationalem Datenbankdesign und der Integration von SQLite in Webanwendungen | Modellierung der Datenbankstruktur für User, Items und Requests |
| Maryam Joumma | 1.7 | Verbesserung von Git-Workflows und strukturierter Projektorganisation in Teamprojekten | Verwaltung des Repositories, Dokumentation und GitHub Pages |

---

## 2. Value Proposition

LocalLend ist eine zweiseitige Plattform (Two-Sided Platform) für das Verleihen und Ausleihen von Werkzeugen und technischen Geräten in der Nachbarschaft und auf dem Campus.

### Zielgruppe

Unsere Zielgruppe sind Studierende und Anwohner, die entweder selten genutzte Gegenstände besitzen oder solche für kurze Zeit benötigen.

### Problem

Viele Menschen benötigen teure Werkzeuge oder technische Geräte (z. B. Bohrmaschinen, Beamer oder Leitern) nur für kurze Zeit. Ein Kauf lohnt sich oft nicht und ist insbesondere für Studierende zu teuer.

Gleichzeitig besitzen viele Menschen solche Gegenstände bereits, nutzen sie jedoch nur selten. Diese bleiben die meiste Zeit ungenutzt.

### Lösung

LocalLend ist eine Webanwendung, die es ermöglicht, Gegenstände lokal und unkompliziert zu verleihen und auszuleihen.

Verleiher können ihre Gegenstände einstellen. Leiher können verfügbare Gegenstände durchsuchen, Details einsehen und Anfragen stellen.

### Zwei Seiten der Plattform

| Seite | Beschreibung |
|---|---|
| Verleiher | Nutzer, die Gegenstände besitzen und verleihen möchten |
| Leiher | Nutzer, die Gegenstände für kurze Zeit benötigen |

### Nutzen für Verleiher

- Bessere Nutzung selten verwendeter Gegenstände  
- Unterstützung anderer Personen in der Umgebung  
- Beitrag zur Reduzierung von Verschwendung  

### Nutzen für Leiher

- Kostenersparnis durch Ausleihen statt Kaufen  
- Schneller und lokaler Zugriff auf benötigte Gegenstände  
- Keine unnötigen Anschaffungen für einmalige Nutzung  

---

## 3. Target Scope

Zur Darstellung des Funktionsumfangs unserer Web-App haben wir die wichtigsten Screens als UI-Scribbles entworfen.

Ziel ist es, die Struktur und den Ablauf der Anwendung zu visualisieren, nicht ein fertiges Design zu zeigen.

---

## UI Scribbles

### Scribble 1: Startseite

Die Startseite stellt LocalLend vor und bietet einen Einstieg in die App.  
Nutzer können direkt mit dem Browsen beginnen oder einen Gegenstand einstellen.

<p align="center">
  <img src="scribbles/landing.jpg" width="500">
</p>

---

### Scribble 2: Gegenstände durchsuchen

Hier können Nutzer alle verfügbaren Gegenstände einsehen.  
Jeder Eintrag enthält grundlegende Informationen sowie einen Button zur Detailansicht.

<p align="center">
  <img src="scribbles/browse.jpg" width="500">
</p>

---

### Scribble 3: Detailansicht

Diese Seite zeigt detaillierte Informationen zu einem Gegenstand, z. B. Beschreibung, Verfügbarkeit und Kaution.  
Von hier aus kann eine Ausleihanfrage gestellt werden.

<p align="center">
  <img src="scribbles/detail.jpg" width="500">
</p>

---

### Scribble 4: Gegenstand erstellen

Verleiher können hier neue Gegenstände hinzufügen.  
Das Formular enthält Angaben wie Titel, Kategorie, Beschreibung und Preis/Kaution.

<p align="center">
  <img src="scribbles/create.jpg" width="500">
</p>

---

### Scribble 5: Login / Registrierung

Nutzer können sich registrieren oder anmelden.  
Bei der Registrierung wird die Rolle (Verleiher oder Leiher) gewählt.

<p align="center">
  <img src="scribbles/login.jpg" width="500">
</p>

---

### Scribble 6: Anfragen verwalten

Verleiher sehen hier eingehende Anfragen und können diese annehmen oder ablehnen.  
Dies bildet die zentrale Interaktion der Plattform.

<p align="center">
  <img src="scribbles/requests.jpg" width="500">
</p>

---

## Happy Path

1. Ein Nutzer registriert sich und wählt die Rolle „Verleiher“.  
2. Der Verleiher loggt sich ein und erstellt einen neuen Gegenstand.  
3. Ein zweiter Nutzer registriert sich als „Leiher“ und loggt sich ein.  
4. Der Leiher durchsucht die verfügbaren Gegenstände.  
5. Der Leiher öffnet die Detailansicht eines Gegenstands.  
6. Der Leiher stellt eine Anfrage.  
7. Der Verleiher sieht die Anfrage in seinem Dashboard.  
8. Der Verleiher akzeptiert die Anfrage.  
9. Der Status des Gegenstands ändert sich von „verfügbar“ zu „ausgeliehen“.  

Dieser Ablauf zeigt die zentrale Interaktion zwischen beiden Seiten der Plattform.

---

## AI Directory

Wir dokumentieren unseren Einsatz von generativer KI transparent:

**Verwendete Tools:** ChatGPT / Gemini (Chat-Interface)  

**Art der Nutzung:**  
Unterstützung beim Brainstorming, Strukturierung der Value Proposition sowie beim Erstellen der Markdown-Dokumentation.

**Verantwortung:**  
Alle Inhalte wurden von uns überprüft und angepasst. Es wurden keine Agentic-AI-Tools verwendet, die eigenständig Code oder Repository-Strukturen erzeugen.
