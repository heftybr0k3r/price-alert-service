from src.common.database import Database
from src.models.alerts.alert import Alert

__author__ = 'Zexx'

Database.initialize()

# Lekérdezzük, hogy mely alert-ek esetében true az active mező értéke -> felesleges lekérés elkerülése

alerts_needing_update = Alert.find_needing_update()

# végig iterálunk

for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()

