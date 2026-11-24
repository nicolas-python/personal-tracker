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
Selection/Homepage wird nicht angezeigt

**Status:** Passed

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
Selection/Homepage wird nicht angezeigt

**Status:** Passed

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

### HOME-004: Gesperrte Bereiche werden angezeigt und sind nicht anklickbar
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

### HOME-005: Freigeschaltete Bereiche bei Premium
**Voraussetzung:**
Benutzerkonto mit Paket Premium existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Homepage mit einem Premium-Benutzer öffnen
2. Premium- und Premium+-Bereiche kontrollieren
3. Prüfen, ob Premium-Bereiche freigeschaltet und anklickbar sind
4. Prüfen, ob Premium+-Bereiche weiterhin gesperrt sind
5. Versuchen, einen Premium-Bereich zu öffnen
6. Prüfen, ob Statistiken für Premium-Benutzer verfügbar sind

**Erwartetes Ergebnis:**
Premium-Bereiche sind freigeschaltet und anklickbar
Premium+-Bereiche sind optisch als gesperrt gekennzeichnet
Premium+-Bereiche können nicht angeklickt werden
Premium-Bereiche lassen sich öffnen
Premium-Statistiken sind verfügbar

**Testergebnis:**
Premium-Bereiche sind freigeschaltet und anklickbar
Premium+-Bereiche sind weiterhin gesperrt
Premium-Bereiche lassen sich öffnen
Premium-Statistiken sind verfügbar

**Status:** Passed

### HOME-006: Freigeschaltete Bereiche bei Premium+
**Voraussetzung:**
Benutzerkonto mit Paket Premium+ existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Homepage mit einem Premium+-Benutzer öffnen
2. Premium- und Premium+-Bereiche kontrollieren
3. Prüfen, ob alle Bereiche freigeschaltet und anklickbar sind
4. Premium-Bereiche öffnen
5. Premium+-Bereiche öffnen
6. Prüfen, ob Statistiken verfügbar sind

**Erwartetes Ergebnis:**
Premium-Bereiche sind freigeschaltet und anklickbar
Premium+-Bereiche sind freigeschaltet und anklickbar
Alle Bereiche lassen sich öffnen
Statistiken sind verfügbar

**Testergebnis:**
Premium- und Premium+-Bereiche sind freigeschaltet und anklickbar
Alle Bereiche lassen sich öffnen
Statistiken sind verfügbar

**Status:** Passed

### HOME-007 Darstellung auf verschiedenen Bildschirmgrößen prüfen
**Voraussetzung:**
Benutzerkonto existiert
Benutzer ist erfolgreich angemeldet
Login,Register, Homepage/Auswahlseite etc ist geöffnet

**Testschritte:**
1. Einloggen
2. Die jeweilige Seite im normalen Browserfenster öffnen
3. Darstellung und Layout überprüfen
4. Browser-Entwicklertools mit F12 öffnen
5. Auf eine mobile Bildschirmgröße wechseln
6. Darstellung und Layout auf dem simulierten Handy überprüfen

**Erwartetes Ergebnis:**
Alle Seiten werden im Browser korrekt dargestellt
Alle Seiten werden auf mobilen Bildschirmgrößen korrekt dargestellt
Inhalte und Bedienelemente sind vollständig sichtbar und nutzbar

**Testergebnis:**
Browserdarstellung ist korrekt
Mobile Darstellung ist korrekt
Inhalte und Bedienelemente sind vollständig sichtbar und nutzbar

**Status:** Passed

### HOME-008: Statistiken bei Premium speichern
**Voraussetzung:**
Benutzerkonto mit Paket Premium existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Premium-Benutzer anmelden
2. Statistikbereich öffnen
3. Werte im Kalorienbedarfsrechner eintragen oder vorhandene Werte ändern
4. Eingabe speichern
5. Seite neu laden
6. Prüfen, ob der gespeicherte Wert weiterhin angezeigt wird

**Erwartetes Ergebnis:**
Statistikbereich ist für Premium-Benutzer verfügbar
Werte im Kalorienbedarfsrechner können eingetragen und gespeichert werden
Gespeicherte Werte bleiben nach dem Neuladen erhalten

**Testergebnis:**
Statistikbereich ist verfügbar
Werte im Kalorienbedarfsrechner können eingetragen und gespeichert werden
Gespeicherte Werte bleiben nach dem Neuladen erhalten

**Status:** Passed

### HOME-009: Statistiken bei Premium+ speichern
**Voraussetzung:**
Benutzerkonto mit Paket Premium+ existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Premium+-Benutzer anmelden
2. Statistikbereich öffnen
3. Werte im Kalorienbedarfsrechner eintragen oder vorhandene Werte ändern
4. Eingabe speichern
5. Seite neu laden
6. Prüfen, ob der gespeicherte Wert weiterhin angezeigt wird

**Erwartetes Ergebnis:**
Statistikbereich ist für Premium+-Benutzer verfügbar
Werte im Kalorienbedarfsrechner können eingetragen und gespeichert werden
Gespeicherte Werte bleiben nach dem Neuladen erhalten

**Testergebnis:**
Statistikbereich ist verfügbar
Werte im Kalorienbedarfsrechner können eingetragen und gespeichert werden
Gespeicherte Werte bleiben nach dem Neuladen erhalten

**Status:** Passed

### HOME-010: Gesperrte Statistiken bei Basic
**Voraussetzung:**
Benutzerkonto mit Paket Basic existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Basic-Benutzer anmelden
2. Statistikbereich aufrufen
3. Prüfen, ob die Premium-Statistiken gesperrt sind
4. Versuchen, auf die gesperrten Statistiken zuzugreifen

**Erwartetes Ergebnis:**
Premium-Statistiken sind für Basic-Benutzer gesperrt
Gesperrte Statistiken können nicht aufgerufen werden
Es erfolgt keine Weiterleitung in einen gesperrten Bereich

**Testergebnis:**
Premium-Statistiken sind für Basic-Benutzer gesperrt
Gesperrte Statistiken können nicht aufgerufen werden
Es erfolgt keine Weiterleitung in einen gesperrten Bereich

**Status:** Passed


