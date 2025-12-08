class Vehiculo:
    """Abstracción: exponemos solo acelerar() y frenar(), ocultando motor."""

    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print(f"{self.marca} acelera.")

    def frenar(self):
        print(f"{self.marca} frena.")


coche = Vehiculo("Toyota")
coche.acelerar()  # Output: Toyota acelera.
