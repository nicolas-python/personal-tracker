-----------------------------------------------
## Registrieren
-----------------------------------------------
### REG-001 Registrierung mit gültigen Daten
**Voraussetzung:**
Die Registrierungsseite ist erreichbar
Der gewählte Benutzername ist noch nicht vergeben
Die maximale Benutzeranzahl ist noch nicht erreicht

**Testschritte:**
1. Registrierungsseite öffnen
2. Benutzernamen eingeben "test1"
3. Passwort eingeben
4. Passwort bestätigen
5. Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Der Benutzer wird erfolgreich erstellt 
Eine Bestätigungsmeldung wird angezeigt
Der Benutzer wird zur Loginseite weitergeleitet

**Testergebnis:**
Benutzer wurde erfolgreich erstellt und zur Loginseite weitergeleitet

**Status:** Passed

### REG-002 Registrierung mit bereits vorhandenem Benutzernamen
**Voraussetzung:**
Die Registrierungsseite ist erreichbar
Ein Benutzerkonto mit dem gewählten Benutzernamen existiert bereits

**Testschritte:**
1. Registrierungsseite öffnen
2. Benutzernamen `test1` eingeben 
3. Passwort eingeben
4. Passwort bestätigen
5. Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Die Registrierung wird abgelehnt
Eine Fehlermeldung informiert darüber, dass der Benutzername bereits vergeben ist
Es wird kein neues Benutzerkonto erstellt

**Testergebnis:**
Fehlermeldung: "Der Benutzername ist bereits vergeben"
Kein neues Benutzerkonto erstellt

**Status:** Passed

### REG-003 Registrierung mit leerem Passwort
**Voraussetzung:**
Die Registrierungsseite ist erreichbar

**Testschritte:**
1. Registrierungsseite öffnen
2. Benutzernamen eingeben 
3. Passwort leere lassen 
4. Passwort bestätigen leere lassen
5. Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Die Registrierung wird abgelehnt
Eine Fehlermeldung informiert darüber, dass alle Pflichtfelder ausgefüllt werden müssen
Es wird kein neues Benutzerkonto erstellt

**Testergebnis:**
Fehlermeldung: "Bitte alle Felder ausfüllen"
Kein neues Benutzerkonto erstellt

**Status:** Passed

### REG-004 Registrierung mit leerem Paket auswahl
**Voraussetzung:**
Die Registrierungsseite ist erreichbar

**Testschritte:**
1. Registrierungsseite öffnen
2. Benutzernamen eingeben 
3. Passwort eingeben 
4. Passwort bestätigen ausfüllen
5. Kein Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Die Registrierung wird abgelehnt
Eine Fehlermeldung informiert darüber, dass ein Paket gewählt werden muss
Es wird kein neues Benutzerkonto erstellt

**Testergebnis:**
Fehlermeldung: "Ungültige Paketauswahl"
Kein neues Benutzerkonto erstellt

**Status:** Passed

### REG-005 Registrierung mit leerem Benutzernamen
**Voraussetzung:**
Die Registrierungsseite ist erreichbar

**Testschritte:**
1. Registrierungsseite öffnen
2. Kein Benutzernamen eingeben 
3. Passwort eingeben 
4. Passwort bestätigen ausfüllen
5. Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Die Registrierung wird abgelehnt
Eine Fehlermeldung informiert darüber, dass alle Pflichtfelder ausgefüllt werden müssen
Es wird kein neues Benutzerkonto erstellt

**Testergebnis:**
Fehlermeldung: "Bitte alle Felder ausfüllen"
Kein neues Benutzerkonto erstellt

**Status:** Passed

### REG-006 Registrierung mit nicht übereinstimmenden Passwörtern
**Voraussetzung:**
Die Registrierungsseite ist erreichbar

**Testschritte:**
1. Registrierungsseite öffnen
2. Benutzernamen eingeben 
3. Passwort eingeben  "Test123"
4. anderes Passwort in Passwort bestätigen eingeben "Test456"
5. Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Die Registrierung wird abgelehnt
Eine Fehlermeldung informiert darüber, dass Passwörter übereinstimmen müssen
Es wird kein neues Benutzerkonto erstellt

**Testergebnis:**
Fehlermeldung: "Die Passwörter stimmen nicht überein"
Kein neues Benutzerkonto erstellt

**Status:** Passed

### REG-007 Maximale Benutzeranzahl erreicht
**Voraussetzung:**
Die Registrierungsseite ist erreichbar
Maximale Benutzeranzahl erreicht (8 Stück)

