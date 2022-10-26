from Auth.MQTTPubSession import MQTTPubSession
from DataManager.Temperature import TemperatureManager
from datetime import datetime
import time

#credenziali di accesso
username, password = "", ""
#id del publisher
idPub = "publisher-0001"
#viene generato un singolo publisher
publisher = MQTTPubSession(username,password,idPub)
publisherSession = publisher.creaSessione()

#genero dei dati casuali da inviare ai subscriber per un topic noto
topic = "/iot/user/demo/temperature"


while(1):
    payload = TemperatureManager.generateCelsius()
    info = publisherSession.publish(topic, str(payload))
    info.wait_for_publish()
    print(f'SENT - {datetime.now().strftime("%d/%m%Y %H:%M:%Y")}\tTopic: {topic} Payload: {payload}')
    time.sleep(15)