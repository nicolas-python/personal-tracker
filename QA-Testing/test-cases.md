## Registrieren
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