### HOME-011: Navigation zur Upgrade-Seite
**Voraussetzung:**
Benutzerkonto existiert
Benutzer ist erfolgreich angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Upgrade-Knopf auf der Homepage anklicken
2. Prüfen, ob die Upgrade-Seite geöffnet wird
3. Upgrade-Seite überprüfen
4. Zurück-Navigation anklicken
5. Prüfen, ob die Homepage / Auswahlseite wieder geöffnet wird

**Erwartetes Ergebnis:**
Upgrade-Knopf ist sichtbar und anklickbar
Upgrade-Seite wird korrekt geöffnet
Verfügbare Pakete werden angezeigt
Zurück-Navigation funktioniert
Homepage / Auswahlseite wird wieder angezeigt

**Testergebnis:**
Upgrade-Knopf funktioniert
Upgrade-Seite wird korrekt geöffnet
Verfügbare Pakete werden angezeigt
Zurück-Navigation funktioniert
Homepage / Auswahlseite wird wieder angezeigt

**Status:** Passed

---------------------------------
##Paketverwaltung / Upgrade
---------------------------------
### PV-001: Upgrade von Basic auf Premium
**Voraussetzung:**
Benutzerkonto mit Paket Basic existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Paket Premium auswählen
2. Upgrade durchführen
3. Prüfen, ob das Upgrade erfolgreich durchgeführt wurde
4. Prüfen, ob das Benutzerkonto jetzt Premium besitzt
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob Premium-Funktionen freigeschaltet sind

**Erwartetes Ergebnis:**
Upgrade auf Premium wird erfolgreich durchgeführt
Benutzerkonto erhält das Paket Premium
Premium-Funktionen sind freigeschaltet
Premium+-Funktionen bleiben gesperrt

**Testergebnis:**
Benutzerkonto erhält das Paket Premium
Premium- Funktionen sind freigeschaltet
Premium+ Funktionen bleiben gesperrt

**Status:** Passed

### PV-002: Upgrade von Basic auf Premium+
**Voraussetzung:**
Benutzerkonto mit Paket Basic existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Paket Premium+ auswählen
2. Upgrade durchführen
3. Prüfen, ob das Upgrade erfolgreich durchgeführt wurde
4. Prüfen, ob das Benutzerkonto jetzt Premium+ besitzt
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob Premium- und Premium+-Funktionen freigeschaltet sind

**Erwartetes Ergebnis:**
Upgrade auf Premium+ wird erfolgreich durchgeführt
Benutzerkonto erhält das Paket Premium+
Premium-Funktionen sind freigeschaltet
Premium+-Funktionen sind freigeschaltet

**Testergebnis:**
Benutzerkonto besitzt jetzt das Paket Premium+
Premium-Funktionen sind freigeschaltet
Premium+-Funktionen sind freigeschaltet

**Status:** Passed


### PV-003: Upgrade von Premium auf Premium+
**Voraussetzung:**
Benutzerkonto mit Paket Premium existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Paket Premium+ auswählen
2. Upgrade durchführen
3. Prüfen, ob das Upgrade erfolgreich durchgeführt wurde
4. Prüfen, ob das Benutzerkonto jetzt Premium+ besitzt
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob Premium+-Funktionen freigeschaltet sind

**Erwartetes Ergebnis:**
Upgrade auf Premium+ wird erfolgreich durchgeführt
Benutzerkonto erhält das Paket Premium+
Premium-Funktionen bleiben freigeschaltet
Premium+-Funktionen sind freigeschaltet

**Testergebnis:**
Benutzerkonto besitzt jetzt das Paket Premium+
Premium-Funktionen bleiben freigeschaltet
Premium+-Funktionen sind freigeschaltet

**Status:** Passed

### PV-004: Downgrade von Premium+ auf Premium
**Voraussetzung:**
Benutzerkonto mit Paket Premium+ existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Paket Premium auswählen
2. Downgrade durchführen
3. Prüfen, ob das Downgrade erfolgreich durchgeführt wurde
4. Prüfen, ob das Benutzerkonto jetzt Premium besitzt
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob Premium+-Funktionen gesperrt sind

**Erwartetes Ergebnis:**
Downgrade auf Premium wird erfolgreich durchgeführt
Benutzerkonto erhält das Paket Premium
Premium-Funktionen bleiben freigeschaltet
Premium+-Funktionen sind gesperrt

**Testergebnis:**
Benutzerkonto besitzt jetzt das Paket Premium
Premium-Funktionen bleiben freigeschaltet
Premium+-Funktionen sind gesperrt

**Status:** Passed

### PV-005: Downgrade von Premium+ auf Basic
**Voraussetzung:**
Benutzerkonto mit Paket Premium+ existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Paket Basic auswählen
2. Downgrade durchführen
3. Prüfen, ob das Downgrade erfolgreich durchgeführt wurde
4. Prüfen, ob das Benutzerkonto jetzt Basic besitzt
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob Premium- und Premium+-Funktionen gesperrt sind

**Erwartetes Ergebnis:**
Downgrade auf Basic wird erfolgreich durchgeführt
Benutzerkonto erhält das Paket Basic
Basic-Funktionen bleiben verfügbar
Premium- und Premium+-Funktionen sind gesperrt

**Testergebnis:**
Benutzerkonto besitzt jetzt das Paket Basic
Basic-Funktionen bleiben verfügbar
Premium- und Premium+-Funktionen sind gesperrt

**Status:** Passed

### PV-006: Downgrade von Premium auf Basic
**Voraussetzung:**
Benutzerkonto mit Paket Premium existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Paket Basic auswählen
2. Downgrade durchführen
3. Prüfen, ob das Downgrade erfolgreich durchgeführt wurde
4. Prüfen, ob das Benutzerkonto jetzt Basic besitzt
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob Premium-Funktionen gesperrt sind

**Erwartetes Ergebnis:**
Downgrade auf Basic wird erfolgreich durchgeführt
Benutzerkonto erhält das Paket Basic
Basic-Funktionen bleiben verfügbar
Premium- und Premium+-Funktionen sind gesperrt

**Testergebnis:**
Benutzerkonto besitzt jetzt das Paket Basic
Basic-Funktionen bleiben verfügbar
Premium- und Premium+-Funktionen sind gesperrt

