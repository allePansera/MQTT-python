from Auth.MQTTSubSession import MQTTSubSession

#TODO -> si potrebbero fare pià file per testare molteplici subscriber


#viene generato un singolo publisher
subscriber = MQTTSubSession()
subscriberSession = subscriber.creaSessione()
subscriberSession.loop_forever()