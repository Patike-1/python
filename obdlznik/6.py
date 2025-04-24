class Rectangle:
    def __init__(self, x, y, a, b):
        """Konštruktor, ktorý vytvorí obdĺžnik so stranami a, b a polohou ľavého horného rohu [x, y]."""
        self.x = x  # X-ová súradnica ľavého horného rohu
        self.y = y  # Y-ová súradnica ľavého horného rohu
        self.a = a  # Dĺžka prvej strany
        self.b = b  # Dĺžka druhej strany

    def setDimensions(self, a, b):
        """Zmení rozmery obdĺžnika."""
        self.a = a
        self.b = b

    def getDimensions(self):
        """Vráti tuple - dvojicu obsahujúcu dĺžky strán obdĺžnika."""
        return (self.a, self.b)

    def isSquare(self):
        """Vrátí boolean, na základe toho, či je obdĺžnik štvorcom."""
        return self.a == self.b

    def getArea(self):
        """Vráti číslo - veľkosť plochy obdĺžnika."""
        return self.a * self.b

    def getCircumference(self):
        """Vráti číslo - dĺžku obvodu obdĺžnika."""
        return 2 * (self.a + self.b)

    def getPosition(self):
        """Vráti dvojicu obsahujúcu súradnice [x, y] ľavého horného rohu obdĺžnika."""
        return (self.x, self.y)

    def move(self, deltaX, deltaY):
        """Posunie obdĺžnik na ploche o deltaX bodov v osi X a o deltaY bodov v osi Y."""
        self.x += deltaX
        self.y += deltaY

    def moveTo(self, x, y):
        """Presunie obdĺžnik na súradnice [x, y]."""
        self.x = x
        self.y = y

    def contains(self, x, y):
        """Vrátí boolean podľa toho, či je bod na súradniciach [x, y] v obdĺžniku."""
        return self.x <= x <= self.x + self.a and self.y <= y <= self.y + self.b

    def makeSquare(self):
        """Zmení obdĺžnik na štvorec, tak že dlhšiu stranu skráti na dĺžku menšej strany."""
        if self.a > self.b:
            self.a = self.b
        elif self.b > self.a:
            self.b = self.a


# Testovanie triedy Rectangle
if __name__ == "__main__":
    # Vytvorenie obdĺžnika s ľavým horným rohom na (0, 0) a stranami 5 a 10
    rect = Rectangle(0, 0, 5, 10)

    # Získanie rozmerov
    print(f"Rozmery obdĺžnika: {rect.getDimensions()}")  # (5, 10)

    # Zistenie, či je to štvorec
    print(f"Je to štvorec? {rect.isSquare()}")  # False

    # Zistenie plochy
    print(f"Area (plocha): {rect.getArea()}")  # 50

    # Zistenie obvodu
    print(f"Obvod: {rect.getCircumference()}")  # 30

    # Zistenie pozície ľavého horného rohu
    print(f"Pozícia ľavého horného rohu: {rect.getPosition()}")  # (0, 0)

    # Posunutie obdĺžnika
    rect.move(5, 5)
    print(f"Nová pozícia po posunutí: {rect.getPosition()}")  # (5, 5)

    # Presunutie na konkrétne súradnice
    rect.moveTo(10, 10)
    print(f"Nová pozícia po presunutí: {rect.getPosition()}")  # (10, 10)

    # Zistenie, či bod je v obdĺžniku
    print(f"Obsahuje bod (12, 12)? {rect.contains(12, 12)}")  # True
    print(f"Obsahuje bod (20, 20)? {rect.contains(20, 20)}")  # False

    # Zmena obdĺžnika na štvorec
    rect.makeSquare()
    print(f"Nové rozmery po zmene na štvorec: {rect.getDimensions()}")  # (10, 10)

    # Zistenie, či je to štvorec
    print(f"Je to štvorec? {rect.isSquare()}")  # True