**Status:** Passed

### PV-007: Freigeschaltete Funktionen nach Upgrade prüfen
**Voraussetzung:**
Benutzerkonto mit Paket Basic existiert
Benutzer ist angemeldet
Upgrade auf Premium oder Premium+ wurde durchgeführt

**Testschritte:**
1. Nach dem Upgrade die Homepage / Auswahlseite öffnen
2. Alle Funktionen des neuen Pakets kontrollieren
3. Freigeschaltete Bereiche öffnen
4. Prüfen, ob die Funktionen erreichbar und nutzbar sind

**Erwartetes Ergebnis:**
Alle Funktionen des neuen Pakets sind freigeschaltet
Die freigeschalteten Bereiche können geöffnet werden
Die Funktionen können genutzt werden

**Testergebnis:**
Alle Funktionen des neuen Pakets sind freigeschaltet
Die freigeschalteten Bereiche können geöffnet werden
Die Funktionen können genutzt werden

**Status:** passed

### PV-008: Gesperrte Funktionen ohne entsprechendes Paket prüfen
**Voraussetzung:**
Benutzerkonto mit Paket Basic oder Premium existiert
Benutzer ist angemeldet
Homepage / Auswahlseite ist geöffnet

**Testschritte:**
1. Homepage / Auswahlseite öffnen
2. Funktionen kontrollieren, die nicht im aktuellen Paket enthalten sind
3. Versuchen, gesperrte Bereiche anzuklicken
4. Prüfen, ob ein direkter Zugriff auf gesperrte Bereiche möglich ist

**Erwartetes Ergebnis:**
Funktionen ohne entsprechende Paketberechtigung sind gesperrt
Gesperrte Bereiche können nicht geöffnet werden
Ein Zugriff auf gesperrte Funktionen ist nicht möglich

**Testergebnis:**
Funktionen ohne entsprechende Paketberechtigung sind gesperrt
Gesperrte Bereiche können nicht geöffnet werden
Ein Zugriff auf gesperrte Funktionen ist nicht möglich

**Status:** Passed

### PV-009: Upgrade ohne gültige Paketauswahl
**Voraussetzung:**
Benutzerkonto mit Paket Basic oder Premium existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Upgrade-Seite öffnen
2. Kein Paket auswählen
3. Upgrade bestätigen beziehungsweise versuchen, das Upgrade durchzuführen
4. Prüfen, ob eine Fehlermeldung angezeigt wird
5. Prüfen, ob das bisherige Paket unverändert bleibt

**Erwartetes Ergebnis:**
Upgrade ohne gültige Paketauswahl wird verhindert
Eine entsprechende Fehlermeldung wird angezeigt
Das bisherige Paket bleibt unverändert

**Testergebnis:**
Upgrade ohne gültige Paketauswahl wird verhindert
Eine entsprechende Fehlermeldung wird angezeigt
Das bisherige Paket bleibt unverändert

**Status:** Passed

### PV-010: Paket bleibt nach erneutem Login erhalten
**Voraussetzung:**
Benutzerkonto mit einem beliebigen Paket existiert
Benutzer ist angemeldet

**Testschritte:**
1. Aktuelles Paket des Benutzerkontos überprüfen
2. Benutzer abmelden
3. Erneut mit demselben Benutzerkonto anmelden
4. Homepage / Auswahlseite öffnen
5. Prüfen, ob weiterhin das gleiche Paket zugewiesen ist
6. Prüfen, ob die entsprechenden Funktionen freigeschaltet sind

**Erwartetes Ergebnis:**
Das Benutzerkonto behält sein bisheriges Paket
Das Paket wird nach erneutem Login korrekt angezeigt
Die entsprechenden Funktionen sind weiterhin freigeschaltet

**Testergebnis:**
Das Benutzerkonto behält sein bisheriges Paket
Das Paket wird nach erneutem Login korrekt angezeigt
Die entsprechenden Funktionen sind weiterhin freigeschaltet

**Status:** Passed

### PV-011: Paket bleibt nach Upgrade und erneutem Login erhalten
**Voraussetzung:**
Benutzerkonto mit Paket Basic oder Premium existiert
Benutzer ist angemeldet
Upgrade-Seite ist geöffnet

**Testschritte:**
1. Ein Upgrade auf ein höheres Paket durchführen
2. Prüfen, ob das neue Paket übernommen wurde
3. Benutzer abmelden
4. Erneut mit demselben Benutzerkonto anmelden
5. Homepage / Auswahlseite öffnen
6. Prüfen, ob das neue Paket weiterhin zugewiesen ist
7. Prüfen, ob die entsprechenden Funktionen freigeschaltet sind

**Erwartetes Ergebnis:**
Upgrade wird erfolgreich durchgeführt
Das neue Paket wird dauerhaft übernommen
Das neue Paket bleibt nach erneutem Login erhalten
Die entsprechenden Funktionen sind weiterhin freigeschaltet

**Testergebnis:**
Upgrade erfolgreich durchgeführt
Das neue Paket wird dauerhaft übernommen
Das neue Paket bleibt nach erneutem Login erhalten
Die entsprechenden Funktionen sind weiterhin freigeschaltet

**Status:** Passed

-------------------------
##Trainingspläne
-------------------------
### TR-001 Trainingsplan erstellen
**Voraussetzung:**
Benutzer ist angemeldet
create-workout-Seite ist geöffnet

**Testschritte:**
1. Einen neuen Trainingsplan erstellen
2. Trainingsplan Bennen
3. 1 bis 2 Übungen reinmachen
4. Trainingsplan speichern

**Erwartetes Ergebnis:**
Trainingsplan wird erfolgreich erstellt
Trainingsplan wird in der Übersicht angezeigt

**Testergebnis:**
Trainingsplan erfolgreich erstellt
Trainingsplan wird in der Übersicht angezeigt

**Status:** Passed


### TR-002: Trainingsplan bearbeiten
**Voraussetzung:**
Ein Trainingsplan existiert
Benutzer ist angemeldet

**Testschritte:**
1. Einen bestehenden Trainingsplan auswählen
2. Trainigsplan bearbeiten drücken (✏️)
3. Den Namen des Trainingsplans ändern
4. Änderungen speichern

