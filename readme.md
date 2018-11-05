Árértesítő szolgáltatás

A webapp segítségével meghatározott online áruházak esetében adott terméknél az árak automatikus, periodikus ellenőrzésére van lehetőség, majd beállított árlimit elérése esetén értesíti a felhasználót a kedvezményes ár-ról.

Webáruházakat csak az adminisztrátor tudja hozzáadni, szerkeszteni, eltávolítani, a felhasználó a betáplált boltok termékei közül választhat (jelenleg Edigital, iPon, Mall, Xiamoishop, eMag) tetszőleges számút.

A felhasználó regisztrálás után létrehozhat értesítéseket a különböző támogatott webáruházak termékeihez, módosíthatja az értesítési ára(ka)t, letilthatja vagy törölheti az általa létrehozott értesítéseket.

Az értesítések egy e-mail API segítségével kerülnek elküldésre a felhasználó regisztrációkor megadott mail címére.

A webapplikáció különböző technológiák együttesével képes ellátni feladatát: MongoDB mint adatbázis (NoSQL), Python (alap programozási nyelv), Flask (mikro web-szerver), jinja2 (sablonmotor Pythonhoz), Mailgun (sandbox verzió, e-mail-ek küldéséhez, max. 5 recipiens).

In English:

Price alert service web-app

With this webapp you can set up alerts for different items from various shops, then the application on the server checks the current prices, and if the given price equals the setted up limit it sends an e-mail notification to the user.

Only administrator(s) can add, edit or delete webstores from the database. Users can select one or more items from these webstores:
(currently supported): Edigital, Emag, iPon, Mall, Xiaomishop).

After registration the given user can create any number of alerts in the program, can modify the price limits for the selected items, can disable or delete the previously made price alert(s).

The alerts are sent by an e-mail API (provider: MailGun, free tier - restricted to only 5 recipient) to the user's e-mail address.

Involved technologies with which the app was built:

-> MongoDB as the database in the backend,
-> Python as the main programming language,
-> Flask (micro web-server),
-> jinja2 (template engine),
-> MailGun (e-mail API provider).


![Értesítéskérések](readme-files/ertesitesek_git.png)

![Értesítések_részletes](readme-files/ertesitesek_reszletes_git.png)

![Regisztráció](readme-files/regisztracio_git.png)

![Webáruházak](readme-files/webaruhazak_git.png)
