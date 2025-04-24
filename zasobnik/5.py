class Zasobnik:
    def __init__(self):
        """Iniciuje prázdny zásobník."""
        self.stack = []

    def push(self, item):
        """Pridá prvok do zásobníka."""
        self.stack.append(item)

    def pop(self):
        """Odoberie a vráti prvok zo zásobníka."""
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Zásobník je prázdny.")
            return None

    def display(self):
        """Zobrazí všetky prvky zásobníka."""
        if self.isEmpty():
            print("Zásobník je prázdny.")
        else:
            print("Aktuálny stav zásobníka:")
            for item in reversed(self.stack):
                print(item)

    def isEmpty(self):
        """Skontroluje, či je zásobník prázdny."""
        return len(self.stack) == 0

    def length(self):
        """Vráti počet prvkov v zásobníku."""
        return len(self.stack)


# Testovanie triedy Zasobnik
if __name__ == "__main__":
    zasobnik = Zasobnik()

    # Pridanie prvkov do zásobníka
    zasobnik.push(5)
    zasobnik.push("Ahoj")
    zasobnik.push([1, 2, 3])

    # Zobrazenie aktuálneho stavu zásobníka
    zasobnik.display()  # Zobrazí: [1, 2, 3], Ahoj, 5

    # Odobratie prvku
    print("Odobrany prvok:", zasobnik.pop())  # Vytlačí: Odobrany prvok: [1, 2, 3]

    # Zobrazenie aktuálneho stavu zásobníka po odstránení
    zasobnik.display()  # Zobrazí: Ahoj, 5

    # Zistenie, či je zásobník prázdny
    print("Je zásobník prázdny?", zasobnik.isEmpty())  # Vytlačí: False

    # Zistenie počtu prvkov v zásobníku
    print("Počet prvkov v zásobníku:", zasobnik.length())  # Vytlačí: 2

    # Odobratie posledného prvku
    print("Odobrany prvok:", zasobnik.pop())  # Vytlačí: Odobrany prvok: Ahoj

    # Zobrazenie aktuálneho stavu zásobníka po odstránení všetkých prvkov
    zasobnik.display()  # Zobrazí: Zásobník je prázdny.

    # Zistenie, či je zásobník prázdny po odstránení všetkých prvkov
    print("Je zásobník prázdny?", zasobnik.isEmpty())  # Vytlačí: True
