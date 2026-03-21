import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Requiere: pip install tkcalendar


class AgendaApp:
    def __init__(self, app_ventana):
        self.root = app_ventana
        self.root.title("Agenda Personal - UEA")
        self.root.geometry("750x550")

        # --- CONTENEDORES (ORGANIZACIÓN POR FRAMES) ---
        self.frame_entrada = tk.LabelFrame(self.root, text="Detalles del Nuevo Evento", padx=15, pady=15)
        self.frame_entrada.pack(padx=20, pady=15, fill="x")

        self.frame_lista = tk.Frame(self.root, padx=10, pady=10)
        self.frame_lista.pack(padx=20, pady=5, fill="both", expand=True)

        self.frame_acciones = tk.Frame(self.root, padx=10, pady=10)
        self.frame_acciones.pack(padx=20, pady=15, fill="x")

        # --- COMPONENTES DE ENTRADA ---
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, sticky="w", padx=5)
        # DatePicker (Componente Avanzado solicitado)
        self.ent_fecha = DateEntry(self.frame_entrada, width=12, background='darkblue',
                                   foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.ent_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", padx=5)
        self.ent_hora = tk.Entry(self.frame_entrada)
        self.ent_hora.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, sticky="w", padx=5)
        self.ent_desc = tk.Entry(self.frame_entrada, width=55)
        self.ent_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # --- TREEVIEW (VISUALIZACIÓN DE EVENTOS) ---
        columnas = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings")

        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción del Evento")

        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=100, anchor="center")
        self.tree.column("descripcion", width=450)

        # Corrección del Scrollbar
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.config(yscrollcommand=scrollbar.set)  # Cambio aquí para evitar el error de PyCharm

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- BOTONES DE ACCIÓN ---
        tk.Button(self.frame_acciones, text="➕ Agregar Evento", command=self.agregar_evento,
                  bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), padx=10).pack(side="left", padx=5)

        tk.Button(self.frame_acciones, text="🗑️ Eliminar Seleccionado", command=self.eliminar_evento,
                  bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), padx=10).pack(side="left", padx=5)

        tk.Button(self.frame_acciones, text="🚪 Salir", command=self.root.quit,
                  bg="#95a5a6", fg="white", padx=15).pack(side="right", padx=5)

    def agregar_evento(self):
        fecha = self.ent_fecha.get()
        hora = self.ent_hora.get()
        desc = self.ent_desc.get()

        if hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            self.ent_hora.delete(0, tk.END)
            self.ent_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Por favor completa la hora y descripción.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            if messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento seleccionado?"):
                for item in seleccion:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Error", "Selecciona un evento de la tabla primero.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

