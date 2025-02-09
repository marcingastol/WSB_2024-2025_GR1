import moj_modul # import naszego modulu

# uzycie funkcji z modulu
moj_modul.przywitaj("Marcin") # oczekiwany rezultat: Czesc Marcin! Milo Cie poznac.

print("Funkcja policz do trzech zwraca liczby:")
moj_modul.policz_do_trzech() # powinno nam wydrukowac liczby 1,2,3 - w trzech linijkach

print(moj_modul.wiadomosc_powitalna)