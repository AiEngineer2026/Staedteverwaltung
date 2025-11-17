import csv
import os

class Stadt:
    def __init__(self, name, einwohner):
        self.name = name
        self.einwohner = einwohner

    def __str__(self):
        return f"Stadt: {self.name}, Einwohner: {self.einwohner}"

class Hauptstadt(Stadt):
    def __init__(self, name, einwohner, land):
        super().__init__(name, einwohner)
        self.land = land

    def __str__(self):
        return f"{self.name} – Hauptstadt von {self.land}, Einwohner: {self.einwohner}"

class Staedteverwaltung:
    DATEINAME = "staedte.csv"

    def __init__(self):
        self.staedte = []
        self.lade_daten()

    def stadt_hinzufügen(self, stadt):
        if any(s.name.lower() == stadt.name.lower() for s in self.staedte):
            print("Diese Stadt existiert schon!")
            return
        self.staedte.append(stadt)
        print(f"{stadt.name} wurde hinzugefügt!")
        self.speichere_daten()

    def groesste_stadt(self):
        return max(self.staedte, key=lambda s: s.einwohner, default=None)

    def kleinste_stadt(self):
        return min(self.staedte, key=lambda s: s.einwohner, default=None)

    def anzeigen(self):
        if not self.staedte:
            print("Keine Städte vorhanden!")
            return
        for stadt in sorted(self.staedte, key=lambda s: s.einwohner, reverse=True):
            print(stadt)

    # --- PERSISTENZ-TEIL ---

    def speichere_daten(self):
        """Speichert alle Städte in einer CSV-Datei."""
        with open(self.DATEINAME, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Name", "Einwohner", "Typ", "Land"])
            for s in self.staedte:
                if isinstance(s, Hauptstadt):
                    writer.writerow([s.name, s.einwohner, "Hauptstadt", s.land])
                else:
                    writer.writerow([s.name, s.einwohner, "Stadt", ""])
        print("💾 Daten wurden gespeichert.")

    def lade_daten(self):
        """Lädt Städte aus der CSV-Datei, falls vorhanden."""
        if not os.path.exists(self.DATEINAME):
            print("Keine gespeicherten Daten gefunden.")
            return
        with open(self.DATEINAME, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f,delimiter=';')
            for zeile in reader:
                name = zeile["name"]
                einwohner = int(zeile["einwohner"])
                typ = zeile["typ"]
                land = zeile["land"]

                if typ == "Hauptstadt":
                    stadt = Hauptstadt(name, einwohner, land)
                else:
                    stadt = Stadt(name, einwohner)
                self.staedte.append(stadt)
        print("📂 Gespeicherte Städte wurden geladen.")

if __name__ == "__main__":
    verwaltung = Staedteverwaltung()

    print("\nAktuelle Städte:")
    verwaltung.anzeigen()

    # Neue Städte hinzufügen
    hamburg = Stadt("Hamburg", 600000)
    muenchen = Stadt("München", 450000)
    berlin = Hauptstadt("Berlin", 1200000, "Deutschland")

    verwaltung.stadt_hinzufügen(hamburg)
    verwaltung.stadt_hinzufügen(muenchen)
    verwaltung.stadt_hinzufügen(berlin)

    print("\nNach Hinzufügen:")
    verwaltung.anzeigen()

    print("\nGrößte Stadt:", verwaltung.groesste_stadt())
    print("Kleinste Stadt:", verwaltung.kleinste_stadt())