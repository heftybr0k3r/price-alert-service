Árértesítő szolgáltatás

A webapp segítségével meghatározott online áruházak esetében adott terméknél az árak automatikus, periodikus ellenőrzésére van lehetőség, majd beállított limit esetén értesíti a felhasználót a kedvezményes ár-ról.

Webáruházakat csak az adminisztrátor tudja hozzáadni, szerkeszteni, eltávolítani, a felhasználó a betáplált boltok ternékei közül választhat (jelenleg Edigital, iPon, Mall, Xiamoishop, eMag) tetszőleges számút.

A felhasználó regisztrálás után létrehozhat értesítéseket a különböző támogaott webáruházak termékeihez, módsíthatja az értesítési ár(aka)t, letilthatja vagy törölheti az általa létrehozott értesítésket.

Az értesítések egy e-mail API segítségével kerülnek elküldésre a felhasználó regisztrációkor megadott mail címére.

A webapplikáció különböző technológiák együttesével képes ellátni feladatát: MongoDB mint adatbázis (NoSQL), Python (alap programozási nyelv), Flask (mikro web-szerver), jinja2 (sablonmotor Pythonhoz), Mailgun (sandbox verzió, e-mail-ek küldéséhez, max. 5 recipiens).

![Home Screen](readme-files/home.png)

![Sign up Screen](readme-files/signup.png)

![Alerts Screen](readme-files/alerts.png)

![Create Alert Screen](readme-files/create_alert.png)

![Stores Screen](readme-files/stores.png)

![Edit Store Screen](readme-files/edit_store.png)
