# Sistema de Gestión de Biblioteca Digital
# Autor: Jesse James Choez Chavez
# Universidad Estatal Amazónica (UEA)
# Implementación usando POO con colecciones específicas: tuplas, listas, diccionarios y conjuntos [web:6][web:7][cite:1]

from typing import Tuple, List, Dict, Set, Optional

class Libro:
    """
    Clase Libro: Representa un libro con atributos inmutables (título, autor como tupla)
    y mutables (categoría, ISBN único). Usa tupla para autor y título por inmutabilidad [web:6][web:10].
    """
    def __init__(self, titulo: str, autor: Tuple[str, str], categoria: str, isbn: str):
        self._titulo_autor = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # Estado de disponibilidad

    @property
    def titulo(self) -> str:
        return self._titulo_autor[0]

    @property
    def autor(self) -> Tuple[str, str]:
        return self._titulo_autor[1]

    def __str__(self) -> str:
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    """
    Clase Usuario: Maneja usuarios con ID único y lista de libros prestados [web:8][web:15].
    """
    def __init__(self, nombre: str, user_id: str):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados: List[str] = []  # Lista de ISBNs prestados

    def listar_prestados(self) -> List[str]:
        """Retorna lista de ISBNs prestados."""
        return self.libros_prestados[:]

    def __str__(self) -> str:
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

class Biblioteca:
    """
    Clase principal Biblioteca: Usa diccionario {ISBN: Libro} para libros eficientes,
    conjunto de user_ids únicos, dict {user_id: Usuario} para usuarios [web:7][web:9][web:13].
    """
    def __init__(self):
        self.libros: Dict[str, Libro] = {}  # Diccionario ISBN -> Libro
        self.usuarios: Dict[str, Usuario] = {}  # Dict user_id -> Usuario
        self.user_ids: Set[str] = set()  # Conjunto IDs únicos

    def agregar_libro(self, libro: Libro) -> bool:
        """Añade libro si ISBN no existe."""
        if libro.isbn in self.libros:
            print(f"Libro con ISBN {libro.isbn} ya existe.")
            return False
        self.libros[libro.isbn] = libro
        return True

    def quitar_libro(self, isbn: str) -> bool:
        """Quita libro si existe y no está prestado."""
        if isbn not in self.libros:
            print(f"Libro ISBN {isbn} no encontrado.")
            return False
        libro = self.libros[isbn]
        if not libro.disponible:
            print(f"Libro {isbn} está prestado.")
            return False
        del self.libros[isbn]
        return True

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra usuario si ID único."""
        if usuario.user_id in self.user_ids:
            print(f"Usuario ID {usuario.user_id} ya registrado.")
            return False
        self.usuarios[usuario.user_id] = usuario
        self.user_ids.add(usuario.user_id)
        return True

    def dar_baja_usuario(self, user_id: str) -> bool:
        """Da de baja usuario si no tiene préstamos."""
        if user_id not in self.user_ids:
            print(f"Usuario {user_id} no encontrado.")
            return False
        if self.usuarios[user_id].libros_prestados:
            print(f"Usuario {user_id} tiene préstamos pendientes.")
            return False
        del self.usuarios[user_id]
        self.user_ids.remove(user_id)
        return True

    def prestar_libro(self, isbn: str, user_id: str) -> bool:
        """Presta libro si disponible y usuario existe."""
        if user_id not in self.user_ids:
            print(f"Usuario {user_id} no registrado.")
            return False
        if isbn not in self.libros:
            print(f"Libro {isbn} no existe.")
            return False
        libro = self.libros[isbn]
        if not libro.disponible:
            print(f"Libro {isbn} no disponible.")
            return False
        libro.disponible = False
        self.usuarios[user_id].libros_prestados.append(isbn)
        return True

    def devolver_libro(self, isbn: str, user_id: str) -> bool:
        """Devuelve libro si prestado al usuario."""
        if user_id not in self.user_ids or isbn not in self.libros:
            return False
        usuario = self.usuarios[user_id]
        if isbn not in usuario.libros_prestados:
            print(f"Libro {isbn} no prestado a {user_id}.")
            return False
        usuario.libros_prestados.remove(isbn)
        self.libros[isbn].disponible = True
        return True

    def buscar_libros(self, valor: str) -> List[Libro]:
        """Busca por título, autor (nombre o apellido), o categoría."""
        resultados = []
        for libro in self.libros.values():
            if (valor.lower() in libro.titulo.lower() or
                valor.lower() in libro.autor[0].lower() or
                valor.lower() in libro.autor[1].lower() or
                valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_prestados_usuario(self, user_id: str) -> Optional[List[str]]:
        """Lista libros prestados de un usuario."""
        if user_id in self.usuarios:
            return self.usuarios[user_id].libros_prestados
        return None

# Pruebas del sistema
def main():
    biblio = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien Años de Soledad", ("Gabriel", "García Márquez"), "Novela", "978-0307474728")
    libro2 = Libro("1984", ("George", "Orwell"), "Distopía", "978-0451524935")
    libro3 = Libro("Clean Code", ("Robert", "Martin"), "Programación", "978-0132350884")
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    # Registrar usuarios
    user1 = Usuario("Jesse Choez", "UEA001")
    user2 = Usuario("Ana López", "UEA002")
    biblio.registrar_usuario(user1)
    biblio.registrar_usuario(user2)

    # Préstamos
    biblio.prestar_libro("978-0307474728", "UEA001")
    biblio.prestar_libro("978-0451524935", "UEA002")

    # Búsquedas
    print("Búsqueda por 'García':")
    for l in biblio.buscar_libros("García"):
        print(l)

    print("\nLibros prestados a Jesse (UEA001):", biblio.listar_prestados_usuario("UEA001"))

    # Devolución
    biblio.devolver_libro("978-0307474728", "UEA001")

    print("\nDespués de devolución:", biblio.listar_prestados_usuario("UEA001"))

    print("\n¡Sistema funcionando correctamente!")

if __name__ == "__main__":
    main()