**Erwartetes Ergebnis:**
Aktualisierungsmeldung „Trainingsplan aktualisiert!“ wird angezeigt
Trainingsplan wird erfolgreich aktualisiert
Weiterleitung zur workouts-Seite erfolgt
Neuer Name wird in der Übersicht angezeigt

**Testergebnis:**
Aktualisierungsmeldung "Trainingsplan aktualisiert!" wird angezeigt
Trainingsplan wird erfolgreich aktualisiert
Neuer Name wird in der Übersicht angezeigt

**Status:** Passed

### TR-003: Trainingsplan löschen
**Voraussetzung:**
Ein Trainingsplan existiert
Benutzer ist angemeldet

**Testschritte:**
1. Workouts-Seite öffnen
2. Einen bestehenden Trainingsplan auswählen (X-Button drücken)
3. Trainingsplan löschen
4. Übersicht prüfen

**Erwartetes Ergebnis:**
Pop um message Möchtest du den Traingsplan""wirklich löschen? Bestätigen
Trainingsplan wird erfolgreich gelöscht
Der gelöschte Trainingsplan wird nicht mehr in der Übersicht angezeigt

**Testergebnis:**
Pop um message Möchtest du den Traingsplan""wirklich löschen? Bestätigen
Trainingsplan erfolgreich gelöscht
Trainingsplan wird nicht mehr in der Übersicht angezeigt

**Status:** Passed

### TR-004: Übungen hinzufügen
**Voraussetzung:**
Ein Trainingsplan existiert
Benutzer ist angemeldet

**Testschritte:**
1. Einen bestehenden Trainingsplan auswählen
2. Trainingsplan per ✏️-Knopf bearbeiten
3. Eine neue Übung hinzufügen
4. Änderungen speichern
5. Übersicht prüfen

**Erwartetes Ergebnis:**
Aktualisierungsmeldung "Trainingsplan aktualisiert!" wird angezeigt
Weiterleitung zur workouts-Seite erfolgt
Übung wird erfolgreich zum Trainingsplan hinzugefügt
Übung wird im Trainingsplan angezeigt

**Testergebnis:**
Aktualisierungsmeldung "Trainingsplan aktualisiert!" wird angezeigt
Übung erfolgreich hinzugefügt
Übung wird im Trainingsplan angezeigt

**Status:** Passed

### TR-005: Übungen entfernen
**Voraussetzung:**
Ein Trainingsplan mit mindestens einer Übung existiert
Benutzer ist angemeldet

**Testschritte:**
1. Workouts-Seite über den Trainingspläne-Knopf öffnen
2. Einen Trainingsplan zum Bearbeiten auswählen (✏️)
3. Eine vorhandene Übung entfernen
4. Änderungen speichern
5. Übersicht prüfen

**Erwartetes Ergebnis:**
Pop up massage "Trainingsplan aktualisiert" bestatigen
In workouts weitergeleitet werden
Ausgewählte Übung wird aus dem Trainingsplan entfernt
Übrige Übungen bleiben im Trainingsplan erhalten

**Testergebnis:**
Aktualisierungsmeldung "Trainingsplan aktualisiert!" wird angezeigt
Übung erfolgreich entfernt
Übrige Übungen bleiben im Trainingsplan erhalten

**Status:** Passed


### TR-006: Trainingsplan mit leerem Namen erstellen
**Voraussetzung:**
Benutzer ist angemeldet
Workout-Seite ist geöffnet

**Testschritte:**
1. Einen neuen Trainingsplan erstellen
2. Das Namensfeld leer lassen
3. Speichern versuchen

**Erwartetes Ergebnis:**
Trainingsplan wird nicht erstellt
Eine entsprechende Fehlermeldung wird angezeigt

**Testergebnis:**
Leere Trainingsplannamen werden verhindert
Auch Eingaben, die nur aus Leerzeichen bestehen, werden abgelehnt
Bei einem leeren Eingabefeld wird eine entsprechende Fehlermeldung angezeigt
Die Erstellung mit einem gültigen Namen funktioniert weiterhin

**Status:** Passed

### TR-007: Trainingsplan ohne Übungsangaben erstellen
**Voraussetzung:**
Benutzer ist angemeldet
Workout-Seite ist geöffnet

**Testschritte:**
1. Einen neuen Trainingsplan erstellen
2. Einen Trainingsplannamen eingeben
3. Keine Übungen hinzufügen
4. Trainingsplan speichern

**Erwartetes Ergebnis:**
Trainingsplan wird erfolgreich erstellt und gespeichert
Der Trainingsplan wird in der Übersicht angezeigt
Es werden keine Übungen gespeichert

**Testergebnis:**
Leerer Traingsplan wird erstellt

**Status:** Passed

### TR-008: Übung ohne vollständige Angaben speichern
**Voraussetzung:**
Benutzer ist angemeldet
Workout-Seite ist geöffnet

**Testschritte:**
1. Einen neuen Trainingsplan erstellen
2. Einen Trainingsplannamen eingeben
3. Eine Übung hinzufügen
4. Sätze, Wiederholungen und Gewicht leer lassen
5. Trainingsplan speichern

**Erwartetes Ergebnis:**
Trainingsplan wird nicht gespeichert
Eine entsprechende Fehlermeldung wird angezeigt
Fehlende Übungsangaben werden erkannt

**Testergebnis:**
Trainingsplan wird nicht gespeichert
Eine Fehlermeldung wird angezeigt wenn die Übungsangaben fehlen

**Status:** Passed

### TR-0019: Trainingsplan mit mehreren Übungen erstellen
**Voraussetzung:**
Benutzer ist angemeldet
Fitness-Seite ist geöffnet

**Testschritte:**
1. Einen neuen Trainingsplan erstellen
2. Einen gültigen Namen eingeben
3. Mehrere Übungen hinzufügen
4. Trainingsplan speichern

**Erwartetes Ergebnis:**
Trainingsplan wird erfolgreich erstellt
Alle hinzugefügten Übungen werden dem Trainingsplan zugeordnet und angezeigt

**Testergebnis:**
Trainingsplan erfolgreich erstellt
Alle hinzugefügten Übungen werden korrekt angezeigt

**Status:** Passed


