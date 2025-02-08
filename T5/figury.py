import math

class Kwadrat:
    def __init__(self,dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku

    def powierzchnia(self):
        return self.dlugosc_boku ** 2
    
class Kolo:
    def __init__(self,promien):
        self.promien = promien

    def powierzchnia(self):
        return math.pi * (self.promien ** 2)