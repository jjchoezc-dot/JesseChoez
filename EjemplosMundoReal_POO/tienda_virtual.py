"""
Tienda Virtual - Ejemplo POO Mundo Real
Clases: Producto (herencia), Carrito y Tienda interactúan.
Demuestra herencia y encapsulación de inventario.
"""


class Producto:
    """Clase base para productos con precio y stock."""

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio  # Encapsulado
        self._stock = stock

    def disponible(self):
        return self._stock > 0

    def comprar(self, cantidad):
        if self.disponible() and cantidad <= self._stock:
            self._stock -= cantidad
            return cantidad * self._precio
        return 0


class Electronico(Producto):  # Herencia
    """Producto electrónico con garantía."""

    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia

    def __str__(self):
        return f"{self.nombre}: ${self._precio} (Garantía: {self.garantia} años)"


class Tienda:
    """Gestiona productos y carritos."""

    def __init__(self):
        self.productos = []
        self.carrito = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_al_carrito(self, nombre_producto, cantidad):
        for prod in self.productos:
            if prod.nombre == nombre_producto and prod.disponible():
                total = prod.comprar(cantidad)
                if total > 0:
                    self.carrito.append((nombre_producto, cantidad, total))
                    print(f"Agregado: {cantidad} {nombre_producto}")
                    return
        print("Producto no disponible.")


# Ejemplo de interacción
tienda = Tienda()
tienda.agregar_producto(Electronico("Laptop", 800, 5, 2))
tienda.agregar_producto(Producto("Mouse", 20, 10))

tienda.agregar_al_carrito("Laptop", 1)
tienda.agregar_al_carrito("Mouse", 2)

total_carrito = sum(item[2] for item in tienda.carrito)
print(f"Total carrito: ${total_carrito}")
print(tienda.productos[0])  # Herencia en acción

