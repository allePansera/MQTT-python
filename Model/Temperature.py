class Temperature:
    """La classe modella la risorsa temperature"""
    def __init__(self,value,UoM):
        """Il costruttore accetta 2 parametri:
        - valore numerico
        - stringa che identifica l'unità di misura"""
        self.value = float(value,5)
        self.UoM = UoM


    def __str__(self):
        return self.__dict__