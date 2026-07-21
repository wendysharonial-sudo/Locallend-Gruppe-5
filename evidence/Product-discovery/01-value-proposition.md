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

Viele Studierende und andere Mitglieder lokaler Gemeinschaften benötigen Werkzeuge, technische Geräte oder weitere Alltagsgegenstände nur für einen kurzen Zeitraum. Der Kauf solcher Gegenstände lohnt sich häufig nicht, da sie anschließend nur selten genutzt werden.

Gleichzeitig besitzen viele Menschen Gegenstände, die den Großteil der Zeit ungenutzt bleiben. Dadurch entstehen unnötige Kosten, Ressourcenverschwendung und zusätzlicher Platzbedarf.

Zudem fehlt häufig eine einfache und übersichtliche Möglichkeit, Personen aus der eigenen Umgebung zu finden, die bereit sind, Gegenstände vorübergehend zu verleihen.

## Our Solution

LocalLend ist eine Webanwendung, die das lokale Verleihen und Ausleihen von Alltagsgegenständen innerhalb einer Hochschul- und Nachbarschafts-Community ermöglicht.

Nutzer können ein Konto erstellen, eigene Gegenstände anbieten und verfügbare Angebote anderer Nutzer durchsuchen. Über die Detailansicht können sie Informationen zu einem Gegenstand einsehen und eine Ausleihanfrage stellen.

Der Besitzer eines Gegenstands kann eingehende Anfragen in einer eigenen Übersicht prüfen, akzeptieren oder ablehnen. Wird eine Anfrage angenommen, ändert sich der Status des Gegenstands automatisch von „verfügbar“ zu „ausgeliehen“. Nach der Rückgabe wird der Gegenstand wieder für andere Nutzer verfügbar.

LocalLend setzt damit die zentrale Idee „Teilen statt Kaufen“ um. Vorhandene Ressourcen werden innerhalb einer lokalen Gemeinschaft besser genutzt, unnötige Käufe vermieden und nachhaltiger Konsum erleichtert.

## Target User(s)

### Primäre Zielgruppe

- Studierende
- Bewohner von Wohngemeinschaften
- Mitglieder lokaler Hochschul- und Nachbarschafts-Communitys
- Personen, die Gegenstände nur kurzfristig benötigen
- Personen, die selten genutzte Gegenstände verleihen möchten

### Persona 1 – Lisa (22)

Lisa studiert Wirtschaftsinformatik und benötigt für einen Umzug kurzfristig eine Bohrmaschine. Da sie das Werkzeug voraussichtlich nur einmal verwenden wird, möchte sie keine neue Bohrmaschine kaufen.

Über LocalLend kann sie nach einer verfügbaren Bohrmaschine in ihrer lokalen Community suchen und eine Ausleihanfrage stellen.

### Persona 2 – Max (28)

Max besitzt verschiedene Werkzeuge und technische Geräte, die er nur selten nutzt. Er möchte diese anderen Personen aus seiner Umgebung zur Verfügung stellen, anstatt sie ungenutzt aufzubewahren.

Über LocalLend kann er seine Gegenstände anbieten und eingehende Ausleihanfragen verwalten.

## Happy Path

1. Ein Nutzer registriert sich bei LocalLend und erstellt ein Konto.
2. Der Nutzer meldet sich an.
3. Der Nutzer bietet einen neuen Gegenstand an.
4. Ein anderer Nutzer registriert sich oder meldet sich mit einem bestehenden Konto an.
5. Der zweite Nutzer durchsucht die verfügbaren Gegenstände.
6. Der Nutzer verwendet bei Bedarf die Suchfunktion, um ein passendes Angebot zu finden.
7. Der Nutzer öffnet die Detailansicht eines Gegenstands.
8. Der Nutzer sendet eine Ausleihanfrage.
9. Der Besitzer sieht die Anfrage in seiner Anfragenübersicht.
10. Der Besitzer akzeptiert oder lehnt die Anfrage.
11. Bei einer Annahme ändert sich der Status des Gegenstands von „verfügbar“ zu „ausgeliehen“.
12. Die akzeptierte Ausleihe wird im Profil des ausleihenden Nutzers angezeigt.
13. Nach der Nutzung bestätigt der ausleihende Nutzer die Rückgabe.
14. Die Ausleihe wird als abgeschlossen dargestellt und der Gegenstand wird wieder als „verfügbar“ angezeigt.

Dieser Ablauf bildet die zentrale Interaktion von LocalLend ab: Ein vorhandenes lokales Angebot trifft auf eine konkrete Nachfrage und wird über einen nachvollziehbaren digitalen Ausleihprozess vermittelt.

## Improvements Since the Oral Examination

Seit der mündlichen Prüfung wurde die Anwendung gezielt weiterentwickelt und verfeinert:

- Der vollständige Anfrageprozess wurde mit den Benutzerkonten und der Datenbank verbunden.
- Besitzer können eingehende Ausleihanfragen akzeptieren oder ablehnen.
- Bei einer angenommenen Anfrage wird der Gegenstand automatisch als „ausgeliehen“ markiert.
- Weitere offene Anfragen für denselben Gegenstand werden entsprechend berücksichtigt.
- Ausleihende Nutzer können die Rückgabe eines Gegenstands bestätigen.
- Nach der Rückgabe wird der Gegenstand automatisch wieder als „verfügbar“ angezeigt.
- Aktive und abgeschlossene Ausleihen werden im Profil getrennt dargestellt.
- Die Darstellung der eigenen Angebote und eingehenden Anfragen wurde verbessert.
- Die Suchfunktion und die Übersicht verfügbarer Gegenstände wurden überarbeitet.
- Beim Erstellen eines Gegenstands stehen zusätzliche Kategorien zur Verfügung.
- Die Navigation der Startseite wurde an den Anmeldestatus des Nutzers angepasst.

## Target Scope

Die Anwendung umfasst die folgenden Kernfunktionen:

- Benutzerregistrierung und Anmeldung
- Sicheres Speichern von Passwörtern
- Session-basierte Erkennung angemeldeter Nutzer
- Abmeldung
- Darstellung eines persönlichen Benutzerprofils
- Erstellen und Anzeigen eigener Gegenstände
- Kategorisierung von Gegenständen
- Durchsuchen verfügbarer Gegenstände
- Suche nach Gegenständen
- Detailansicht einzelner Gegenstände
- Erstellen von Ausleihanfragen
- Anzeigen eingehender und ausgehender Anfragen
- Akzeptieren und Ablehnen von Anfragen
- Automatischer Statuswechsel zwischen „verfügbar“ und „ausgeliehen“
- Bestätigung der Rückgabe
- Darstellung aktiver und abgeschlossener Ausleihen
- Datenbereitstellung über JSON-API-Endpunkte

### Umgesetzte Benutzeroberflächen

- Startseite
- Login-Seite
- Registrierungsseite
- Übersicht verfügbarer Gegenstände
- Suchfunktion für Gegenstände
- Detailansicht eines Gegenstands
- Formular zum Erstellen eines Gegenstands
- Profilübersicht
- Übersicht eingehender Ausleihanfragen
- Übersicht aktiver und abgeschlossener Ausleihen




