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


