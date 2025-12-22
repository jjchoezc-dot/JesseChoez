"""
Sistema de Reservas de Hotel - Ejemplo POO Mundo Real
Clases interactúan: Cliente reserva Habitacion en Hotel.
Demuestra atributos privados, métodos y objetos relacionados.
"""


class Habitacion:
    """Representa una habitación con estado de disponibilidad."""

    def __init__(self, numero, precio):
        self._numero = numero  # Atributo protegido
        self._precio = precio
        self._disponible = True

    def reservar(self):
        """Cambia estado a no disponible."""
        self._disponible = False
        return f"Habitación {self._numero} reservada."

    def esta_disponible(self):
        return self._disponible

    def __str__(self):
        return f"Habitación {self._numero}: ${self._precio} {'Disponible' if self._disponible else 'Ocupada'}"


class Cliente:
    """Cliente con nombre y lista de reservas."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)


class Hotel:
    """Hotel gestiona múltiples habitaciones y clientes."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.clientes = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def encontrar_habitacion_disponible(self, numero):
        for hab in self.habitaciones:
            if hab.esta_disponible() and hab._numero == numero:
                return hab
        return None

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)


# Ejemplo de interacción entre objetos
hotel = Hotel("Hotel Ecuador")
hotel.agregar_habitacion(Habitacion(101, 100))
hotel.agregar_habitacion(Habitacion(102, 120))

cliente1 = Cliente("Jessechoez")
hotel.registrar_cliente(cliente1)

hab101 = hotel.encontrar_habitacion_disponible(101)
if hab101:
    print(hab101.reservar())
    cliente1.agregar_reserva("Reserva 101")
    print(f"Cliente {cliente1.nombre} tiene {len(cliente1.reservas)} reservas.")

print(hotel.habitaciones[0])  # Polimorfismo con __str__
