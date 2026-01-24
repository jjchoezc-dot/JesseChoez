# Programa que demuestra constructores (__init__) y destructores (__del__) en Python
# El constructor __init__ se llama automáticamente al crear un objeto (instanciación).
# El destructor __del__ se llama cuando el objeto ya no es referenciado (cuenta de referencias = 0)
# o con 'del objeto', pero NO es determinístico debido al recolector de basura de Python.[web:2][web:6]

class ContadorSimple:
    """Clase simple para demostrar creación y destrucción básica."""

    def __init__(self, nombre):
        # Constructor: inicializa atributos y realiza setup inicial.
        self.nombre = nombre
        self.valor = 0
        print(f"Constructor llamado: Contador '{self.nombre}' creado con valor {self.valor}")

    def incrementar(self):
        self.valor += 1
        print(f"{self.nombre} incrementado a {self.valor}")

    def __del__(self):
        # Destructor: se activa al destruir el objeto. Aquí solo imprime un mensaje de limpieza.
        # Útil para logging o stats, pero NO para recursos críticos (usa context managers con 'with').[web:11][web:13]
        print(f"Destructor llamado: Contador '{self.nombre}' destruido (limpieza: reset stats)")


class ManejadorArchivo:
    """Clase para manejo de archivos: abre en __init__, cierra en __del__."""

    def __init__(self, nombre_archivo, modo='w'):
        # Constructor: inicializa atributos y abre el archivo (recurso externo).
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = open(nombre_archivo, modo)  # Abre el archivo
        print(f"Constructor llamado: Archivo '{self.nombre_archivo}' abierto en modo '{modo}'")

    def escribir(self, texto):
        if self.archivo:
            self.archivo.write(texto + '\n')
            print(f"Escrito en {self.nombre_archivo}: {texto}")

    def __del__(self):
        # Destructor: verifica si el archivo está abierto y lo cierra (limpieza de recurso).
        # Se activa cuando el objeto es recolectado por garbage collector.
        # Nota: Mejor usar 'with open()' para garantía inmediata, pero aquí demostramos __del__.[web:11]
        if hasattr(self, 'archivo') and not self.archivo.closed:
            self.archivo.close()
            print(f"Destructor llamado: Archivo '{self.nombre_archivo}' cerrado correctamente")


# Ejemplo de uso principal
if __name__ == "__main__":
    print("=== Demostración de Constructores y Destructores ===\n")

    # Crear objetos: llama __init__
    contador1 = ContadorSimple("ContadorA")
    contador1.incrementar()

    archivo = ManejadorArchivo("ejemplo.txt", "w")
    archivo.escribir("Hola desde la clase")
    archivo.escribir("Línea 2 con destructor")

    # Eliminar explícitamente: acelera llamada a __del__
    print("\n--- Eliminando contador1 ---")
    del contador1  # Llama __del__ pronto

    print("\n--- Fin del script, objetos restantes se destruyen automáticamente ---")
    # Al salir, Python destruye objetos restantes y llama __del__
