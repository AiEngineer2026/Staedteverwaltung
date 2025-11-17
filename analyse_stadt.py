import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt

conn = sql.connect("staedte.db")

df = pd.read_sql_query("SELECT * FROM staedte", conn)

print("\n📊 Statistik über alle Städte:\n")
print(df["einwohner"].describe())

print("\nGrößte Stadt:")
print(df.loc[df["einwohner"].idxmax()])

print ("\nKleinste Stadt:")
print(df.loc[df["einwohner"].idxmin()])

durchschnitt = df["einwohner"].mean()
print(f"\n📈 Durchschnittliche Einwohnerzahl: {durchschnitt:,.0f}".replace(",", "."))

# --- Balkendiagramm der Einwohnerzahlen ---
plt.figure(figsize=(8,5))
plt.bar(df["name"], df["einwohner"], color="skyblue", edgecolor="black")

plt.title("Einwohnerzahlen deutscher Städte")
plt.xlabel("Stadt")
plt.ylabel("Einwohnerzahl")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# --- Kreisdiagramm der prozentualen Verteilung ---
plt.figure(figsize=(6, 6))
plt.pie(
    df["einwohner"],
    labels=df["name"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["cornflowerblue", "lightgreen", "salmon"]
)
plt.title("Anteil der Städte an der Gesamtbevölkerung")
plt.tight_layout()

plt.show()



