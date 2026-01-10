"""
Programa: Calculadora de Áreas Geométricas - Tarea Tipos de Datos
Nombre: JESSE JAMES CHOEZ CHAVEZ
Fecha: 10 Enero 2026

Descripción: Programa que demuestra tipos de datos Python (int, float, str, bool)
usando snake_case. Calcula áreas de figuras geométricas ingresadas por usuario.

Uso:
1. Selecciona figura: triangulo, circulo o rectangulo
2. Ingresa medidas requeridas
3. Obtén área calculada

Tecnologías: PyCharm  + GitHub
"""

"""
Programa: Calculadora de Área de Figuras Geométricas
Autor: Estudiante
Fecha: Enero 2026
Descripción: Calcula el área de triángulos, círculos o rectángulos usando diferentes tipos de datos Python.
snake_case para todos los identificadores según PEP 8.
"""

# Tipos de datos: int, float, str, bool
figura_seleccionada = input("Selecciona figura (triangulo/circulo/rectangulo): ").lower().strip()
es_valido = False

# Validación booleana (tipo bool)
if figura_seleccionada in ["triangulo", "circulo", "rectangulo"]:
    es_valido = True
    print("Figura válida seleccionada.")  # Mensaje string (tipo str)
else:
    print("Error: Figura no reconocida. Terminando programa.")

# Solo continúa si es_valido == True
if es_valido:
    # Datos de entrada como float para precisión decimal
    lado_1 = float(input("Ingresa primer valor (ej. base): "))
    lado_2 = float(input("Ingresa segundo valor (ej. altura): "))

    # int para número entero de π aproximado
    pi_aproximado = 3

    # Cálculos según figura (usando snake_case)
    if figura_seleccionada == "triangulo":
        area_triangulo = (lado_1 * lado_2) / 2
        print(f"Área del triángulo: {area_triangulo:.2f} unidades cuadradas")

    elif figura_seleccionada == "rectangulo":
        area_rectangulo = lado_1 * lado_2
        print(f"Área del rectángulo: {area_rectangulo:.2f} unidades cuadradas")

    elif figura_seleccionada == "circulo":
        # Radio como float, usa int para π
        radio_cuadrado = lado_1 ** 2
        area_circulo = pi_aproximado * radio_cuadrado
        print(f"Área del círculo (π≈{pi_aproximado}): {area_circulo:.2f} unidades cuadradas")

print("Programa finalizado.")