### TR-0010: Training starten
**Voraussetzung:**
Ein Trainingsplan mit mindestens einer Übung existiert in Workouts
Benutzer ist angemeldet

**Testschritte:**
1. Einen Trainingsplan auswählen
2. Training starten per Startknopf "▶️"

**Erwartetes Ergebnis:**
Training wird erfolgreich gestartet
Übungen des ausgewählten Trainingsplans werden angezeigt

**Testergebnis:**
Training erfolgreich gestartet
Übungen werden korrekt angezeigt

**Status:** Passed

### TR-011: Training abschließen
**Voraussetzung:**
Benutzer ist angemeldet
Ein Trainingsplan mit mindestens einer Übung existiert

**Testschritte:**
1. Ein Training starten per Startknopf "▶️" starten
2. Trainigsplan starten knopf drücken
3. Übungen per "Next" knopf durchegehen
4. Training abschließen

**Erwartetes Ergebnis:**
Trainigstimer fangt nach knopfdruck an hochzuzählen
Workout-Fortschirttsbalken füllt sich nach jedem mal "Next" drücken einen teil grün
Training wird erfolgreich abgeschlossen
Trainingsansicht wird entsprechend aktualisiert
Workout geschaffts erfolgs meldung mit Trainingszeit und Satz anzahl
Nach Workout geschfts meldung zuruck in selection/hompage geleitet werden,Statistiken ändern sich

**Testergebnis:**
Trainigstimer fangt nach knopfdruck an hochzuzählen
Workout-Fortschirttsbalken füllt sich nach jedem mal "Next" drücken einen teil grün
Training wird erfolgreich abgeschlossen
Trainingsansicht wird entsprechend aktualisiert
Workout geschaffts erfolgs meldung mit Trainingszeit und Satz anzahl
Nach Workout geschfts meldung zuruck in selection/hompage geleitet werden,Statistiken ändern sich

**Status:** Passed

### TR-012: Trainingszeit / Timer prüfen
**Voraussetzung:**
Ein Trainingsplan existiert
Benutzer ist angemeldet

**Testschritte:**
1. Ein Training starten
2. Timer per knopfdruck starten
3. Timer beobachten
4. Einige Sekunden warten
5. Timer erneut prüfen 

**Erwartetes Ergebnis:**
Timer startet beim Knopfdruck
Trainingszeit wird fortlaufend angezeigt

**Testergebnis:**
Timer startet korrekt
Trainingszeit wird fortlaufend angezeigt

**Status:** Passed

### TR-013: Abgeschlossenes Training in Statistiken speichern
**Voraussetzung:**
Benutzer ist angemeldet
Ein Training wurde gestartet
Trainigsplan wurde beendet

**Testschritte:**
1. Ein Training durchführen
2. Training abschließen
3. Prüfen, ob das abgeschlossene Training in Statistik gespeichert wurde

**Erwartetes Ergebnis:**
Abgeschlossenes Training wird erfolgreich in Statistik gespeichert
Trainingseinheit wird bei den gespeicherten Trainingseinheiten angezeigt

**Testergebnis:**
Training erfolgreich in Statistik gespeichert
Trainingseinheit wird bei den gespeicherten Trainingseinheiten angezeigt

**Status:** Passed

### TR-014: Abgeschlossene Trainingseinheiten aufrufen
**Voraussetzung:**
Mindestens eine abgeschlossene Trainingseinheit wurde gespeichert
Benutzer ist angemeldet

**Testschritte:**
1. Gespeicherte Trainingseinheiten öffnen
2. Eine vorhandene Trainingseinheit auswählen
3. Gespeicherte Trainingsdaten prüfen

**Erwartetes Ergebnis:**
Gespeicherte Trainingseinheit kann erneut aufgerufen werden
Gespeicherte Trainingsdaten werden korrekt angezeigt

**Testergebnis:**
Trainingseinheit erfolgreich aufgerufen
Gespeicherte Trainingsdaten werden korrekt angezeigt

**Status:** Passed

### TR-015: Trainingsplan nach erneutem Login weiterhin vorhanden
**Voraussetzung:**
Ein Trainingsplan wurde erstellt
Benutzer ist angemeldet

**Testschritte:**
1. Benutzer abmelden
2. Erneut mit demselben Benutzerkonto anmelden
3. Workout-Seite öffnen
4. Prüfen, ob der zuvor erstellte Trainingsplan weiterhin vorhanden ist

**Erwartetes Ergebnis:**
Trainingsplan ist nach erneutem Login weiterhin vorhanden
Zugehörige Übungen werden weiterhin angezeigt

**Testergebnis:**
Trainingsplan ist nach erneutem Login weiterhin vorhanden
Zugehörige Übungen werden korrekt angezeigt

**Status:** Passed

-------------------
## Ernährung
-------------------
### ER-001: Kalorienrechner mit gültigen Werten testen
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Kalorienbedarfsrechner ist geöffnet

**Testschritte:**
1. Kalorienbedarfsrechner öffnen
2. Werte eingeben
3. Aktivitätslevel und Ziel auswählen
4. Auf den Button „Kalorienbedarfsrechner“ klicken

**Erwartetes Ergebnis:**
Kalorienziel wird berechnet und angezeigt
Kalorienziel und Proteinziel werden übernommen
Beide Werte werden in der Statistik angezeigt

**Testergebnis:**
Kalorienziel wird berechnet und angezeigt
Kalorienziel und Proteinziel werden übernommen
Beide Werte werden in der Statistik angezeigt

**Status:** Passed

### ER-002: Kalorienrechner nach ausloggen noch erhalten
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Kalorienbedarfsrechner wurde für den Benutzer bereits ausgefüllt

**Testschritte:**
1. Ausloggen 
2. Erneut einloggen 
3. Statistik überprüfen (Werte)
4. Nutrition-Seite öffnen und Kalorienziel sowie Proteinziel überprüfen

**Erwartetes Ergebnis:**
Kalorienziel ist weiterhin angegeben
Proteinziel ist weiterhin angegeben
Statistik zeigt weiterhin die gespeicherten Werte an

**Testergebnis:**
Kalorienziel ist weiterhin angegeben
Proteinziel ist weiterhin angegeben
Statistik zeigt weiterhin die gespeicherten Werte an

