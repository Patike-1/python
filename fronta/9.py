class Fronta:
    def __init__(self):
        """Iniciuje prázdnu frontu."""
        self.queue = []

    def push(self, item):
        """Pridá prvok do fronty."""
        self.queue.append(item)

    def pop(self):
        """Odoberie a vráti prvok z fronty."""
        if not self.isEmpty():
            return self.queue.pop(0)  # Odoberie prvý prvok z fronty (FIFO)
        else:
            print("Fronta je prázdna.")
            return None

    def display(self):
        """Zobrazí všetky prvky fronty."""
        if self.isEmpty():
            print("Fronta je prázdna.")
        else:
            print("Aktuálny stav fronty:")
            for item in self.queue:
                print(item)

    def isEmpty(self):
        """Skontroluje, či je fronta prázdna."""
        return len(self.queue) == 0

    def length(self):
        """Vráti počet prvkov vo fronte."""
        return len(self.queue)


# Testovanie triedy Fronta
if __name__ == "__main__":
    fronta = Fronta()

    # Pridanie prvkov do fronty
    fronta.push(5)
    fronta.push("Ahoj")
    fronta.push([1, 2, 3])

    # Zobrazenie aktuálneho stavu fronty
    fronta.display()  # Zobrazí: 5, Ahoj, [1, 2, 3]

    # Odobratie prvku z fronty (FIFO)
    print("Odobrany prvok:", fronta.pop())  # Vytlačí: Odobrany prvok: 5

    # Zobrazenie aktuálneho stavu fronty po odstránení
    fronta.display()  # Zobrazí: Ahoj, [1, 2, 3]

    # Zistenie, či je fronta prázdna
    print("Je fronta prázdna?", fronta.isEmpty())  # Vytlačí: False

    # Zistenie počtu prvkov v fronte
    print("Počet prvkov v fronte:", fronta.length())  # Vytlačí: 2

    # Odobratie ďalšieho prvku
    print("Odobrany prvok:", fronta.pop())  # Vytlačí: Odobrany prvok: Ahoj

    # Zobrazenie aktuálneho stavu fronty po odstránení ďalšieho prvku
    fronta.display()  # Zobrazí: [1, 2, 3]

    # Zistenie, či je fronta prázdna po odstránení všetkých prvkov
    print("Je fronta prázdna?", fronta.isEmpty())  # Vytlačí: False

    # Odobratie posledného prvku
    print("Odobrany prvok:", fronta.pop())  # Vytlačí: Odobrany prvok: [1, 2, 3]

    # Zobrazenie aktuálneho stavu fronty po odstránení všetkých prvkov
    fronta.display()  # Zobrazí: Fronta je prázdna.

    # Zistenie, či je fronta prázdna po odstránení všetkých prvkov
    print("Je fronta prázdna?", fronta.isEmpty())  # Vytlačí: True
