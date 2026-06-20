Product Discovery - LocalLend

Design Challenge

Wie können wir Studierenden und Anwohnern helfen, einfachen und kostengünstigen Zugang zu Werkzeugen und technischen Geräten zu erhalten, unter Berücksichtigung begrenzter Budgets, seltener Nutzung solcher Gegenstände und des Wunsches nach nachhaltiger Ressourcennutzung?

Viele Studierende und Anwohner benötigen Werkzeuge oder technische Geräte nur für einen kurzen Zeitraum. Beispiele sind Bohrmaschinen für Reparaturen, Leitern für Renovierungsarbeiten oder Beamer für Präsentationen.

Der Kauf solcher Gegenstände lohnt sich häufig nicht, insbesondere wenn sie nur selten genutzt werden. Gleichzeitig besitzen viele Menschen genau diese Gegenstände bereits, verwenden sie jedoch nur gelegentlich.

Die Herausforderung besteht darin, Angebot und Nachfrage lokal zusammenzubringen und den Austausch von Gegenständen möglichst einfach und übersichtlich zu gestalten.

⸻

Need Finding

Zur Analyse des Problems haben wir die Situation aus Sicht der Leiher und Verleiher betrachtet.

Dabei wurden folgende Probleme identifiziert:

* Werkzeuge und technische Geräte sind oft teuer in der Anschaffung.
* Viele Gegenstände werden nur selten benötigt.
* Nutzer wissen häufig nicht, wer in ihrer Umgebung passende Gegenstände besitzt.
* Bestehende Plattformen konzentrieren sich überwiegend auf Kauf und Verkauf.
* Es fehlt eine einfache Möglichkeit zum lokalen Ausleihen.
* Nutzer wünschen Transparenz über den Status ihrer Anfragen.
* Verleiher möchten selbst entscheiden können, ob sie eine Anfrage annehmen oder ablehnen.

Diese Erkenntnisse zeigen, dass eine lokale Verleihplattform einen echten Mehrwert bieten kann.

⸻

Zielgruppe

Studierende

* verfügen häufig über ein begrenztes Budget
* benötigen Werkzeuge oder technische Geräte nur gelegentlich
* möchten unnötige Anschaffungskosten vermeiden

Anwohner

* besitzen Werkzeuge oder technische Geräte
* nutzen diese oft nur selten
* möchten vorhandene Ressourcen sinnvoll einsetzen

⸻

Persona

Anna Müller

Alter: 23 Jahre

Beruf: Studentin

Wohnort: Berlin

Familienstand: Ledig

Ziele

* Geld sparen
* Werkzeuge bei Bedarf nutzen
* Unnötige Anschaffungen vermeiden

Herausforderungen

* Begrenztes Budget
* Besitzt nur wenige Werkzeuge
* Benötigt Gegenstände nur gelegentlich

Zitat

„Ich brauche eine Bohrmaschine nur für ein einziges Projekt. Ein Kauf lohnt sich nicht.“

Erkenntnis

Anna legt mehr Wert auf einen einfachen Zugang zu Werkzeugen als auf deren Besitz.

⸻

Nutzerbedürfnisse

Bedürfnisse der Leiher

* schneller Zugang zu benötigten Gegenständen
* geringere Kosten gegenüber einem Neukauf
* einfache Suche nach verfügbaren Gegenständen
* Transparenz über den Status einer Anfrage

Bedürfnisse der Verleiher

* einfache Verwaltung ihrer Gegenstände
* Kontrolle über Ausleihanfragen
* Übersicht über laufende Anfragen
* Möglichkeit, Anfragen anzunehmen oder abzulehnen

⸻

Umfrage

Zur Überprüfung unserer Annahmen haben wir folgende Umfragefragen erstellt:

1. Haben Sie schon einmal ein Werkzeug oder technisches Gerät nur für kurze Zeit benötigt?
2. Würden Sie einen Gegenstand lieber ausleihen als kaufen?
3. Besitzen Sie Werkzeuge oder technische Geräte, die Sie selten nutzen?
4. Würden Sie eigene Gegenstände an andere verleihen?
5. Ist es Ihnen wichtig, Ausleihanfragen selbst annehmen oder ablehnen zu können?
6. Würden Sie eine Plattform wie LocalLend nutzen?
7. Welche Funktion wäre für Sie am wichtigsten?

⸻

Lösungsansätze

Lösung	Vorteile	Nachteile
WhatsApp-Gruppe	Schnell umsetzbar	Unübersichtlich bei vielen Anfragen
Gemeinsame Tabelle	Einfach zu erstellen	Schlechte Benutzerfreundlichkeit
Kauf-/Verkaufsplattform	Bekanntes Konzept	Fokus auf Kauf statt Ausleihe
Verleih-Web-App	Strukturierter Prozess	Höherer Entwicklungsaufwand

⸻