**Status:** Passed

### ER-003: Kalorienrechner mit neuen Werten aktualisieren
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Kalorienbedarfsrechner wurde für den Benutzer bereits ausgefüllt

**Testschritte:**
1. Kalorienbedarfsrechner öffnen
2. Neue Werte eingeben
3. Aktivitätslevel und Ziel ändern
4. Auf den Button „Kalorienbedarfsrechner“ klicken
5. Statistik überprüfen

**Erwartetes Ergebnis:**
Kalorienziel wird mit den neuen Werten berechnet
Neues Kalorienziel und Proteinziel werden übernommen
Beide Werte werden in der Statistik aktualisiert

**Testergebnis:**
Kalorienziel wird mit den neuen Werten berechnet
Neues Kalorienziel und Proteinziel werden übernommen
Beide Werte werden in der Statistik aktualisiert

**Status:** Passed

### ER-004: Kalorienrechner mit ungültigen Werten testen
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Kalorienbedarfsrechner ist geöffnet

**Testschritte:**
1. Ungültige Werte eingeben (z. B. Buchstaben)
2. Aktivitätslevel und Ziel auswählen
3. Auf den Button „Kalorienbedarfsrechner“ klicken

**Erwartetes Ergebnis:**
Ungültige Eingaben werden erkannt
Kalorienziel wird nicht berechnet
Eine entsprechende Fehlermeldung wird angezeigt

**Testergebnis:**
Buchstabeneingabe ist nicht möglich
Kalorienziel wird nicht berechnet
Fehlermeldung: "Füllen Sie dieses Feld aus"

**Status:** Passed


### ER-005: Kalorienrechner mit Punkt als Dezimaltrennzeichen testen (Gewicht in kg)
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Kalorienbedarfsrechner ist geöffnet

**Testschritte:**
1. Einen Wert mit Punkt als Dezimaltrennzeichen eingeben (z. B. 75.5 (kg))
2. Weitere erforderliche Werte eingeben
3. Aktivitätslevel und Ziel auswählen
4. Auf den Button „Kalorienbedarfsrechner“ klicken

**Erwartetes Ergebnis:**
Eingabe mit Punkt wird korrekt verarbeitet
Kalorienziel wird berechnet und angezeigt
Kalorienziel und Proteinziel werden übernommen

**Testergebnis:**
Eingabe mit Punkt wird korrekt verarbeitet
Kalorienziel wird berechnet und angezeigt
Kalorienziel und Proteinziel werden übernommen

**Status:** Passed


### ER-006: Kalorienrechner mit Komma als Dezimaltrennzeichen testen (Gewicht in kg)
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Kalorienbedarfsrechner ist geöffnet

**Testschritte:**
1. Einen Wert mit Komma als Dezimaltrennzeichen eingeben (z. B. 75,5 (kg))
2. Weitere erforderliche Werte eingeben
3. Aktivitätslevel und Ziel auswählen
4. Auf den Button „Kalorienbedarfsrechner“ klicken

**Erwartetes Ergebnis:**
Eingabe mit Komma wird korrekt verarbeitet
Kalorienziel wird berechnet und angezeigt
Kalorienziel und Proteinziel werden übernommen

**Testergebnis:**
Eingabe mit Komma wird korrekt verarbeitet
Kalorienziel wird berechnet und angezeigt
Kalorienziel und Proteinziel werden übernommen

**Status:** Passed


### ER-007: Lebensmittel suchen
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Lebensmittel-Suchfunktion ist erreichbar

**Testschritte:**
1. Lebensmittel-hinzufügen-Button drücken
2. Ein Lebensmittel in das Suchfeld eingeben
3. Suche starten
4. Suchergebnisse überprüfen

**Erwartetes Ergebnis:**
Passende Lebensmittel werden gesucht
Suchergebnisse werden angezeigt
Die Lebensmittelinformationen werden korrekt dargestellt

**Testergebnis:**
Passende Lebensmittel werden gesucht
Suchergebnisse werden angezeigt
Die Lebensmittelinformationen werden korrekt dargestellt

**Status:** Passed


### ER-008: Lebensmittel hinzufügen (Prüfen bei Frühstück,Mittagessen,Abendessen,Snacks)
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Ein Lebensmittel wurde erfolgreich gesucht

**Testschritte:**
1. Ein Lebensmittel auswählen
2. Gewünschte Menge eingeben
3. Mahlzeit auswählen
4. Lebensmittel hinzufügen knopf betätigen
5. Eintrag überprüfen

**Erwartetes Ergebnis:**
Lebensmittel wird erfolgreich hinzugefügt
Lebensmittel wird in der ausgewählten Mahlzeit angezeigt
Kalorien und Proteine werden korrekt übernommen
Anzeigebalken übernehmen den Eintrag 
Info kreis details übernehmen den Eintrag 

**Testergebnis:**
Lebensmittel wird erfolgreich hinzugefügt
Lebensmittel wird in der ausgewählten Mahlzeit angezeigt
Kalorien und Proteine werden korrekt übernommen
Anzeigebalken übernehmen den Eintrag 
Info kreis details übernehmen den Eintrag 

**Status:** Passed


### ER-009: Lebensmittel löschen
**Voraussetzung:**
Benutzer ist angemeldet
Nutrition-Seite ist erreichbar
Mindestens ein Lebensmittel wurde hinzugefügt

**Testschritte:**
1. Ein gespeichertes Lebensmittel auswählen
2. Löschfunktion betätigen
3. Eintrag überprüfen

**Erwartetes Ergebnis:**
Pop up :"Möchtest du [Lebensmittelname] wirklich löschen?"
Lebensmittel wird erfolgreich gelöscht
Lebensmittel wird nicht mehr in der Mahlzeit angezeigt
Kalorien und Proteine werden entsprechend aktualisiert

**Testergebnis:**
Pop up :"Möchtest du [Lebensmittelname] wirklich löschen?"
Lebensmittel wird erfolgreich gelöscht
Lebensmittel wird nicht mehr in der Mahlzeit angezeigt
Kalorien und Proteine werden entsprechend aktualisiert

**Status:** Passed 

### ER-010: Eigenes Lebensmittel erstellen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar

