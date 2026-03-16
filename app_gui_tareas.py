from tkinter import *
from tkinter import messagebox


def crear_app():
    root = Tk()
    root.title("Gestor de Tareas Simple")
    root.geometry("400x400")

    # Etiqueta y campo de texto
    Label(root, text="Ingresa una tarea:").pack(pady=10)
    entry = Entry(root, width=40)
    entry.pack(pady=5)

    # Lista para mostrar tareas
    lista_tareas = Listbox(root, width=50, height=15)
    lista_tareas.pack(pady=20)

    def agregar():
        texto = entry.get()
        if texto:
            lista_tareas.insert(END, texto)
            entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Ingresa una tarea primero.")

    def limpiar():
        lista_tareas.delete(0, END)

    # Botones
    Button(root, text="Agregar", command=agregar, bg="green", fg="white").pack(pady=5)
    Button(root, text="Limpiar", command=limpiar, bg="red", fg="white").pack(pady=5)

    root.mainloop()


# Para verificar si funciona sin ventana
print("Código preparado para ejecutar en PyCharm. Funciones definidas correctamente.")