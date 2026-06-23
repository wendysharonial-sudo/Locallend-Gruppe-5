---

title: Jean Yves Nkwane

parent: Individual Contributions

nav_order: 2

---



{: .no_toc }

# Jean Yves Nkwane



<details open markdown="block">

<summary>Inhaltsverzeichnis</summary>

+ ToC

{: toc }

{: .text-delta }

</details>



## Meta-Goals



### Target grade



1.0



### Personal goals



Mein Hauptziel in diesem Projekt war es, meine Fähigkeiten in der Frontend-Entwicklung gezielt auszubauen. Insbesondere wollte ich die Strukturierung mit HTML und CSS sowie die dynamische Seitengenerierung mittels Jinja2 meistern. Mir war es wichtig, ein tiefes Verständnis dafür zu entwickeln, wie Frontend-Templates und das Flask-Backend nahtlos miteinander interagieren, um eine benutzerfreundliche und reibungslose Oberfläche (wie z. B. unseren "Happy Path") zu schaffen.



---



## Eidesstattliche Erklärung



**Jean Yves Nkwane, Matrikelnr.: 77201393552**



Ich erkläre an Eides statt:



Diese Arbeit habe ich selbständig und eigenhändig erstellt.

Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.



Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierter Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.



Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.



---



## Top-3 Contributions



| \# | My contribution | Why I am proud of it | Which challenge I overcame |

| :-- | :-- | :-- | :-- |

| 1 | **Strukturierung der Frontend-Architektur (Base-Template & bedingte Navbar)** | Das `base.html` bildet das visuelle und funktionale Rückgrat der gesamten Web-App. Die Implementierung der dynamischen, sitzungsbasierten Navigationsleiste macht die App erst interaktiv. | Die Herausforderung bestand darin, die Jinja2-Vererbung (`{% extends %}`) korrekt aufzusetzen und Backend-Sitzungsvariablen sauber für die Frontend-Darstellung (Login/Logout Zustand) nutzbar zu machen. |

| 2 | **Implementierung des gesamten "Happy Paths" (CRUD-Formulare & Profilseite)** | Durch die Erstellung der Login-, Register-, Items-, und Profil-Seiten hat die App einen vollständigen, flüssigen Workflow für den Endnutzer bekommen. | Es war anspruchsvoll, die HTML-Formulare (`method="POST"`) exakt auf die Erwartungen des Backends abzustimmen und komplexe Jinja2-Schleifen für die dynamische Anzeige von Benutzer-Items fehlerfrei einzubinden. |

| 3 | **Design & Modernes Custom CSS** | Ich habe der App mit Custom Utilities, Hero-Sections auf der Landingpage und fließenden Übergängen einen modernen, professionellen Look verliehen, der weit über Standard-Bootstrap hinausgeht. | Das korrekte Zusammenspiel von Custom CSS (Transitions, Hover-Effekte) und dem existierenden Bootstrap-Framework erforderte viel Feinabstimmung, ohne Layout-Brüche zu riskieren. |



## Design Decisions that I led



1. [DD-05](../../../evidence/design-decisions/dd-05.md)

2. [DD-06](../../../evidence/design-decisions/dd-06.md)



---



## Contributions



| Contribution | Proof (Git Commits) | Sources used |

| :-- | :-- | :-- |

| **Base Jinja2 Layout & Bootstrap Navbar** | Branch `yves-frontend`, Commit `b492ee0` | [Bootstrap Navbar Docs](https://getbootstrap.com/docs/5.3/components/navbar/), [Flask Flash Messages](https://flask.palletsprojects.com/en/latest/patterns/flashing/) |

| **Dynamische Navbar (Login/Logout Status)** | Branch `yves-frontend`, Commit `732055f` | [Flask Session Docs](https://flask.palletsprojects.com/en/latest/quickstart/#sessions) |

| **Landing Page Design (Hero Section)** | Branch `yves-frontend`, Commits `91dcd0d`, `45cd105` | [Bootstrap Grid Layout](https://getbootstrap.com/docs/5.3/layout/grid/) |

| **Modern Custom CSS (Styling & Utilities)** | Branch `yves-frontend`, Commit `a9c05f4` | [MDN CSS Transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions) |

| **Auth-Formulare (Login & Register)** | Branch `yves-frontend`, Commit `8a9ca12` | [Bootstrap Forms](https://getbootstrap.com/docs/5.3/forms/overview/) |

| **Items-Seite & Jinja2 Item-Schleife** | Branch `yves-frontend`, Commits `4b41821`, `4b853c5` | [Jinja2 Control Structures](https://jinja.palletsprojects.com/en/latest/templates/#for) |

| **CRUD Formulare (Add & Edit Item)** | Branch `yves-frontend`, Commits `5514256`, `9d76ed4` | Eigene Implementierung |

| **Dynamische Profilseite (Jinja2 Variablen)** | Branch `yves-frontend`, Commit `361ec46` | Eigene Implementierung |

| **Custom 404 Fehlerseite** | Branch `yves-frontend`, Commit `5514256` | [Flask Error Handling](https://flask.palletsprojects.com/en/latest/errorhandling/) |

| **Projekt-Setup (.gitignore)** | Branch `main`, Commit `c8d9c4a` | [GitHub gitignore templates](https://github.com/github/gitignore) |



---



## AI Directory



| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |

| :-- | :--     | :--            | :--                             | :--                         |

| 01  | ChatGPT | Verständnisfragen zu Bootstrap 5 Grid-System und Layout-Klassen | `style.css`, `base.html`, Landingpage | Ich habe nach Best Practices gefragt, um Container responsiv auszurichten (z.B. für die Hero-Section). Den Code habe ich daraufhin manuell konzipiert. |

| 02  | ChatGPT | Erklärung von Jinja2 Template-Vererbung (`extends`, `block`) | Alle `.html` Templates | Gefragt: "Wie strukturiert man in Flask am besten ein modulares Base-Template?". Das gelieferte Konzept habe ich selbst in die Architektur übertragen. |

| 03  | ChatGPT | Hilfe beim Verständnis von CSS-Transitions und Custom Styles | `style.css` | Gefragt nach Beispielen für sanfte Hover-Effekte auf Web-Elementen. Die exakten Werte und Farbpaletten wurden von mir manuell ins Design integriert. |