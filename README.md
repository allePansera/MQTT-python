# MQTT-python

## Logics

Il progetto si occupa di creare un modello di dialogo Pub/Sub altamente configurabile
Vengono create delle sessioni configurabili all'interno di file json che possono essere dati in pasto al costruttore delle classi.
In questo modo ogni dispositivo sarà configurato con un JSON in modo da evitare di modificare il codice durante la creazione di nuovi topic/dispositivi.


## Code

All'interno di Configurations sono stati inseriti i file base con le config di Default per client e subscriber.
Le classi che generano le sessioni Publisher/Subscriber sono definite dentro Auth/MQTTSub(Pub)Session.py

E' stata modellata solo la risorsa Temperature.

publisherExample.py e subscriberExample.py sono codici esemplificativi con la creazione di un singolo publisher ed un singolo subscriber