**Testschritte:**
1. Funktion zum Erstellen eigener Lebensmittel per Knopf öffnen
2. Namen für das Lebensmittel eingeben (test)
3. Erforderliche Nährwertangaben eingeben (z. B. Kalorien und Proteine)
4. Eigenes Lebensmittel speichern

**Erwartetes Ergebnis:**
Eine entsprechende Erfolgsmeldung wird angezeigt :"Eigenes Lebensmittel erfolgreich gespeichert!"
Eigenes Lebensmittel wird erfolgreich erstellt  
Lebensmittel wird gespeichert

**Testergebnis:**
Eine entsprechende Erfolgsmeldung wird angezeigt :"Eigenes Lebensmittel erfolgreich gespeichert!"
Eigenes Lebensmittel wird erfolgreich erstellt  
Lebensmittel wird gespeichert

**Status:** Passed

### ER-011: Eigenes Lebensmittel suchen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Mindestens ein eigenes Lebensmittel wurde erstellt

**Testschritte:**
1. Funktion „Lebensmittel hinzufügen“ öffnen
2. Namen des eigenen Lebensmittels in das Suchfeld eingeben (test)
3. Suche starten
4. Suchergebnisse überprüfen

**Erwartetes Ergebnis:**
Eigenes Lebensmittel wird gefunden  
Passende Suchergebnisse werden angezeigt  
Gespeicherte Nährwertangaben werden korrekt dargestellt
Gespeicherte Nährwertangaben werden korrekt in der Info angezeigt

**Testergebnis:**
Eigenes Lebensmittel wird gefunden  
Passende Suchergebnisse werden angezeigt  
Gespeicherte Nährwertangaben werden korrekt dargestellt
Gespeicherte Nährwertangaben werden korrekt in der Info angezeigt

**Status:** Passed

### ER-012: Eigenes Lebensmittel hinzufügen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Mindestens ein eigenes Lebensmittel wurde erstellt und gesucht

**Testschritte:**
1. Eigenes Lebensmittel aus den Suchergebnissen auswählen
2. Lebensmittelname auswahlen
3. Lebensmittel werte einfügen
4. Lebensmittel hinzufügen
5. Eintrag überprüfen

**Erwartetes Ergebnis:**
Eigenes Lebensmittel wird erfolgreich hinzugefügt  
Lebensmittel wird in der ausgewählten Mahlzeit angezeigt  
Kalorien und Proteine werden korrekt übernommen  
Anzeigebalken übernehmen den Eintrag  
Info-Kreis-Details übernehmen den Eintrag

**Testergebnis:**
Eigenes Lebensmittel wird erfolgreich hinzugefügt  
Lebensmittel wird in der ausgewählten Mahlzeit angezeigt  
Kalorien und Proteine werden korrekt übernommen  
Anzeigebalken übernehmen den Eintrag  
Info-Kreis-Details übernehmen den Eintrag

**Status:** Passed

### ER-013: Eigenes Lebensmittel löschen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Mindestens ein eigenes Lebensmittel wurde erstellt

**Testschritte:**
1. Eigenes Lebensmittel auswählen
2. Löschfunktion betätigen
3. Löschvorgang bestätigen

**Erwartetes Ergebnis:**
Pop-up mit einer entsprechenden Löschbestätigung wird angezeigt :"Möchtest du test wirklich löschen?"
Eigenes Lebensmittel wird erfolgreich gelöscht  

**Testergebnis:**
Pop-up mit einer entsprechenden Löschbestätigung wird angezeigt :"Möchtest du test wirklich löschen?"
Eigenes Lebensmittel wird erfolgreich gelöscht  

**Status:** Passed

### ER-014: Lebensmittelmenge ändern
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Mindestens ein Lebensmittel wurde zu einer Mahlzeit hinzugefügt

**Testschritte:**
1. Gespeichertes Lebensmittel auswählen  (Bearbeiten Button)
2. Menge ändern
3. Änderung speichern bzw. bestätigen
4. Nährwertangaben überprüfen

**Erwartetes Ergebnis:**
Neue Lebensmittelmenge wird übernommen  
Kalorien und Proteine werden entsprechend der neuen Menge angepasst  
Anzeigebalken und Info-Kreis-Details werden aktualisiert

**Testergebnis:**
Neue Lebensmittelmenge wird übernommen  
Kalorien und Proteine werden entsprechend der neuen Menge angepasst  
Anzeigebalken und Info-Kreis-Details werden aktualisiert

**Status:** Passed

### ER-015: Vergangene Tage aufrufen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Für mindestens einen vergangenen Tag wurden Lebensmittel gespeichert

**Testschritte:**
1. Nutrition-Seite öffnen
2. Einen vergangenen Tag auswählen
3. Gespeicherte Mahlzeiten überprüfen

**Erwartetes Ergebnis:**
Vergangener Tag wird korrekt aufgerufen  
Gespeicherte Mahlzeiten des ausgewählten Tages werden angezeigt  
Kalorien und Proteine werden korrekt dargestellt

**Testergebnis:**

**Status:** Open

### ER-016: Gespeicherte Mahlzeiten nach erneutem Aufruf prüfen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Für den aktuellen Tag wurden bereits mehrere Lebensmittel gespeichert

**Testschritte:**
1. Mehrere Lebensmittel zu unterschiedlichen Mahlzeiten hinzufügen
2. Nutrition-Seite verlassen
3. Nutrition-Seite erneut öffnen
4. Gespeicherte Mahlzeiten überprüfen

**Erwartetes Ergebnis:**
Alle zuvor gespeicherten Lebensmittel sind weiterhin vorhanden  
Lebensmittel befinden sich in den richtigen Mahlzeiten  
Mengen und Nährwertangaben bleiben erhalten

**Testergebnis:**
Alle zuvor gespeicherten Lebensmittel sind weiterhin vorhanden  
Lebensmittel befinden sich in den richtigen Mahlzeiten  
Mengen und Nährwertangaben bleiben erhalten

**Status:** Passed

### ER-017: Gespeicherte Lebensmittel nach erneutem Login prüfen
**Voraussetzung:**
Benutzer ist angemeldet  
Mindestens ein Lebensmittel wurde gespeichert

