import os
import subprocess
import sys
from pathlib import Path


class Dashboard:
    """
    Dashboard OOP para gestión de proyectos Programación Orientada a Objetos.
    Personalizado para estudiante UEA - Guayaquil, EC. Soporta Windows/PyCharm.
    """

    def __init__(self):
        self.ruta_base = Path(__file__).parent  # Ruta dinámica al dashboard
        self.unidades = {
            '1': 'Unidad 1 - Conceptos Básicos OOP',
            '2': 'Unidad 2 - Herencia y Polimorfismo',
            '3': 'Mis Proyectos POO',  # Personalizado para tus tareas
            'g': 'Git - Gestión Repositorio'
        }

    def mostrar_codigo(self, ruta_script: Path) -> str | None:
        """Muestra código fuente con manejo robusto de errores."""
        try:
            codigo = ruta_script.read_text(encoding='utf-8')
            print(f"\n--- Código de {ruta_script.name} ---\n{codigo}\n")
            return codigo
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {ruta_script}")
            return None
        except Exception as e:
            print(f"❌ Error lectura: {e}")
            return None

    def ejecutar_codigo(self, ruta_script: Path):
        """Ejecución optimizada para Windows: nueva ventana cmd."""
        try:
            cmd = ['start', 'cmd', '/k',
                   f'python "{ruta_script.absolute()}" & echo. & echo Presiona cualquier tecla para cerrar... & pause >nul']
            subprocess.run(cmd, shell=True, check=True)
            print(f"✅ Ejecutando {ruta_script.name} en nueva ventana...")
        except Exception as e:
            print(f"❌ Error ejecución: {e}")

    def git_action(self, accion: str):
        """Acciones Git: pull, status, push."""
        try:
            if accion == 'pull':
                subprocess.run(['git', 'pull'], cwd=self.ruta_base, check=True)
                print("✅ Git pull completado.")
            elif accion == 'status':
                result = subprocess.run(['git', 'status', '-s'], cwd=self.ruta_base, capture_output=True, text=True)
                print("\n--- Git Status ---\n" + result.stdout)
            elif accion == 'push':
                subprocess.run(['git', 'add', '.'], cwd=self.ruta_base, check=True)
                subprocess.run(['git', 'commit', '-m', 'Actualización Dashboard POO'], cwd=self.ruta_base, check=True)
                subprocess.run(['git', 'push'], cwd=self.ruta_base, check=True)
                print("✅ Git push completado.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error Git ({accion}): {e}")

    def mostrar_menu_principal(self):
        """Menú principal con opciones OOP."""
        while True:
            print("\n" + "=" * 50)
            print("🚀 DASHBOARD POO - Programación Orientada a Objetos UEA")
            print("=" * 50)
            for key, nombre in self.unidades.items():
                print(f"{key.upper()} - {nombre}")
            print("0 - Salir")

            eleccion = input("\n👉 Elige opción: ").strip().lower()
            if eleccion == '0':
                print("👋 ¡Gracias por usar Dashboard POO!")
                sys.exit(0)
            elif eleccion in self.unidades:
                if eleccion == 'g':
                    self._menu_git()
                else:
                    self._mostrar_sub_menu(self.unidades[eleccion])
            else:
                print("❌ Opción inválida. Intenta de nuevo.")

    def _menu_git(self):
        """Submenú Git personalizado para tus hábitos."""
        while True:
            print("\n--- Menú Git ---")
            print("1 - Git Pull (actualizar)")
            print("2 - Git Status")
            print("3 - Git Add/Commit/Push")
            print("0 - Regresar")

            op = input("👉 Elige: ").strip()
            if op == '1':
                self.git_action('pull')
            elif op == '2':
                self.git_action('status')
            elif op == '3':
                self.git_action('push')
            elif op == '0':
                break
            else:
                print("❌ Inválido.")
            input("\nPresiona Enter para continuar...")

    def _mostrar_sub_menu(self, nombre_unidad: str):
        """Submenú por unidad: lista subcarpetas."""
        ruta_unidad = self.ruta_base / nombre_unidad
        if not ruta_unidad.exists():
            print(f"❌ Carpeta no existe: {ruta_unidad}")
            return

        sub_carpetas = [p.name for p in ruta_unidad.iterdir() if p.is_dir()]
        while True:
            print(f"\n📁 {nombre_unidad}")
            for i, carpeta in enumerate(sub_carpetas, 1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")

            try:
                eleccion = int(input("👉 Elige: ")) - 1
                if eleccion == -1: break
                if 0 <= eleccion < len(sub_carpetas):
                    self._mostrar_scripts(ruta_unidad / sub_carpetas[eleccion])
            except ValueError:
                print("❌ Ingresa número válido.")

    def _mostrar_scripts(self, ruta_sub: Path):
        """Lista y maneja scripts Python."""
        scripts = [p for p in ruta_sub.iterdir() if p.suffix == '.py']
        while True:
            print(f"\n🐍 Scripts en {ruta_sub.name}:")
            for i, script in enumerate(scripts, 1):
                print(f"{i} - {script.name}")
            print("0 - Regresar")

            try:
                eleccion = int(input("👉 Elige: ")) - 1
                if eleccion == -1: break
                if 0 <= eleccion < len(scripts):
                    script = scripts[eleccion]
                    self.mostrar_codigo(script)
                    if input("🔥 ¿Ejecutar? (s/n): ").lower() == 's':
                        self.ejecutar_codigo(script)
                    input("\nPresiona Enter...")
            except ValueError:
                print("❌ Número inválido.")


# Ejecutar Dashboard
if __name__ == "__main__":
    app = Dashboard()
    app.mostrar_menu_principal()
