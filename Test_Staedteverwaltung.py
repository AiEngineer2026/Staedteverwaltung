import unittest
import sqlite3 as sql
from Staedteverwaltung import Stadt, Hauptstadt, Staedteverwaltung

class TestStaedteverwaltung(unittest.TestCase):

    def setUp(self):
        """Wird vor jedem Test automatisch ausgeführt"""
        self.verwaltung = Staedteverwaltung()
        self.verwaltung.conn = sql.connect(":memory:")
        self.verwaltung.cursor = self.verwaltung.conn.cursor()
        self.verwaltung._erstelle_tabelle()

    def test_stadt_hinzufuegen(self):
        """Testet, ob eine Stadt hinzugefügt wird"""
        hamburg = Stadt("Hamburg", 600000)
        self.verwaltung.stadt_hinzufuegen(hamburg)

        result = self.verwaltung.cursor.execute("SELECT name FROM staedte WHERE name = ?", ("Hamburg",)).fetchone()
        self.assertIsNotNone(result)

    def test_groesste_stadt(self):
        """Testet, ob die ausgewählte Stadt die größte Einwohnerzahl besitzt!"""
        berlin = Hauptstadt("Berlin", 1200000, "Deutschland")
        hamburg = Stadt("Hamburg", 600000)
        muenchen = Stadt("Muenchen", 450000)

        # ALle Städte hinzufügen
        self.verwaltung.stadt_hinzufuegen(berlin)
        self.verwaltung.stadt_hinzufuegen(hamburg)
        self.verwaltung.stadt_hinzufuegen(muenchen)

        # SQL Abfrage ob die ausgewählte Stadt die größte ist
        self.verwaltung.cursor.execute("SELECT name FROM staedte ORDER BY einwohner DESC LIMIT 1")
        result = self.verwaltung.cursor.fetchone()[0]

        # Erwartung prüfen
        self.assertEqual(result, "Berlin")

    def test_doppelte_stadt(self):
        """Testet, ob beim Hinzufügen einer doppelten Stadt eine Exception ausgelöst wird"""
        hamburg = Stadt("Hamburg", 600000)
        self.verwaltung.stadt_hinzufuegen(hamburg)

        # Versuch, dieselbe Stadt nochmal hinzuzufügen
        with self.assertRaises(sql.IntegrityError):
            self.verwaltung.stadt_hinzufuegen(hamburg)

    def test_negative_einwohner(self):
        """Testet ob eine negative Zahl für EInwohner eingegeben wurde!"""
        with self.assertRaises(ValueError):
            Stadt("Loikum", -100)

    def test_falscher_datentyp(self):
        """Testet, ob bei falschem Datentyp (kein int) ein TypeError ausgelöst wird"""
        with self.assertRaises(TypeError):
            Stadt("Loikum", "Viele")

    def test_stadt_loeschen(self):
        # Vorbereitung: Stadt anlegen
        hamburg = Stadt("Hamburg", 600000)
        self.verwaltung.stadt_hinzufuegen(hamburg)

        # Stadt löschen
        self.verwaltung.stadt_loeschen("Hamburg")

        # Prüfen ob Hamburg gelöscht wurde
        self.verwaltung.cursor.execute("SELECT COUNT(*) FROM staedte WHERE name = ?", ('Hamburg',))
        ergebnis_tupel = self.verwaltung.cursor.fetchone()
        anzahl_eintraege = ergebnis_tupel[0]

        self.assertEqual(anzahl_eintraege, 0, "Fehler: Die Stadt 'Hamburg' wurde nach dem Löschen immer noch gefunden.")

def test_kleinste_stadt(self):
    """Testet, ob die kleinste Stadt korrekt erkannt wird"""

    # Testdaten
    berlin = Hauptstadt("Berlin", 1200000, "Deutschland")
    hamburg = Stadt("Hamburg", 600000)
    muenchen = Stadt("Muenchen", 450000)

    # In Datenbank einfügen
    self.verwaltung.stadt_hinzufuegen(berlin)
    self.verwaltung.stadt_hinzufuegen(hamburg)
    self.verwaltung.stadt_hinzufuegen(muenchen)

    # SQL-Abfrage, um die kleinste Stadt zu holen
    self.verwaltung.cursor.execute(
        "SELECT name FROM staedte ORDER BY einwohner ASC LIMIT 1"
    )
    result = self.verwaltung.cursor.fetchone()[0]

    # Erwartung prüfen
    self.assertEqual(
        result,
        "Muenchen",
        "Fehler: Die kleinste Stadt wurde nicht korrekt ermittelt."
    )





