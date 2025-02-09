class Samochod:
    # definicja klasy
    def __init__(self, marka, model):
        # self reprezentuje nowo tworzona instacje/obiekt
        self.marka = marka # ustawiamy atrybut 'marka' obiektu
        self.model = model # ustawiamy atrybut 'model'
        self.predkosc = 0 # ustawiamy predkosc poczatkowa samochodu to 0 km/h
        self.wlaczony_silnik = False
        self.kolor = "czerwony"
    
    def uruchom_silnik(self):
        print("Silnik zostal uruchomiony")
        self.wlaczony_silnik = True

    def przyspiesz(self, wartosc):
        # zakladamy ze atrybut predkosc istnieje
        self.predkosc += wartosc

moj_samochod = Samochod("Toyota","Yaris")

#moj_samochod.uruchom_silnik()
#moj_samochod.przyspiesz(50)

#print(moj_samochod.wlaczony_silnik)
#print(moj_samochod.predkosc)


moj_samochod_2 = Samochod("BMW", "5")
moj_samochod_2.uruchom_silnik()

print(moj_samochod_2.kolor)