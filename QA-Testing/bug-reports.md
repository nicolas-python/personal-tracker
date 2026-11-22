### REG-BUG-001: Passwortfeld liegt über dem Popup
**Bereich:** Register/Login

**Schritte zur Reproduktion:**
1. Login-Seite öffnen
2. Anmelden
3. Beobachten, dass das Passwortfeld über dem Popup liegt

**Erwartetes Verhalten:**
Das Popup wird vollständig im Vordergrund angezeigt

**Tatsächliches Verhalten:**
Das Passwort-Eingabefeld liegt optisch über dem Popup

**Ursache:**
Fehlender "z-index" beim Popup

**Lösung:**
"z-index: 2000" zur CSS-Klasse ".popup" hinzugefügt

**Betroffene Testfälle:**
LOG-001
LOG-002
LOG-003
LOG-004
LOG-006

**Status:** Fixed


### TR-BUG-002 Trainingsplan bearbeiten
**Bereich:** Trainingspläne bearbeiten/workouts

**Schritte zur Reproduktion:**
1. Einen bestehenden Trainingsplan auswählen
2. Trainingsplan bearbeiten drücken (✏️)
3. Den Namen des Trainingsplans ändern
4. Änderungen speichern
5. Erfolgsmeldung bestätigen

**Erwartetes Ergebnis:**
Aktualisierungsmeldung "Trainingsplan aktualisiert!" wird angezeigt
Trainingsplan wird erfolgreich aktualisiert
Weiterleitung zur workouts-Seite erfolgt
Der neue Name wird in der Übersicht angezeigt

**Testergebnis:**
Aktualisierungsmeldung "Trainingsplan aktualisiert!" wird angezeigt
Trainingsplan wird erfolgreich aktualisiert
Keine Weiterleitung zur workouts-Seite
Benutzer wird stattdessen auf /create-workout weitergeleitet
Der neue Name wird korrekt in der Übersicht angezeigt

**Ursache:**
Noch nicht technisch analysiert. Beobachtetes Fehlerverhalten: Falsche Weiterleitung nach Bestätigung der Erfolgsmeldung

**Lösung:**

**Betroffene Testfälle:**
TR-002
TR-004
TR-005

**Status:**  Open

### TR-BUG-003 Trainingsplan mit leerem Namen erstellen
**Bereich:** Trainingsplan erstellen

**Schritte zur Reproduktion:**
1. Einen neuen Trainingsplan erstellen
2. Das Namensfeld leer lassen
3. Speichern versuchen

**Erwartetes Ergebnis:**
Trainingsplan wird nicht erstellt
Eine entsprechende Fehlermeldung wird angezeigt

**Testergebnis:**
Trainingsplan kann nicht mehr ohne Namen erstellt werden
Auch Eingaben, die nur aus Leerzeichen bestehen, werden verhindert
Normale Trainingsplannamen funktionieren weiterhin

**Ursache:** 
Die Eingabe des Trainingsplannamens wird nicht ausreichend abgesichert

**Lösung:**
Eine Bedingung wurde eingebaut die " " und Leerzeichen in Create workout verhindert
Bei leerem Input-Feld wird eine fehlermeldung Angezeigt 

**Betroffene Testfälle:**
TR-006

**Status:**  Fixed