**Testschritte:**
1. Registrierungsseite öffnen
2. Benutzernamen eingeben 
3. Passwort eingeben 
4. Passwort bestätigen eingeben
5. Paket Auswählen
6. Auf „Registrieren“ klicken

**Erwartetes Ergebnis:**
Die Registrierung wird abgelehnt
Eine Fehlermeldung informiert darüber, dass die Benutzeranzahl überschirtten ist 
Es wird kein neues Benutzerkonto erstellt

**Testergebnis:**
Fehlermeldung: "Maximale Benutzeranzahl von 8 erreicht!"
Datenbank enthält genau 8 Benutzer
Kein neues Benutzerkonto erstellt

**Status:** Passed

### REG-008  Passwort anzeigen/verbergen testen
**Voraussetzung:**
Die Registrierungsseite ist erreichbar

**Testschritte:**
1. Passwort eingeben
2. Auf das Schloss-Symbol klicken (Passwort wird angezeigt)
3. Auf das Auge-Symbol klicken (Passwort wird wieder verborgen)

**Erwartetes Ergebnis:**
Nach dem Klick auf das Schloss-Symbol wird das Passwort als Klartext angezeigt
Nach erneutem Klick wird das Passwort wieder verborgen dargestellt

**Testergebnis:**
Wechsel zwischen sichtbarem und verborgenem Passwort funktioniert

**Status:** Passed

-----------------------------------------------
## Login
-----------------------------------------------
### LOG-001 Login mit korrekten Zugangsdaten
**Voraussetzung:**
Die Loginseite ist erreichbar
Ein Benutzerkonto existiert bereits

**Testschritte:**
1. Benutzernamen eingeben 
2. Passwort eingeben
3. Auf „Einloggen“ klicken

**Erwartetes Ergebnis:**
Login-Bestätigung wird als Popup angezeigt
Weiterleitung auf Selection/Homepage

**Testergebnis:**
Das Passwort-Eingabefeld liegt optisch über dem Popup
Selection/Homepage wird angezeigt

**Status:** Passed

### LOG-002 Login mit falschem Passwort
**Voraussetzung:**
Die Loginseite ist erreichbar
Ein Benutzerkonto existiert bereits

**Testschritte:**
1. Benutzernamen eingeben 
2. falsches Passwort eingeben
3. Auf „Einloggen“ klicken

**Erwartetes Ergebnis:**
Fehlermeldung: "Passwort oder Benutzername sind Falsch"
Keine Weiterleitung auf Selection/Homepage

**Testergebnis:**
Fehlermeldung: "Login fehlgeschlagen: Passwort oder Benutzername falsch"
Das Passwort-Eingabefeld liegt optisch über dem Popup (siehe BUG-001)
Selection/Homepage wird nicht angezeigt

**Status:** Failed

### LOG-003 Login mit unbekanntem Benutzernamen
**Voraussetzung:**
Die Loginseite ist erreichbar
Ein Benutzerkonto existiert bereits

**Testschritte:**
1. Unbekannten Benutzernamen eingeben "test10"
2. Passwort eingeben
3. Auf „Einloggen“ klicken

**Erwartetes Ergebnis:**
Fehlermeldung: "Passwort oder Benutzername sind Falsch"
Keine Weiterleitung auf Selection/Homepage

**Testergebnis:**
Fehlermeldung: "Login fehlgeschlagen: Passwort oder Benutzername falsch"
Das Passwort-Eingabefeld liegt optisch über dem Popup (siehe BUG-001)
Selection/Homepage wird nicht angezeigt

**Status:** Passed

### LOG-004 Login ohne Eingabe
**Voraussetzung:**
Die Loginseite ist erreichbar

**Testschritte:**
1. Benutzernamen leer lassen
2. Passwort leer lassen
3. Auf „Einloggen“ klicken

**Erwartetes Ergebnis:**
Fehlermeldung: "Passwort oder Benutzername sind Falsch"
Keine Weiterleitung auf Selection/Homepage

**Testergebnis:**
Fehlermeldung: "Login fehlgeschlagen: Passwort oder Benutzername falsch"
Das Passwort-Eingabefeld liegt optisch über dem Popup (siehe BUG-001)
Selection/Homepage wird nicht angezeigt

**Status:** Failed

### LOG-005  Passwort anzeigen/verbergen testen
**Voraussetzung:**
Die Loginseite ist erreichbar

**Testschritte:**
1. Passwort eingeben
2. Auf das Schloss-Symbol klicken (Passwort wird angezeigt)
3. Auf das Auge-Symbol klicken (Passwort wird wieder verborgen)

