import random # importujemy modul do losowania liczb

# wylosujmy liczbe z przedzialu 1 do 10

liczba_1 = int(input("Podaj liczbe 1:"))
liczba_2 = int(input("Podaj liczbe 2:"))

losowa = random.randint(liczba_1,liczba_2)
print(f"Wynik losowania z liczb z zakresu {liczba_1} do {liczba_2} to: ", losowa)

# wylosujmy 5 liczb z zakresu od 1 do 10 i zapiszmy je do listy

lista_losowych = random.sample(range(1,11),5)

print("Lista liczb wylosowanych z zakresu 1 do 10 to: ",lista_losowych)
