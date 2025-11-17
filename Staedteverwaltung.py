import sqlite3

class Stadt:
    def __init__(self, name, einwohner):
        if not isinstance(einwohner, int):
            raise TypeError("Einwohnerzahl muss eine ganze Zahl sein!")

        if einwohner < 0:
            raise ValueError("Einwohnerzahl darf nicht negativ sein!")
        self.name = name
        self.einwohner = einwohner

    def __str__(self):
        return f"{self.name} ({self.einwohner} Einwohner)"

class Hauptstadt(Stadt):
    def __init__(self, name, einwohner, land):
        super().__init__(name, einwohner)
        self.land = land

    def __str__(self):
        return f"{self.name} – Hauptstadt von {self.land} ({self.einwohner} Einwohner)"

class Staedteverwaltung:
    DATEINAME = "staedte.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.DATEINAME)
        self.cursor = self.conn.cursor()
        self._erstelle_tabelle()

    def _erstelle_tabelle(self):
        """Erstellt die Tabelle, falls sie noch nicht existiert."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS staedte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                einwohner INTEGER NOT NULL,
                typ TEXT,
                land TEXT
            )
        """)
        self.conn.commit()

    def stadt_hinzufuegen(self, stadt):
        """Fügt eine Stadt oder Hauptstadt in die DB ein."""
        typ = "Hauptstadt" if isinstance(stadt, Hauptstadt) else "Stadt"
        land = getattr(stadt, "land", None)
        try:
            self.cursor.execute("""
                INSERT INTO staedte (name, einwohner, typ, land)
                VALUES (?, ?, ?, ?)
            """, (stadt.name, stadt.einwohner, typ, land))
            self.conn.commit()
            print(f"✅ {stadt.name} wurde hinzugefügt.")
        except sqlite3.IntegrityError:
            print(f"⚠️ {stadt.name} existiert bereits in der Datenbank.")
            raise

    def anzeigen(self):
        """Zeigt alle Städte aus der DB an."""
        self.cursor.execute("SELECT name, einwohner, typ, land FROM staedte ORDER BY einwohner DESC")
        daten = self.cursor.fetchall()
        if not daten:
            print("Keine Städte vorhanden.")
            return
        for row in daten:
            name, einwohner, typ, land = row
            if typ == "Hauptstadt":
                print(f"{name} – Hauptstadt von {land} ({einwohner} Einwohner)")
            else:
                print(f"{name} ({einwohner} Einwohner)")

    def groesste_stadt(self):
        """Gibt die Stadt mit der höchsten Einwohnerzahl zurück."""
        self.cursor.execute("SELECT name, einwohner FROM staedte ORDER BY einwohner DESC LIMIT 1")
        result = self.cursor.fetchone()
        if result:
            print(f"🏙️ Größte Stadt: {result[0]} ({result[1]} Einwohner)")
        else:
            print("Keine Daten vorhanden.")

    def kleinste_stadt(self):
        """Gibt die Stadt mit der kleinsten Einwohnerzahl zurück."""
        self.cursor.execute("SELECT name, einwohner FROM staedte ORDER BY einwohner ASC LIMIT 1")
        result = self.cursor.fetchone()
        if result:
            print(f"🌆 Kleinste Stadt: {result[0]} ({result[1]} Einwohner)")
        else:
            print("Keine Daten vorhanden.")

    def __del__(self):
        """Wird beim Beenden automatisch aufgerufen."""
        self.conn.close()

    def stadt_aktualisieren(self, name, neue_einwohnerzahl):
        self.cursor.execute("UPDATE staedte SET einwohner = ? WHERE name = ?", (neue_einwohnerzahl, name))
        if self.cursor.rowcount > 0:
            print(f"{name} wurde aktualisiert!")
        else:
            print(f"Es wurde keine Stadt mit dem Namen {name} gefunden!")
        self.conn.commit()

    def stadt_loeschen(self, name):
        self.cursor.execute("DELETE FROM staedte WHERE name = ?", (name,))
        if self.cursor.rowcount > 0:
            print(f"{name} wurde gelöscht!")
        else:
            print(f"Es wurde keine Stadt mit dem Namen {name} gefunden!")
        self.conn.commit()




if __name__ == "__main__":
    verwaltung = Staedteverwaltung()

    berlin = Hauptstadt("Berlin", 1200000, "Deutschland")
    hamburg = Stadt("Hamburg", 600000)
    muenchen = Stadt("München", 450000)

    verwaltung.stadt_hinzufuegen(berlin)
    verwaltung.stadt_hinzufuegen(hamburg)
    verwaltung.stadt_hinzufuegen(muenchen)

    print("\n📋 Alle Städte:")
    verwaltung.anzeigen()

    verwaltung.stadt_aktualisieren("Köln", 650000)
    verwaltung.stadt_loeschen("Berlin")
    print("\n📋 Alle Städte upgedated:")
    verwaltung.anzeigen()

    verwaltung.groesste_stadt()
    verwaltung.kleinste_stadt()

    print ("Branch")
