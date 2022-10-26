from Auth.MQTTSubSession import MQTTSubSession

#TODO -> si potrebbero fare pià file per testare molteplici subscriber

#credenziali di accesso
username, password = "", ""
#id del subscriber
idSub = "client-0001"
#viene generato un singolo publisher
subscriber = MQTTSubSession(username,password,idSub)
subscriberSession = subscriber.creaSessione()
subscriberSession.loop_forever()