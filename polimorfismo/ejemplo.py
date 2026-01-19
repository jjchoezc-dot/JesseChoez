class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base, self.altura = base, altura
    def area(self):
        return self.base * self.altura

figuras = [Circulo(5), Rectangulo(4, 6)]
for f in figuras:
    print(f.area())  # Outputs: 78.5, 24
