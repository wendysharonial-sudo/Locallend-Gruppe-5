API-Erklärung

Verantwortlich

Maryam – API & Request-System

Zweck

Dieses Dokument erklärt die Funktionsweise der LocalLend-API, die Verwendung von JSON sowie den Ablauf des Anfrage- und Verleihsystems.

⸻

Was ist eine API?

API steht für Application Programming Interface (Programmierschnittstelle).

Eine API ermöglicht die Kommunikation zwischen verschiedenen Teilen einer Anwendung.

Im Projekt LocalLend stellt die API Informationen über Gegenstände und Ausleihanfragen bereit.

Anstatt eine normale Webseite zurückzugeben, liefert die API strukturierte Daten im JSON-Format.

⸻

Was ist JSON?

JSON steht für JavaScript Object Notation.

JSON ist ein standardisiertes Datenformat, das für den Datenaustausch zwischen Frontend und Backend verwendet wird.

Beispiel:

{
  "id": 1,
  "name": "Bohrmaschine",
  "status": "verfügbar"
}

Dieses Objekt enthält Informationen über einen Gegenstand.

⸻

Frontend und Backend

Das Frontend ist der Teil der Anwendung, mit dem die Nutzer direkt interagieren.

Beispiele:

* Schaltflächen
* Formulare
* Webseiten
* Navigation

Das Backend arbeitet im Hintergrund und verarbeitet die Anwendungslogik.

Beispiele:

* Flask-Anwendung
* API-Endpunkte
* Datenverarbeitung
* Verwaltung von Anfragen

Das Frontend sendet Anfragen an das Backend.

Das Backend verarbeitet diese Anfragen und liefert die entsprechenden Daten als JSON-Antwort zurück.

⸻

Datenfluss im System

Der Datenfluss innerhalb von LocalLend erfolgt wie folgt:

Benutzer
↓
Frontend
↓
API-Endpunkt
↓
Flask-Backend
↓
JSON-Antwort
↓
Anzeige im Frontend

Beispiel:

1. Ein Nutzer öffnet die LocalLend-Webseite.
2. Das Frontend sendet eine Anfrage an einen API-Endpunkt.
3. Flask empfängt die Anfrage.
4. Die entsprechende Funktion wird ausgeführt.
5. Die Daten werden in JSON umgewandelt.
6. Die JSON-Antwort wird zurückgesendet.
7. Das Frontend zeigt die Informationen an.

⸻

Die Funktion jsonify()

Die Flask-Funktion jsonify() wandelt Python-Daten in eine JSON-Antwort um.

Beispiel:

return jsonify({
    "success": True,
    "message": "Gegenstände erfolgreich geladen",
    "data": items
})

Die Antwort enthält:

* success
* message
* data

Dadurch entsteht eine standardisierte und leicht verarbeitbare API-Antwort.

⸻

Ablauf des Anfrage-Systems

Der Anfrageprozess beschreibt die Verarbeitung von Ausleihanfragen innerhalb von LocalLend.

Schritt 1

Ein Nutzer erstellt eine Ausleihanfrage.

Status:

pending

Schritt 2

Der Verleiher überprüft die Anfrage.

Schritt 3

Der Verleiher akzeptiert die Anfrage.

Status:

accepted

Schritt 4

Der Verleiher kann die Anfrage auch ablehnen.

Status:

rejected

Schritt 5

Eine Anfrage kann gelöscht werden.

Status:

deleted

⸻

Verwendete Statuswerte

Status	Beschreibung
pending	Anfrage wurde erstellt und wartet auf eine Entscheidung
accepted	Anfrage wurde akzeptiert
rejected	Anfrage wurde abgelehnt
deleted	Anfrage wurde gelöscht
available	Gegenstand ist verfügbar

⸻

Implementierte API-Endpunkte

Endpunkt	Zweck
/api/items	Gibt verfügbare Gegenstände zurück
/api/requests	Gibt alle Ausleihanfragen zurück
/api/create_request	Erstellt eine neue Anfrage
/api/accept_request	Akzeptiert eine Anfrage
/api/reject_request	Lehnt eine Anfrage ab
/api/delete_request	Löscht eine Anfrage
/api/status	Liefert Informationen über die API

⸻

Verwendete Technologien

* Python
* Flask
* JSON
* Git
* GitHub

⸻

Mein Beitrag

Im Bereich API & Request-System habe ich folgende Aufgaben übernommen:

* Entwicklung der API-Endpunkte
* Bereitstellung von JSON-Antworten
* Implementierung der Anfragenverwaltung
* Implementierung der Anfrageerstellung
* Implementierung der Annahme von Anfragen
* Implementierung der Ablehnung von Anfragen
* Implementierung der Löschung von Anfragen
* Implementierung der Statusverwaltung
* Testen der API-Endpunkte
* Erstellung der API-Dokumentation
* Dokumentation des Anfrageprozesses
* Erklärung der API-Architektur und der JSON-Nutzung

⸻

Fazit

Die LocalLend-API stellt strukturierte JSON-Daten über mehrere Endpunkte bereit.

Sie verwaltet Gegenstände, Ausleihanfragen und Statuswerte und ermöglicht die Kommunikation zwischen Frontend und Backend.

Die Implementierung demonstriert die Nutzung von Flask und JSON zur Entwicklung einer einfachen und übersichtlichen REST-ähnlichen API für das LocalLend-System.