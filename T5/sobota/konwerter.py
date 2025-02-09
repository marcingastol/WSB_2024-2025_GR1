PRZELICZNIK = 0.61 # 1 km = 0.61xxxxx mile

def km_na_mile(km):
    """Konwersja kilometry na mile"""
    return km * PRZELICZNIK

def mile_na_km(mile):
    """Konwersja mile na kilometry"""
    return mile / PRZELICZNIK