**Erwartetes Ergebnis:**
Nach dem Klick auf das Schloss-Symbol wird das Passwort als Klartext angezeigt
Nach erneutem Klick wird das Passwort wieder verborgen dargestellt

**Testergebnis:**
Wechsel zwischen sichtbarem und verborgenem Passwort funktioniert

**Status:** Passed

### LOG-006 Mehrfach falsche Loginversuche testen
**Voraussetzung:**
Die Loginseite ist erreichbar

**Testschritte:**
1. Falscher Benutzer eingeben
2. Falsches Passwort eingeben
3. Auf „Einloggen“ klicken
4. Den Vorgang mehrfach innerhalb einer Minute wiederholen

**Erwartetes Ergebnis:**
Anzeige: "Login fehlgeschlagen: Passwort oder Benutzername falsch"
Nach drei erlaubten Versuchen innerhalb einer kurzen zeitspanne werden weitere Loginversuche blockiert

**Testergebnis:**
Das Passwort-Eingabefeld liegt optisch über dem Popup (siehe BUG-001)
Anzeige: "Login fehlgeschlagen: Passwort oder Benutzername falsch"
Nach drei erlaubten Versuchen wird der weitere Loginversuch blockiert
Anzeige: "Too Many Requests – 3 per 1 minute"

**Status:** Passed

### LOG-007 Login mit Leerzeichen im Benutzernamen

**Voraussetzung:**
Die Loginseite ist erreichbar
Ein Benutzerkonto mit Leerzeichen im Benutzernamen existiert bereits

**Testschritte:**
1. Benutzernamen mit Leerzeichen eingeben
2. Korrektes Passwort eingeben
3. Auf „Einloggen“ klicken

**Erwartetes Ergebnis:**
Login mit dem Benutzernamen funktioniert
Weiterleitung auf Selection/Homepage

**Testergebnis:**
Login mit Leerzeichen im Benutzernamen funktioniert

**Status:** Passed


### LOG-008: Abmeldung und Zugriffsschutz nach Logout

**Voraussetzung:**
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Logout-Button anklicken
2. Beobachten, auf welche Seite man weitergeleitet wird
3. URL http://127.0.0.1:5001/selection direkt in die Adresszeile eingeben

**Erwartetes Ergebnis:**
Benutzer wird erfolgreich abgemeldet
Weiterleitung zur Login-Seite erfolgt
Die aktive Sitzung wird beendet
Erneuter Zugriff auf geschützte Seiten wird verweigert
Benutzer wird wieder zur Login-Seite weitergeleitet

**Testergebnis:**
Benutzer wird erfolgreich abgemeldet
Weiterleitung zur Login-Seite erfolgt
Die aktive Sitzung wird beendet

**Status:** Passed


### LOG-009: Automatischer logout nach 30 min
**Voraussetzung:**
Benutzer ist erfolgreich angemeldet
Auswahlseite ist geöffnet

**Testschritte:**
1. Benutzer anmelden
2. Mindestens 30 Minuten keine Aktivität durchführen   (für den Test wurde die Zeit vorübergehend auf 1 Minute / 60 Sekunden gesetzt)
3. Anschließend eine geschützte Seite aufrufen (z. B. Tanken)
4. Angezeigte Meldung und Weiterleitung prüfen

**Erwartetes Ergebnis:**
Die aktive Sitzung wird nach 30 Minuten Inaktivität ungültig
Benutzer wird zur Login-Seite weitergeleitet
Die Meldung "Deine Sitzung ist abgelaufen oder wurde auf einem anderen Gerät ersetzt" wird angezeigt

**Testergebnis:**
- Automatischer Logout nach 1 Minute (temporär für den Test eingestellt)
- Weiterleitung zur Login-Seite erfolgt
- Die Meldung "Deine Sitzung ist abgelaufen oder wurde auf einem anderen Gerät ersetzt" wird angezeigt

**Status:** Passed


### LOG-009: Login desselben Benutzers auf mehreren Geräten

**Voraussetzung:**
Ein Benutzerkonto existiert
Zwei unterschiedliche Browser oder Geräte stehen zur Verfügung

**Testschritte:**
1. Im ersten Browser mit dem Benutzer anmelden
2. Im zweiten Browser dieselben Zugangsdaten verwenden
3. Prüfen, ob die Anmeldung im zweiten Browser erfolgreich ist
4. Im ersten Browser eine geschützte Seite aufrufen
5. Im zweiten Browser eine geschützte Seite aufrufen

