import random # importowanie modulu random

wynik = [] # deklaracja listy

for i in range(5): # petla 5x 
    liczba = random.randint(1,100) # zapisanie wartosci losowej do zmiennej
    wynik.append(liczba) # dodanie wartosci do listy

print("Wylosowane liczby to:", wynik)