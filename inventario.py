# Descripción: Implementa clases Producto e Inventario con menú consola interactivo.
# Usa lista para almacenar productos (estructura simple y eficiente).
# ID único generado automáticamente para evitar duplicados.
# NUEVO: Persistencia en archivo inventario.txt + Manejo de excepciones

import os
from datetime import datetime


class Producto:
    def __init__(self, nombre, cantidad, precio):
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

    def set_id(self, id_val):
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
    def __init__(self, archivo="inventario.txt"):
        self._productos = []
        self._archivo = archivo
        self._cargar_inventario()

    def _cargar_inventario(self):
        """Carga productos desde archivo al iniciar"""
        try:
            if not os.path.exists(self._archivo):
                print("Archivo " + self._archivo + " no existe. Creando nuevo...")
                self._guardar_inventario()
                return

            with open(self._archivo, 'r', encoding='utf-8') as f:
                lineas = f.readlines()

            self._productos.clear()
            for i, linea in enumerate(lineas, 1):
                linea = linea.strip()
                if not linea or linea.startswith('#'):
                    continue

                partes = linea.split('|')
                if len(partes) >= 4:
                    try:
                        _, id_val, nombre, cantidad, precio = partes
                        producto = Producto(nombre.strip(), int(cantidad), float(precio))
                        producto.set_id(int(id_val))
                        self._productos.append(producto)
                    except (ValueError, IndexError):
                        print("Linea " + str(i) + " ignorada (formato invalido)")

            print("Cargados " + str(len(self._productos)) + " productos desde " + self._archivo)

        except PermissionError:
            print("Sin permisos para leer " + self._archivo)
        except Exception as e:
            print("Error cargando inventario: " + str(e))

    def _guardar_inventario(self):
        """Guarda todos los productos en archivo"""
        try:
            with open(self._archivo, 'w', encoding='utf-8') as f:
                f.write("# Inventario - " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
                f.write("# Formato: dummy|id|nombre|cantidad|precio\n\n")

                for producto in self._productos:
                    linea = "dummy|" + str(producto.get_id()) + "|" + producto.get_nombre() + "|" + str(
                        producto.get_cantidad()) + "|" + str(producto.get_precio()) + "\n"
                    f.write(linea)

            print("Guardado exitosamente en " + self._archivo)
            return True

        except PermissionError:
            print("Sin permisos para escribir en " + self._archivo)
            return False
        except Exception as e:
            print("Error guardando: " + str(e))
            return False

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_id = len(self._productos) + 1
        if any(p.get_id() == nuevo_id for p in self._productos):
            print("Error: ID duplicado.")
            return False

        producto = Producto(nombre, cantidad, precio)
        producto.set_id(nuevo_id)
        self._productos.append(producto)

        if self._guardar_inventario():
            print("Producto '" + nombre + "' (ID " + str(nuevo_id) + ") agregado Y GUARDADO")
        else:
            print("Producto agregado en memoria, pero NO guardado en archivo")

        return True

    def eliminar_producto(self, id_val):
        for i, p in enumerate(self._productos):
            if p.get_id() == id_val:
                eliminado = self._productos.pop(i)
                print("Producto '" + eliminado.get_nombre() + "' eliminado.")

                if self._guardar_inventario():
                    print("Archivo actualizado")
                return True
        return None
