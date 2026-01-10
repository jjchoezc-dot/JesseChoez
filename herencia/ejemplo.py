class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):  # Herencia
    def ladrar(self):
        print(f"{self.nombre} ladra: ¡Guau!")

perro = Perro("Rex")
perro.ladrar()  # Output: Rex ladra: ¡Guau!
