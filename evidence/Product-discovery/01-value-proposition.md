---
title: Value Proposition
nav_order: 5
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>

+ ToC

{: toc }

{: .text-delta }

</details>

## The Problem

Viele Studierende und Anwohner benötigen Werkzeuge oder technische Geräte häufig nur für einen kurzen Zeitraum. Der Kauf solcher Gegenstände lohnt sich oft nicht, da sie anschließend nur selten genutzt werden. Gleichzeitig besitzen viele Menschen Geräte, die den Großteil der Zeit ungenutzt bleiben.

Dadurch entstehen unnötige Kosten, Ressourcenverschwendung und zusätzlicher Platzbedarf. Außerdem fehlt häufig eine einfache Möglichkeit, Personen aus der eigenen Umgebung zu finden, die bereit sind, Gegenstände zu verleihen.

## Our Solution

LocalLend ist eine Webanwendung, die das Verleihen und Ausleihen von Werkzeugen und technischen Geräten innerhalb einer lokalen Gemeinschaft ermöglicht.

Nutzer können eigene Gegenstände anbieten, verfügbare Gegenstände durchsuchen, nach bestimmten Gegenständen suchen und Ausleihanfragen stellen. Besitzer können eingehende Anfragen verwalten, akzeptieren oder ablehnen. Nach erfolgreicher Rückgabe wird der Gegenstand automatisch wieder als verfügbar gekennzeichnet.

Die Plattform unterstützt damit nachhaltigen Konsum und erleichtert die gemeinsame Nutzung vorhandener Ressourcen.

## Target User(s)

### Primäre Zielgruppe

- Studierende
- Bewohner von Wohngemeinschaften
- Anwohner lokaler Gemeinschaften

### Persona 1 – Lisa (22)

Lisa studiert Wirtschaftsinformatik und benötigt für einen Umzug kurzfristig eine Bohrmaschine. Da sie das Werkzeug nur einmal verwenden wird, möchte sie keine neue Bohrmaschine kaufen.

### Persona 2 – Max (28)

Max besitzt verschiedene Werkzeuge und technische Geräte, die er nur selten nutzt. Er möchte diese anderen Personen aus seiner Umgebung zur Verfügung stellen, anstatt sie ungenutzt aufzubewahren.

## Happy Path

1. Ein Nutzer registriert sich und erstellt ein Konto.
2. Der Nutzer meldet sich an.
3. Der Nutzer bietet einen Gegenstand zum Verleihen an.
4. Ein anderer Nutzer durchsucht oder durchsucht mithilfe der Suchfunktion die verfügbaren Gegenstände.
5. Der Nutzer öffnet die Detailansicht eines Gegenstands.
6. Der Nutzer stellt eine Ausleihanfrage.
7. Der Besitzer sieht die Anfrage in seiner Anfragenübersicht.
8. Der Besitzer akzeptiert oder lehnt die Anfrage.
9. Wird die Anfrage akzeptiert, ändert sich der Status des Gegenstands automatisch von **„verfügbar“** zu **„ausgeliehen“**.
10. Nach der Nutzung bestätigt der ausleihende Nutzer die Rückgabe.
11. Der Gegenstand wird wieder als **„verfügbar“** angezeigt.

## Improvements Since the First Submission

Seit der First Submission wurde die Anwendung funktional erweitert und verbessert:

- Vollständiger Ausleih- und Rückgabeprozess
- Akzeptieren und Ablehnen von Ausleihanfragen
- Automatische Statusänderung von Gegenständen
- Suchfunktion für Gegenstände
- Erweiterte Gegenstandskategorien
- Verbesserte Profilübersicht
- Trennung zwischen aktiven und abgeschlossenen Ausleihen
- Verbesserte Navigation abhängig vom Login-Status

## Target Scope

Die Anwendung umfasst folgende Kernfunktionen:

- Benutzerregistrierung und Anmeldung
- Benutzerprofil
- Erstellen eigener Gegenstände
- Kategorisierung von Gegenständen
- Durchsuchen verfügbarer Gegenstände
- Suchfunktion
- Detailansicht eines Gegenstands
- Erstellen von Ausleihanfragen
- Akzeptieren und Ablehnen von Anfragen
- Verwaltung des Anfrage-Status
- Rückgabe eines Gegenstands
- JSON-API-Endpunkte

### Umgesetzte Benutzeroberflächen

- Startseite
- Login-Seite
- Registrierungsseite
- Profilseite
- Übersicht verfügbarer Gegenstände
- Suchfunktion
- Detailansicht eines Gegenstands
- Formular zum Erstellen eines Gegenstands
- Übersicht eingehender Anfragen
- Übersicht aktiver und abgeschlossener Ausleihen
