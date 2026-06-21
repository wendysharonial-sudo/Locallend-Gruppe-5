Individual Contribution - Tuba Celik

## Verantwortungsbereich

Mein Verantwortungsbereich im Projekt lag hauptsächlich im Backend-Bereich für die Benutzerverwaltung.

Dabei hab ich insbesondere an folgenden Bereichen gearbeitet:

- Flask-Routen
- Registrierung 
- Login
- Logout
- Session-Verwaltung
- Integration mit dem Benutzermodell

Meine drei wichtigsten Beiträge

1. Login- und Registrierungs-Backend

Ich habe die Backend-Routen für die Benutzerregistrierung und den Login implementiert.

Dieser Beitrag ist wichtig, da Nutzerinnern und Nutzer ein Konto benötigen, um LocalLend strukturiert verwenden zu können. Die Registrierungsroute verarbeitet die Eingaben des Benutzers, speichert die Daten und leitet anschließend zur Login-Seite weiter. Die Login-Route überprüft die Zugangsdaten und startet eine Session für den angemeldeten Benutzer.

Auf diesen Beitrag bin ich besonders stolz, da dadurch die Benutzeroberfläche mit der Backend-Logik verbunden wird und die Grundlage für echte Benutzerkonten geschaffen wurde.

Herausforderung:

Ich musste zunächst verstehen, wie Flask mit GET- und POST-Anfragen arbeitet und wie Formulardaten mit request.form verarbeitet werden.

Nachweis:

- app.py
- Commit „Add login and register backend“

2. Session-Verwaltung und Logout

Ich habe die Session-Verwaltung implementiert, um angemeldete Benutzer innerhalb der Anwendung verwalten zu können.

Nach einem erfolgreichen Login werden die Benutzer-ID und der Benutzername in der Session gespeichert. Beim Logout wird die Session geleert und der Benutzer zurück zur Startseite geleitet.

Ich bin auf diesen Beitrag stolz, da Session-Verwaltung ein wichtiger Bestandteil von Webanwendungen ist und den Login-Prozess sinnvoll macht.

Herausforderung:

Ich musste verstehen, wie Sessions in Flask funktionieren und weshalb ein Secret Key benötigt wird.

Nachweis:

- app.py
- session["user_id"]
- session["user_name"]
- session.clear()

3. Integration des Backends und Zusammenarbeit mit Git

Ich habe meine Backend-Änderungen in die bestehende Projektstruktur integriert.

Dazu gehörte die Arbeit auf einem eigenen Branch, das Einbinden von Änderungen anderer Teammitglieder sowie das Lösen von Integrationsproblemen, ohne bereits vorhandene Arbeit zu verlieren.

Auf diesen Beitrag bin ich stolz, da ich dadurch den Umgang mit Git und die Zusammenarbeit in einem Teamprojekt praktisch erlernen konnte.

Herausforderung:

Ich musste Merge- und Rebase-Probleme bewältigen und sicherstellen, dass meine Änderungen korrekt gespeichert und gepusht werden.

Nachweis:

- Branch tuba-backend
- Commit „Add login and register backend“