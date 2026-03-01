"""
Sistema Avanzado de Gestión de Inventario - Versión 3.0
Autor: Jesse James Choez Chavez
Usa POO con clases Producto e Inventario (diccionario para O(1) búsquedas).
Persistencia JSON para serialización/deserialización automática.
Colecciones: dict (inventario por ID), list (búsquedas por nombre).
PyCharm/GitHub ready.
"""

import json
import os
from typing import Dict, Optional, List

class Producto:
    """Clase Producto con encapsulamiento (getters/setters). ID único."""
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters
    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    def set_cantidad(self, cantidad: int):
        self._cantidad = cantidad

    def set_precio(self, precio: float):
        self._precio = precio

    def to_dict(self) -> dict:
        """Serialización a dict para JSON."""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Deserialización desde dict."""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

class Inventario:
    """Clase Inventario usa dict {ID: Producto} para acceso O(1)."""
    def __init__(self, archivo: str = 'inventario.json'):
        self.productos: Dict[str, Producto] = {}
        self.archivo = archivo
        self._cargar_inventario()

    def _generar_id(self) -> str:
        """Genera ID único: max actual +1."""
        if not self.productos:
            return "1"
        return str(max(int(p.get_id()) for p in self.productos.values()) + 1)

    def agregar_producto(self, nombre: str, cantidad: int, precio: float):
        id_nuevo = self._generar_id()
        producto = Producto(id_nuevo, nombre, cantidad, precio)
        self.productos[id_nuevo] = producto
        self._guardar_inventario()
        print(f"✅ Producto '{nombre}' (ID: {id_nuevo}) agregado.")

    def eliminar_producto(self, id_producto: str) -> bool:
        if id_producto in self.productos:
            del self.productos[id_producto]
            self._guardar_inventario()
            print(f"✅ Producto ID {id_producto} eliminado.")
            return True
        print("❌ ID no encontrado.")
        return False

    def actualizar_producto(self, id_producto: str, cantidad: Optional[int] = None, precio: Optional[float] = None):
        if id_producto not in self.productos:
            print("❌ ID no encontrado.")
            return
        prod = self.productos[id_producto]
        if cantidad is not None:
            prod.set_cantidad(cantidad)
        if precio is not None:
            prod.set_precio(precio)
        self._guardar_inventario()
        print(f"✅ Producto ID {id_producto} actualizado.")

    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """Búsqueda optimizada: list comprehension sobre dict values."""
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("\n📋 INVENTARIO COMPLETO:")
        for prod in self.productos.values():
            print(f"ID: {prod.get_id()} | {prod.get_nombre():<20} | Cant: {prod.get_cantidad():>3} | Precio: ${prod.get_precio():>7.2f}")

    def _guardar_inventario(self):
        """Serializa dict a JSON."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                data = {id_p: p.to_dict() for id_p, p in self.productos.items()}
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Error guardando: {e}")

    def _cargar_inventario(self):
        """Deserializa JSON a dict de Productos."""
        if not os.path.exists(self.archivo):
            print("📄 Archivo no existe, inventario vacío.")
            return
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.productos = {id_p: Producto.from_dict(p) for id_p, p in data.items()}
            print(f"✅ Cargados {len(self.productos)} productos desde {self.archivo}.")
        except json.JSONDecodeError:
            print("⚠️ Archivo JSON corrupto, inicio vacío.")
        except Exception as e:
            print(f"⚠️ Error cargando: {e}")

def menu():
    inv = Inventario()
    while True:
        print("\n=== SISTEMA AVANZADO DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Eliminar por ID")
        print("3. Actualizar por ID")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == '1':
            nombre = input("Nombre: ").strip()
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.agregar_producto(nombre, cantidad, precio)
        elif opcion == '2':
            id_p = input("ID: ").strip()
            inv.eliminar_producto(id_p)
        elif opcion == '3':
            id_p = input("ID: ").strip()
            cant = input("Nueva cantidad (Enter=sin cambio): ")
            prec = input("Nuevo precio (Enter=sin cambio): ")
            cantidad = int(cant) if cant.strip() else None
            precio = float(prec) if prec.strip() else None
            inv.actualizar_producto(id_p, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre a buscar: ").strip()
            resultados = inv.buscar_por_nombre(nombre)
            if resultados:
                print("Resultados:")
                for p in resultados:
                    print(f"ID: {p.get_id()} | {p.get_nombre()} | Cant: {p.get_cantidad()} | ${p.get_precio()}")
            else:
                print("No encontrado.")
        elif opcion == '5':
            inv.mostrar_todos()
        elif opcion == '0':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
