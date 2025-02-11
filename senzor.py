def read_sensor_data(file_name):
    try:
        with open(file_name, 'r') as file:
            
            data = [int(line.strip()) for line in file]
        
        
        if len(data) == 0:
            print("Súbor je prázdny.")
            return

        
        max_value = max(data)
        min_value = min(data)
        avg_value = sum(data) / len(data)
        
        
        print(f"Maximálna hodnota: {max_value}")
        print(f"Minimálna hodnota: {min_value}")
        print(f"Priemer hodnôt: {avg_value:.2f}")

    except FileNotFoundError:
        print(f"Súbor {file_name} neexistuje.")
    except ValueError:
        print("Súbor obsahuje neplatné dáta. Každý riadok musí obsahovať celé číslo.")


file_name = input("Zadajte názov súboru: ")
read_sensor_data(file_name)