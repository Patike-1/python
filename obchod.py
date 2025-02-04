class ShopCart:
    def __init__(self):
        self.items = []

    def addItem(self, name, price):
        self.items.append({"name": name, "price": price})
        print(f'Položka "{name}" za {price} EUR bola pridaná do košíka.')

    def removeItem(self, name):
        new_items = [item for item in self.items if item["name"] != name]
        if len(new_items) == len(self.items):
            print(f'Položka "{name}" sa v košíku nenachádza.')
        else:
            self.items = new_items
            print(f'Položka "{name}" bola odstránená.')

    def printContent(self):
        if not self.items:
            print("Košík je prázdny.")
        else:
            total = 0
            print("\nPoložky v košíku:")
            for item in self.items:
                print(f'{item["name"]} - {item["price"]} €')
                total += item["price"]
            print(f'Celková hodnota: {total} €')


cart = ShopCart()

while True:
    print("\nVyberte akciu:")
    print("1 - Pridať položku")
    print("2 - Odstrániť položku")
    print("3 - Zobraziť obsah košíka")
    print("4 - Ukončiť program")
    
    choice = input("Zadajte číslo akcie: ")
    
    if choice == "1":
        name = input("Zadajte názov položky: ")
        try:
            price = float(input("Zadajte cenu položky: "))
            cart.addItem(name, price)
        except ValueError:
            print("Neplatná cena, skúste znova.")
    
    elif choice == "2":
        name = input("názov položky, ktorú chcete odstrániť: ")
        cart.removeItem(name)
    
    elif choice == "3":
        cart.printContent()
    
    elif choice == "4":
        print("konec.")
        break
    
    else:
        print("nieco sa pokazilo, skuste to znova.")