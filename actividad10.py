import tkinter as tk
import sqlite3

class RegistroAlumnosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Alumnos")

       
        self.conexion = sqlite3.connect("registro_alumnos.db")
        self.cursor = self.conexion.cursor()

        
        self.crear_tabla_alumnos()

        
        self.crear_interfaz()

    def crear_tabla_alumnos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT,
                            edad INTEGER,
                            carrera TEXT)''')
        self.conexion.commit()

    def crear_interfaz(self):
        
        self.label_id = tk.Label(self.root, text="ID:", fg="purple", font=("Times New Roman", 22))
        self.label_id.grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(self.root, fg="purple", font=("Times New Roman", 22))
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        self.label_nombre = tk.Label(self.root, text="Nombre:", fg="purple", font=("Times New Roman", 22))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(self.root, fg="purple", font=("Times New Roman", 22))
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        self.label_edad = tk.Label(self.root, text="Edad:", fg="purple", font=("Times New Roman", 22))
        self.label_edad.grid(row=2, column=0, padx=10, pady=5)
        self.entry_edad = tk.Entry(self.root, fg="purple", font=("Times New Roman", 22))
        self.entry_edad.grid(row=2, column=1, padx=10, pady=5)

        self.label_carrera = tk.Label(self.root, text="Carrera:", fg="purple", font=("Times New Roman", 22))
        self.label_carrera.grid(row=3, column=0, padx=10, pady=5)
        self.entry_carrera = tk.Entry(self.root, fg="purple", font=("Times New Roman", 22))
        self.entry_carrera.grid(row=3, column=1, padx=10, pady=5)

        
        self.guardar_button = tk.Button(self.root, text="Guardar", command=self.guardar_alumno, fg="purple", font=("Times New Roman", 22))
        self.guardar_button.grid(row=4, column=0, padx=10, pady=5)

        self.mostrar_button = tk.Button(self.root, text="Mostrar", command=self.mostrar_alumnos, fg="purple", font=("Times New Roman", 22))
        self.mostrar_button.grid(row=4, column=1, padx=10, pady=5)

    def guardar_alumno(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        carrera = self.entry_carrera.get()

        
        self.cursor.execute("INSERT INTO alumnos (id, nombre, edad, carrera) VALUES (?, ?, ?, ?)", (id, nombre, edad, carrera))
        self.conexion.commit()

        
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_carrera.delete(0, tk.END)

    def mostrar_alumnos(self):
        
        self.cursor.execute("SELECT * FROM alumnos")
        alumnos = self.cursor.fetchall()

        
        ventana_mostrar = tk.Toplevel(self.root)
        ventana_mostrar.title("Lista de Alumnos")

        for i, alumno in enumerate(alumnos):
            tk.Label(ventana_mostrar, text=f"ID: {alumno[0]} - Nombre: {alumno[1]} - Edad: {alumno[2]} - Carrera: {alumno[3]}", fg="purple", font=("Times New Roman", 22)).grid(row=i, column=0, padx=10, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroAlumnosApp(root)
    root.mainloop()
