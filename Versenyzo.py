class Versenyzo:

    def __init__(self, args: []):
        self.nev = args[0]
        self.orszagKod = args[1]
        self.technikaiPontszam = float(args[2])
        self.komponensPontszam = float(args[3])
        self.hibapont = int(args[4])

    def osszPontszam(self):
        return self.technikaiPontszam + self.komponensPontszam - self.hibapont
