# Programa de Programación Orientada a Objetos en Python
# Demostración de Herencia, Encapsulación y Polimorfismo
# Autor: [Tu Nombre]
# Carrera: [Tu Carrera], Nivel: [Tu Nivel]
# Correo: [tu.correo@ejemplo.com]

class Vehiculo:
    """
    Clase base que representa un vehículo genérico.
    Demuestra herencia (clases derivadas heredan de esta).
    """

    def __init__(self, marca, modelo, ano):
        # Encapsulación: atributos privados con __
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Método getter para encapsulación (acceso controlado)
    def get_marca(self):
        """Retorna la marca del vehículo (encapsulación)."""
        return self.__marca

    def descripcion(self):
        """Método que será sobrescrito en clases derivadas (polimorfismo)."""
        return f"Vehículo: {self.__marca} {self.__modelo} ({self.__ano})"


class Coche(Vehiculo):
    """
    Clase derivada de Vehiculo.
    Demuestra herencia y polimorfismo (sobrescribe descripcion).
    """

    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)  # Llama constructor padre
        self.__cilindrada = cilindrada  # Encapsulación

    def descripcion(self):
        """Sobrescribe el método de la clase base (polimorfismo)."""
        base_desc = super().descripcion()
        return f"{base_desc}, Coche con cilindrada {self.__cilindrada}cc"


class Moto(Vehiculo):
    """
    Otra clase derivada.
    Demuestra polimorfismo con implementación diferente.
    """

    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.__tipo = tipo  # Encapsulación

    def descripcion(self):
        """Sobrescribe el método (polimorfismo)."""
        base_desc = super().descripcion()
        return f"{base_desc}, Moto {self.__tipo}"


# Creación de instancias (objetos)
if __name__ == "__main__":
    # Instancia de clase base
    v_general = Vehiculo("Toyota", "Corolla", 2020)
    print(v_general.descripcion())  # Llama método base

    # Instancias de clases derivadas
    mi_coche = Coche("Ferrari", "488", 2023, 3900)
    mi_moto = Moto("Honda", "CBR", 2022, "deportiva")

    # Demostración de polimorfismo: mismo método, comportamientos diferentes
    vehiculos = [mi_coche, mi_moto, v_general]
    for veh in vehiculos:
        print(veh.descripcion())  # Cada uno ejecuta su versión

    # Demostración de encapsulación
    print("\nEncapsulación - Acceso controlado:")
    print(f"Marca del coche: {mi_coche.get_marca()}")  # Getter funciona
    # print(mi_coche.__cilindrada)  # Error: atributo privado
