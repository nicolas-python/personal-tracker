# QA-Testplan – Personal Tracker

## Testbereiche

## 1. Registrierung
- [x] Registrierung mit gültigen Daten
- [X] Registrierung mit bereits vorhandenem Benutzernamen
- [X] Registrierung mit leerem Passwort
- [X] Registrierung mit leerem Paket auswahl
- [X] Registrierung mit leerem Benutzernamen
- [X] Registrierung mit nicht übereinstimmenden Passwörtern
- [X] Maximale Benutzeranzahl erreicht
- [X] Passwort anzeigen/verbergen testen

## 2. Login
- [X] Login mit korrekten Zugangsdaten
- [X] Login mit falschem Passwort
- [X] Login mit unbekanntem Benutzernamen
- [X] Login ohne Eingabe
- [x] Passwort anzeigen/verbergen testen
- [X] Mehrfach falsche Loginversuche testen
- [ ] Login mit Enter Taste                   (TODO: Funktion implementieren)
- [X] Login mit Leerzeichen im Benutzernamen
- [X] Abmeldung und Zugriffsschutz nach Logout
- [X] Automatischer logout nach 30 min
- [X] Login gleicher benutzer meherer geräte 

## 3.Homepage / Navigation
- [X] Homepage nach erfolgreichem Login anzeigen
- [X] Navigation zu allen verfügbaren Bereichen
- [X] Zurück-Navigation funktioniert
- [X] Gesperrte Bereiche werden angezeigt und sind nicht anklickbar
- [X] Freigeschaltete Bereiche bei Premium
- [X] Freigeschaltete Bereiche bei Premium
- [X] Darstellung auf verschiedenen Bildschirmgrößen prüfen
- [X] Speichern von Statistiken in premium 
- [X] Speichern von Statistiken in premium+
- [X] Gesperrte Statistiken in basic
- [X] Upgrade Knopf funktioniert

## 4. Paketverwaltung / Upgrade
- [X] Upgrade von Basic auf Premium
- [X] Upgrade von Basic auf Premium+
- [X] Upgrade von Premium auf Premium+
- [X] Downgrade von Premium auf Premium+
- [X] Downgrade von Premium+ auf Basic
- [X] Downgrade von Premium auf Basic
- [X] Freigeschaltete Funktionen nach Upgrade prüfen
- [X] Gesperrte Funktionen ohne entsprechendes Paket prüfen
- [X] Upgrade ohne gültige Paketauswahl
- [X] Paket bleibt nach erneutem Login erhalten
- [X] Paket bleibt nach Upgrade und erneutem Login erhalten

## 5. Trainingspläne
- [X] Trainingsplan erstellen
- [X] Trainingsplan bearbeiten
- [X] Trainingsplan löschen
- [X] Übungen hinzufügen
- [X] Übungen entfernen
- [X] Trainingsplan mit leerem Namen erstellen
- [X] Trainingsplan ohne Übungsangaben erstellen
- [X] Übung ohne vollständige Angaben speichern
- [X] Trainingsplan mit mehreren Übungen erstellen
- [X] Training starten
- [X] Training abschließen
- [X] Trainingszeit / Timer prüfen
- [X] Abgeschlossenes Training speichern
- [X] Abgeschlossene Trainingseinheiten aufrufen
- [X] Trainingsplan nach erneutem Login weiterhin vorhanden

## 6. Ernährung
- [X] Kalorienrechner mit gültigen Werten testen
- [X] Kalorienrechner nach ausloggen noch erhalten
- [X] Kalorienrechner updaten neue Werte werden übernommen
- [X] Kalorienrechner mit ungültigen Werten testen
- [X] Kalorien rechner Funktion mit Punkt testen (KG)
- [X] Kalorien rechner Funktion mit Komma testen (KG)
- [X] Lebensmittel suchen
- [X] Lebensmittel hinzufügen
- [X] Lebensmittel löschen
- [ ] Eigenes Lebensmittel erstellen
- [ ] Eigenes Lebensmittel suchen
- [ ] Eigenes Lebensmittel hinzufügen
- [ ] Eigenes Lebensmittel löschen
- [ ] Lebensmittelmenge ändern
- [ ] Mahlzeiten speichern
- [ ] Vergangene Tage aufrufen
- [ ] Gespeicherte Mahlzeiten nach erneutem Aufruf prüfen
- [ ] Gespeicherte Lebensmittel nach erneutem Login weiterhin vorhanden
- [ ] Kalorien- und Proteinwerte korrekt berechnen
- [ ] Tagesziele und Fortschrittsanzeige prüfen

## 7. Rezepte
- [ ] Suche ohne Suchbegriff testen
- [ ] Rezepte suchen (API)
- [ ] Rezeptdetails öffnen (API)
- [ ] Zutaten und Zubereitung anzeigen (API)
- [ ] Zutaten und Zubereitung übersetzung anzeigen (API)

- [ ] Rezepte suchen (DB)
- [ ] Rezeptdetails öffnen (DB)
- [ ] Zutaten und Zubereitung anzeigen (DB)
- [ ] Zutaten und Zubereitung übersetzung anzeigen (DB)
- 
## 8. Tanken
- [ ] Suche mit gültiger PLZ
- [ ] Suche mit ungültiger PLZ
- [ ] Kraftstoffarten wechseln (E5, E10, Diesel)
- [ ] Nach Preis sortieren
- [ ] Nach Entfernung sortieren
- [ ] Tankstellenpreise korrekt anzeigen
- [ ] Entfernung korrekt anzeigen
- [ ] Rechnergebnisse auf korrekte Berechnung prüfen

## 9. Sicherheitstests
- [ ] Passwort-Hashing prüfen
- [ ] SQL-Injection testen
- [ ] Login Rate-Limit prüfen
- [ ] Session-Sicherheit prüfen
- [ ] Zugriffsschutz prüfen
- [ ] CSRF-Schutz prüfen
- [ ] Zugriff auf fremde Benutzerdaten prüfen
- [ ] Maximale Anzahl aktiver Sessions prüfen
- [ ] Ungültige Session-Tokens testen