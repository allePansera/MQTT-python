from Model.Temperature import Temperature
import random

class TemperatureManager:
    """La classe serve per gestire la generazione delle temperature"""
    @staticmethod
    def generateCelsius():
        tempValue = random.randrange(-30,50,0.5)
        UoM = "C°"
        return Temperature(tempValue,UoM)

