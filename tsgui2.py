import tkinter as tk
from tkinter import messagebox
import psutil

def obtener_discos():
    # Obtener la lista de discos duros
    discos = psutil.disk_partitions()
    return [disco.device for disco in discos]

def mostrar_seleccion():
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        valor = listbox.get(indice)
        messagebox.showinfo("Selección", f"Has seleccionado: {valor}")
    else:
        messagebox.showwarning("Advertencia", "No has seleccionado nada.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Discos Duros Disponibles")
ventana.geometry("400x300")

# Crear un Listbox
listbox = tk.Listbox(ventana, selectmode=tk.SINGLE)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Obtener la lista de discos duros y llenar el Listbox
discos = obtener_discos()
for disco in discos:
    listbox.insert(tk.END, disco)

# Crear un botón para mostrar la selección
boton = tk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()
