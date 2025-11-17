try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Hey, du darfst nicht durch 0 dividieren!")
except TypeError:
    print("Hey, du kannst nur mit Zahlen rechnen!")
except:
    print("Hey, hier ist was schief gelaufen!")

