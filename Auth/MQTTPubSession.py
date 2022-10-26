import paho.mqtt.client as mqtt
import time
from Auth.ConfigReader import ConfigReader


class MQTTPubSession:
    """La classe gestisce tutti i metodi per il collegamento dei publisher al broker Mosquito.
        E' definita la variabile che contiene il path per il file di configurazione default.

        Sono definiti e configurati i seguenti metodi di CallBack:
        - on_connect
        - on_disconnect"""
    PATH = "Configurations/Publisher/config.json"

    @staticmethod
    def onConnect(client, userdata, flags, rc):
        """Il metodo viene usato per gestire la connessione al broker"""
        print(f'{userdata.__dict__} connection status: {rc}')

    @staticmethod
    def onDisconnect(client, userdata, rc):
        if rc != 0:
            print(f'\n{userdata.__dict__} unexpectedly disconnected from the session. Rc {rc}\n')
        else:
            print(f'\n{userdata.__dict__} disconnected from the session.\n')

    def __init__(self,idClient,username,password,PATH=None):
        """Il costruttore accetta i seguenti parametri:
        - idClient
        - username
        - password
        - PATH (parametro addizionale nel caso in cui non si voglia usare il valore di default).

        L'IP e la porta del broker vengono recuperati dal file di configurazione."""
        self.path = MQTTPubSession.PATH if PATH is None else PATH
        self.username = username
        self.password = password
        self.idClient = idClient
        self.brokerIp = ConfigReader.read(self.path)['broker_ip']
        self.brokerPort = ConfigReader.read(self.path)['broker_port']

    def creaSessione(self):
        """Il metodo si occupa di creare la sessione mqtt di publish per i dati indicati.
        Ritorna un'istanza di mqtt.Client

        L'utilizzatore stabilirà come inviare i dati usando l'istanza di publish ritornata"""
        try:
            client = mqtt.Client(self.idClient)
            client.on_connect = MQTTPubSession.onConnect()
            client.on_disconnect = MQTTPubSession.onDisconnect()
            client.username_pw_set(self.username,self.password)
            client.connect(self.brokerIp, self.brokerPort)
            return client
        except Exception as e:
            return None