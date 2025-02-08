#from math import sqrt

import math

class Kalkulator:
    def __init__(self,liczba_1,liczba_2):
        self.liczba_1 = liczba_1
        self.liczba_2 = liczba_2
    
    def dodawanie(self):
        return self.liczba_1 + self.liczba_2
    
    def odejmowanie(self):
        return self.liczba_1 - self.liczba_2
    
    def dzielenie(self):
        print(self.liczba_1 / self.liczba_2)
    
    def mnozenie(self):
        print(self.liczba_1 * self.liczba_2)

    def pierwiastek(self):
        return math.sqrt(self.liczba_1)
        
    def potega(self):
        return math.pow(self.liczba_1,self.liczba_2)

#liczba_1 = int(input("Podaj liczbe 1: "))
#liczba_2 = int(input("Podaj liczbe 2: "))
#kalkulator_1 = Kalkulator(liczba_1,liczba_2)    

kalkulator_1 = Kalkulator(3,4)    
print(kalkulator_1.pierwiastek())

#kalkulator_1.dzielenie()