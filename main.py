import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas Moderno")
        self.master.geometry("400x450")

        # --- Interfaz Gráfica ---

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.master, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)

        # Vincular la tecla Enter para añadir tareas
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botones de control
        self.btn_frame = tk.Frame(self.master)
        self.btn_frame.pack(pady=5)

        self.add_button = tk.Button(self.btn_frame, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.btn_frame, text="Completar", command=self.mark_completed, bg="#2196f3", fg="white")
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.btn_frame, text="Eliminar", command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.grid(row=0, column=2, padx=5)

        # Listbox para mostrar las tareas
        self.tasks_listbox = tk.Listbox(self.master, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Evento: Doble clic para completar tarea
        self.tasks_listbox.bind('<Double-1>', lambda event: self.mark_completed())

    # --- Lógica de la Aplicación ---

    def add_task(self):
        """Añade una tarea a la lista si el campo no está vacío."""
        task = self.task_entry.get()
        if task.strip() != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar el campo
        else:
            messagebox.showwarning("Advertencia", "¡Debes escribir algo!")

    def mark_completed(self):
        """Modifica visualmente la tarea seleccionada para marcarla como hecha."""
        try:
            index = self.tasks_listbox.curselection()[0]
            task_text = self.tasks_listbox.get(index)

            if "[HECHO]" not in task_text:
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"[HECHO] {task_text}")
                self.tasks_listbox.itemconfig(index, fg="gray")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea de la lista.")

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona la tarea que deseas eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()