Gewählte Lösung

Wir haben uns für eine webbasierte Verleihplattform entschieden.

Mit LocalLend können Nutzer:

* Gegenstände einstellen
* verfügbare Angebote durchsuchen
* Ausleihanfragen stellen
* Anfragen annehmen oder ablehnen
* den Status von Anfragen verfolgen

Dadurch werden sowohl die Bedürfnisse der Leiher als auch der Verleiher berücksichtigt.

⸻

Nutzerrollen

Wir haben uns bewusst dafür entschieden, Nutzer nicht dauerhaft als „Verleiher“ oder „Leiher“ einzustufen.

Jeder Nutzer kann sowohl Gegenstände verleihen als auch ausleihen. Die Rolle ergibt sich jeweils aus der aktuellen Interaktion innerhalb der Plattform.

Diese Entscheidung erhöht die Flexibilität der Anwendung und entspricht dem tatsächlichen Verhalten unserer Zielgruppe.

⸻

Prototyp

Der aktuelle Prototyp umfasst folgende Kernfunktionen:

Benutzerverwaltung

* Registrierung
* Login
* Logout

Gegenstandsverwaltung

* Gegenstände erstellen
* Gegenstände anzeigen
* Gegenstände durchsuchen

Anfrage-System

* Ausleihanfrage stellen
* Anfrage annehmen
* Anfrage ablehnen
* Anfrage löschen
* Status einer Anfrage anzeigen

API

* JSON-Endpunkt für Gegenstände
* JSON-Endpunkt für Anfragen
* JSON-Endpunkt zum Erstellen einer Anfrage
* JSON-Endpunkt zum Annehmen einer Anfrage
* JSON-Endpunkt zum Ablehnen einer Anfrage
* JSON-Endpunkt zum Löschen einer Anfrage
* API-Status-Endpunkt

⸻

Zusammenhang mit dem Anfrage-System

Im Anfrage-System werden verschiedene Statuswerte verwendet:

Status	Bedeutung
pending	Anfrage wurde erstellt
accepted	Anfrage wurde angenommen
rejected	Anfrage wurde abgelehnt
deleted	Anfrage wurde gelöscht

Dadurch können Nutzer jederzeit nachvollziehen, in welchem Zustand sich ihre Anfrage befindet.

⸻

Feedback

Erstes informelles Feedback aus dem Team und dem Umfeld zeigt:

Positives Feedback

* hilfreiche Lösung für Studierende
* spart Kosten
* leicht verständliches Konzept
* unterstützt nachhaltige Ressourcennutzung

Verbesserungsvorschläge

* Suchfunktion erweitern
* Kategorien ergänzen
* Status von Anfragen deutlicher anzeigen
* mehr Informationen zu Gegenständen anzeigen

⸻

Value Proposition

Kundengruppe

* Studierende
* Anwohner

Aufgaben der Nutzer

* Werkzeuge ausleihen
* Gegenstände verleihen
* Geld sparen
* Ressourcen sinnvoll nutzen

Probleme

* Hohe Anschaffungskosten
* Fehlender Zugang zu bestimmten Werkzeugen
* Seltene Nutzung vieler Gegenstände

Nutzen

* Kostengünstiger Zugang zu Werkzeugen und Geräten
* Nachhaltige Nutzung vorhandener Ressourcen
* Unterstützung lokaler Gemeinschaften
* Transparente Anfrageverwaltung

Unsere Lösung

LocalLend verbindet Verleiher und Leiher auf einer gemeinsamen Plattform und vereinfacht den gesamten Ausleihprozess – von der Suche bis zur Anfrageverwaltung.

⸻

Zusammenhang mit den Design Decisions

Die Ergebnisse des Product Discovery haben unsere Design Decisions beeinflusst:

* Nutzer wünschen Kontrolle → Anfragebasiertes Ausleihen wurde gewählt.
* Nutzer wünschen Transparenz → Statuswerte wie „pending“, „accepted“ und „rejected“ wurden eingeführt.
* Strukturierte Daten werden benötigt → JSON-API wurde implementiert.
* Eine einfache Nutzung ist wichtig → klare Benutzeroberfläche mit Suchfunktion.
* Die Anwendung soll später erweitert werden können → API und Frontend wurden getrennt aufgebaut.

⸻

Fazit

Das Product Discovery hat gezeigt, dass ein echter Bedarf für eine lokale Plattform zum Verleihen und Ausleihen von Werkzeugen und technischen Geräten besteht.

Leiher profitieren von einem kostengünstigen Zugang zu benötigten Gegenständen, während Verleiher ihre vorhandenen Ressourcen sinnvoll nutzen können.

Die bisherigen Erkenntnisse bestätigen die Relevanz der Lösung LocalLend und unterstützen die Entwicklung einer lokalen Plattform für das Verleihen und Ausleihen von Werkzeugen und technischen Geräten.