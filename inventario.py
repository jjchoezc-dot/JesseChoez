# Sistema de Gestión de Inventarios - Tarea POO Python
# Autor: [Tu Nombre] - Estudiante de Ingeniería en Sistemas
# Descripción: Implementa clases Producto e Inventario con menú consola interactivo.
# Usa lista para almacenar productos (estructura simple y eficiente).
# ID único generado automáticamente para evitar duplicados.

class Producto:
    def __init__(self, nombre, cantidad, precio):  # Corregido: __init__
        self._id = None
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_id(self, id_val):  # Renombrado para evitar keyword shadow
        self._id = id_val

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_id = len(self._productos) + 1
        # Corregido: any() con generator expression
        if any(p.get_id() == nuevo_id for p in self._productos):
            print("Error: ID duplicado.")
            return False

        producto = Producto(nombre, cantidad, precio)
        producto.set_id(nuevo_id)
        self._productos.append(producto)
        print(f"Producto '{nombre}' agregado con ID {nuevo_id}.")
        return True

    def eliminar_producto(self, id_val):
        # Corregido: enumerate con unpacking correcto
        for i, p in enumerate(self._productos):
            if p.get_id() == id_val:
                eliminado = self._productos.pop(i)
                print(f"Producto '{eliminado.get_nombre()}' eliminado.")
                return True
        print("Producto no encontrado.")
        return False

    def actualizar_producto(self, id_val, cantidad=None, precio=None):
        for p in self._productos:
            if p.get_id() == id_val:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto ID {id_val} actualizado.")
                return True
        print("Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self._productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos.")
        return resultados

    def mostrar_todos(self):
        if not self._productos:
            print("Inventario vacío.")
            return
        print("\n--- Inventario Completo ---")
        for p in self._productos:
            print(p)
        print("---------------------------")


def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIOS ===")
        print("1. Añadir producto")
        print("2. Eliminar por ID")
        print("3. Actualizar cantidad/precio por ID")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("0. Salir")

        opcion = input("Elige: ").strip()

        if opcion == '1':
            nombre = input("Nombre: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("Error: Cantidad y precio numéricos.")

        elif opcion == '2':
            try:
                id_val = int(input("ID a eliminar: "))
                inventario.eliminar_producto(id_val)
            except ValueError:
                print("ID numérico.")

        elif opcion == '3':
            try:
                id_val = int(input("ID: "))
                cant_str = input("Nueva cantidad (Enter para skip): ").strip()
                cantidad = int(cant_str) if cant_str else None
                prec_str = input("Nuevo precio (Enter para skip): ").strip()
                precio = float(prec_str) if prec_str else None
                inventario.actualizar_producto(id_val, cantidad, precio)
            except ValueError:
                print("Valores inválidos.")

        elif opcion == '4':
            nombre = input("Nombre a buscar: ").strip()
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '0':
            print("¡Saliendo!")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