**Erwartetes Ergebnis:**
Die bisherige Sitzung wird beendet
Ausloggen der aktiven Sitzung mit der Fehlermeldung :"Deine Sitzung ist abgelaufen oder wurde auf einem anderen Gerät ersetzt"
Es können maximal 1 aktive Sitzungen pro Benutzer gleichzeitig bestehen

**Testergebnis:**
Die bisherige Sitzung wird beendet
Die erwartete Fehlermeldung wird angezeigt
Es besteht maximal eine aktive Sitzung pro Benutzer

**Status:** Passed

-----------------------------------------------
##Homepage / Navigation
-----------------------------------------------
### HOME-001: Homepage nach erfolgreichem Login anzeigen

**Voraussetzung:**
Ein Benutzerkonto existiert
Benutzer befindet sich auf der Login-Seite

**Testschritte:**
1. Gültigen Benutzernamen eingeben
2. Gültiges Passwort eingeben
3. Auf den Login-Button klicken
4. Popup "Login erfolgreich!" bestätigen
5. Weiterleitung zur Selection / Homepage abwarten
6. Angezeigte Seite prüfen

**Erwartetes Ergebnis:**
Login ist erfolgreich
Popup "Login erfolgreich!" wird angezeigt 
Benutzer wird zur Homepage / Auswahlseite weitergeleitet
Benutzername wird auf der Homepage angezeigt
Homepage wird vollständig und korrekt dargestellt

**Testergebnis:**
Login ist erfolgreich
Popup "Login erfolgreich!" wird angezeigt
Benutzer wird zur Homepage / Auswahlseite weitergeleitet
Benutzername wird auf der Homepage angezeigt
Homepage wird vollständig und korrekt dargestellt

**Status:** Passed


### HOME-002: Navigation zu allen verfügbaren Bereichen
**Voraussetzung:**
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Jeden verfügbaren Bereich auf der Homepage einzeln anklicken
2. Prüfen, ob der jeweilige Bereich geöffnet wird
3. Prüfen, ob die richtige Seite angezeigt wird
4. Zur Homepage zurückkehren
5. Mit dem nächsten Bereich fortfahren

**Erwartetes Ergebnis:**
Alle verfügbaren Bereiche sind erreichbar
Jeder Bereich öffnet die richtige Seite
Die Navigation funktioniert ohne Fehlermeldungen

**Testergebnis:**
Alle verfügbaren Bereiche sind erreichbar
Jeder Bereich öffnet die richtige Seite
Die Navigation funktioniert ohne Fehlermeldungen


**Status:** Passed

### HOME-003: Zurück-Navigation funktioniert
**Voraussetzung:**
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Einen verfügbaren Bereich öffnen (z. B. Ernährung)
2. Zurück-Button anklicken
3. Prüfen, ob die Homepage / Auswahlseite wieder angezeigt wird
4. Den Vorgang bei weiteren Bereichen wiederholen

**Erwartetes Ergebnis:**
Zurück-Button funktioniert
Benutzer wird zur Homepage / Auswahlseite zurückgeleitet
Homepage wird korrekt dargestellt
Es treten keine Fehlermeldungen auf

**Testergebnis:**
Zurück-Button funktioniert
Benutzer wird zur Homepage / Auswahlseite zurückgeleitet
Homepage wird korrekt dargestellt
Es treten keine Fehlermeldungen auf

**Status:** Passed

### HOME-003: Gesperrte Bereiche werden angezeigt und sind nicht anklickbar
**Voraussetzung:**
Benutzerkonto mit Paket Basic existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Homepage mit einem Basic-Benutzer öffnen
2. Premium- und Premium+-Bereiche kontrollieren (gesperrt)
3. Prüfen, ob gesperrte Bereiche mit einem Schloss gekennzeichnet sind
4. Versuchen, die gesperrten Bereiche anzuklicken
5. Prüfen, ob Statistiken für Basic-Benutzer gesperrt sind

**Erwartetes Ergebnis:**
Premium- und Premium+-Bereiche werden angezeigt
Gesperrte Bereiche sind optisch als gesperrt gekennzeichnet
Gesperrte Bereiche können nicht angeklickt werden
Es erfolgt keine Weiterleitung in einen gesperrten Bereich
Premium-Statistiken sind für Basic-Benutzer nicht verfügbar

**Testergebnis:**
Premium- und Premium+-Bereiche werden angezeigt
Gesperrte Bereiche sind optisch als gesperrt gekennzeichnet
Gesperrte Bereiche können nicht angeklickt werden
Es erfolgt keine Weiterleitung in einen gesperrten Bereich

**Status:** Passed