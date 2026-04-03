import tkinter as tk
from tkinter import messagebox


class GestorTareasApp:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.root = root
        self.root.title("Gestor de Tareas Pro - UEA")
        self.root.geometry("400x500")

        # --- Interfaz Gráfica ---

        # Título y campo de entrada
        self.label = tk.Label(root, text="Escribe una nueva tarea:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entrada_tarea = tk.Entry(root, font=("Arial", 14), width=30)
        self.entrada_tarea.pack(pady=5)
        self.entrada_tarea.focus_set()  # Pone el cursor en el campo al iniciar

        # Botones de acción
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar (Enter)", command=self.agregar_tarea,
                                     bg="#d4edda")
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(self.frame_botones, text="Completar (C)", command=self.marcar_completada,
                                       bg="#fff3cd")
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar (Del)", command=self.eliminar_tarea,
                                      bg="#f8d7da")
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas (Listbox)
        self.lista_tareas = tk.Listbox(root, font=("Arial", 12), width=40, height=15, selectmode=tk.SINGLE)
        self.lista_tareas.pack(pady=10, padx=20)

        # --- Configuración de Atajos de Teclado (Event Binding) ---

        # Añadir con Enter
        self.entrada_tarea.bind('<Return>', lambda event: self.agregar_tarea())

        # Marcar completada con tecla 'C' o 'c'
        self.root.bind('<c>', lambda event: self.marcar_completada())
        self.root.bind('<C>', lambda event: self.marcar_completada())

        # Eliminar con tecla 'Delete' o 'd'
        self.root.bind('<Delete>', lambda event: self.eliminar_tarea())
        self.root.bind('<d>', lambda event: self.eliminar_tarea())

        # Cerrar con Escape
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    # --- Funcionalidades ---

    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea.strip():
            self.lista_tareas.insert(tk.END, f" {tarea}")
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "No puedes agregar una tarea vacía.")

    def marcar_completada(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            tarea_actual = self.lista_tareas.get(indice)

            # Si ya está completada, no hacer nada
            if "✔" in tarea_actual:
                return

            # Feedback visual: Añadimos un check y cambiamos el color de fondo del ítem
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, f"✔ {tarea_actual.strip()}")
            self.lista_tareas.itemconfig(indice, fg="gray", bg="#e2e3e5")
        except IndexError:
            messagebox.showwarning("Selección", "Por favor, selecciona una tarea para completar.")

    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(indice)
        except IndexError:
            messagebox.showwarning("Selección", "Selecciona la tarea que deseas eliminar.")


# --- Inicialización de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()