**Testschritte:**
1. Lebensmittel zu einer Mahlzeit hinzufügen
2. Ausloggen
3. Erneut mit demselben Benutzerkonto einloggen
4. Nutrition-Seite öffnen
5. Gespeicherte Lebensmittel überprüfen

**Erwartetes Ergebnis:**
Gespeicherte Lebensmittel sind weiterhin vorhanden  
Lebensmittel werden den richtigen Mahlzeiten zugeordnet  
Mengen und Nährwertangaben bleiben erhalten

**Testergebnis:**
Gespeicherte Lebensmittel sind weiterhin vorhanden  
Lebensmittel werden den richtigen Mahlzeiten zugeordnet  
Mengen und Nährwertangaben bleiben erhalten

**Status:** Passed

### ER-018: Kalorien- und Proteinwerte korrekt berechnen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Mindestens ein Lebensmittel mit bekannten Nährwertangaben ist vorhanden

**Testschritte:**
1. Ein Lebensmittel mit bekannten Kalorien- und Proteinwerten auswählen
2. Eine bestimmte Menge eingeben
3. Lebensmittel hinzufügen
4. Angezeigte Kalorien und Proteine überprüfen
5. Weitere Lebensmittel hinzufügen
6. Gesamtwerte überprüfen

**Erwartetes Ergebnis:**
Kalorien werden entsprechend der eingegebenen Menge berechnet  
Proteine werden entsprechend der eingegebenen Menge berechnet  
Gesamtwerte berücksichtigen alle hinzugefügten Lebensmittel  
Berechnungen und Anzeigen stimmen mit den erwarteten Werten überein

**Testergebnis:**
Kalorien werden entsprechend der eingegebenen Menge berechnet  
Proteine werden entsprechend der eingegebenen Menge berechnet  
Gesamtwerte berücksichtigen alle hinzugefügten Lebensmittel  
Berechnungen und Anzeigen stimmen mit den erwarteten Werten überein

**Status:** Passed

### ER-019: Tagesziele und Fortschrittsanzeige prüfen
**Voraussetzung:**
Benutzer ist angemeldet  
Nutrition-Seite ist erreichbar  
Kalorienziel und Proteinziel wurden bereits festgelegt

**Testschritte:**
1. Nutrition-Seite öffnen
2. Aktuelle Tagesziele überprüfen
3. Lebensmittel mit bekannten Nährwertangaben hinzufügen
4. Fortschrittsanzeigen überprüfen
5. Weitere Lebensmittel hinzufügen und Veränderungen kontrollieren

**Erwartetes Ergebnis:**
Kalorienziel wird korrekt angezeigt  
Proteinziel wird korrekt angezeigt  
Fortschrittsanzeige berücksichtigt die aufgenommenen Kalorien und Proteine  
Fortschrittsanzeige aktualisiert sich nach dem Hinzufügen weiterer Lebensmittel  
Angezeigte Werte stimmen mit den aufgenommenen Mengen überein

**Testergebnis:**
Kalorienziel wird korrekt angezeigt  
Proteinziel wird korrekt angezeigt  
Fortschrittsanzeige berücksichtigt die aufgenommenen Kalorien und Proteine  
Fortschrittsanzeige aktualisiert sich nach dem Hinzufügen weiterer Lebensmittel  
Angezeigte Werte stimmen mit den aufgenommenen Mengen überein

**Status:** Passed

------------
## Rezepte
------------
### RE-001:  Suche ohne Suchbegriff
**Voraussetzung:** 
Benutzer ist angemeldet und befindet sich im Rezeptbereich

**Testschritte:**
1. Rezeptbereich öffnen
2. Suchfeld leer lassen
3. Such-Button drücken

**Erwartetes Ergebnis:** 
Es wird keine Suche ausgeführt und eine entsprechende Meldung angezeigt:"Bitte gib einen Suchbegriff ein"

**Testergebnis:**
Es wird keine Suche ausgeführt und eine entsprechende Meldung angezeigt:"Bitte gib einen Suchbegriff ein"

**Status:** Passed

------------
API
-------------
### RE-002: Rezepte suchen (API)
**Voraussetzung:** 
Benutzer ist angemeldet und befindet sich im Rezeptbereich

**Testschritte:**
1. Einen gültigen Suchbegriff eingeben (z. B. `Hähnchen`)
2. Such-Button drücken

**Erwartetes Ergebnis:** 
Passende Rezepte werden über die API gesucht und in der Ergebnisliste angezeigt mit Bildern

**Testergebnis:**
Passende Rezepte werden über die API gesucht und in der Ergebnisliste angezeigt mit Bildern

**Status:** Passed


### RE-003: Rezeptdetails öffnen (API)
**Voraussetzung:**
Eine Rezeptsuche wurde erfolgreich durchgeführt

**Testschritte:**
1. Ein Rezept aus der Ergebnisliste auswählen
2. Rezeptdetails öffnen

**Erwartetes Ergebnis:** 
Die Details des ausgewählten Rezepts werden geladen und angezeigt

**Testergebnis:**
Die Details des ausgewählten Rezepts werden geladen und angezeigt

**Status:** Passed


### RE-004: Zutaten und Zubereitung anzeigen (API)
**Voraussetzung:** 
Die Details eines Rezepts wurden geöffnet

**Testschritte:**
1. Rezeptdetails öffnen
2. Zutatenliste und Zubereitung überprüfen

**Erwartetes Ergebnis:** 
Die Zutatenliste und die Zubereitungsanleitung des ausgewählten Rezepts werden vollständig angezeigt

**Testergebnis:**
Die Zutatenliste und die Zubereitungsanleitung des ausgewählten Rezepts werden vollständig angezeigt

**Status:** Passed


### RE-005: Zutaten und Zubereitung übersetzt anzeigen (API)
**Voraussetzung:** Die Details eines Rezepts wurden geöffnet.

**Testschritte:**
1. Ein Rezept mit (englischen) Zutaten und Zubereitung öffnen

**Erwartetes Ergebnis:**
Zutaten und Zubereitung werden auf Deutsch übersetzt und verständlich angezeigt

**Testergebnis:**
Zutaten und Zubereitung werden auf Deutsch übersetzt und verständlich angezeigt

**Status:** Passed

----------
## DB
----------
