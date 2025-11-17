class Auto():
    """
    Das ist meine Auto Klasse, damit ich nicht
    jedes mal aufs neue alles definieren muss!
    """
    def __init__(self, marke, modell, baujahr, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.raeder = 4
        self.tueren = tueren
        self.ps = ps

    def begruessung(self):
        print("Hallo mein lieber, ich bin ein" + self.marke)

    def fahren(self):
        print("Brum!" * int(self.ps/10))

class Sportwagen(Auto):
    def __init__(self, marke, modell, baujahr, tueren, ps, folierung):
        super().__init__(marke, modell, baujahr, tueren, ps)
        self.folierung = folierung
        self.auspuff = 2

    def Turbo(self):
        print("Turba aktiv!")

class Kombi(Auto):
    def __init__(self, marke, modell, baujahr, tueren, ps, ladeflaeche):
        super().__init__(marke, modell, baujahr, tueren, ps)
        self.ladeflaeche = ladeflaeche

    def transport(self):
        print("Transport aktiv!")


kombi1 = Kombi("Seat", "Leon", "2025", "4", "150", 490)
kombi2 = Kombi("Opel", "Astra", "2025", "4", "150", 450)

print(kombi1.ladeflaeche)
print(kombi2.ladeflaeche)
print(kombi1.transport())
print(kombi2.transport())
print(kombi2.begruessung())