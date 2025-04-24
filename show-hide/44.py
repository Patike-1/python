def show_or_hide():
    # Načítame počet záznamov
    x = int(input())  # Počet záznamov
    records = []

    # Načítame záznamy
    for _ in range(x):
        records.append(input())  # Pridáme každú položku do zoznamu

    # Vytvoríme zoznam pre označenie odstránených alebo obnovených prvkov
    removed = [False] * x  # Na začiatku všetky prvky sú neodstránené

    # Načítavame indexy na odstránenie/obnovenie
    while True:
        index = int(input())  # Načítame index
        if index == -1:
            break  # Končíme, keď je zadané -1
        if 0 <= index < x:  # Overíme, či index je platný
            removed[index] = not removed[index]  # Prepneme stav (odstrániť/obnoviť)

    # Výpis výsledného zoznamu
    for i in range(x):
        if not removed[i]:
            print(records[i])  # Vypíšeme len tie, ktoré nie sú odstránené

# Spustíme funkciu
show_or_hide()
