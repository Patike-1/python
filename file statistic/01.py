def file_statistics(filename):
    try:
        with open(filename, 'r', ) as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            chars = len(content)

            print(f"Počet riadkov: {len(lines)}")
            print(f"Počet slov: {len(words)}")
            print(f"Počet znakov: {chars}")
    except FileNotFoundError:
        print("Súbor nebol nájdený.")
    except Exception as e:
        print(f"Nastala chyba: {e}")

# Hlavný program
filename = input("Zadajte názov súboru: ")
file_statistics(filename)
