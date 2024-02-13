import tkinter as tk
from tkinter import messagebox
import random

def generarContrasena():
    longitud = varLongitud.get()
    if longitud not in [8, 12, 15]:
        messagebox.showerror("Error", "Por favor selecciona una longitud válida (8, 12, o 15)")
        return
    
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    simbolos = '#$%&/!'
    numeros = '1234567890'

    caracteres = ''
    if varMinusculas.get():
        caracteres += minusculas
    if varMayusculas.get():
        caracteres += mayusculas
    if varNumeros.get():
        caracteres += numeros
    if varSimbolos.get():
        caracteres += simbolos
    
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    lblContrasena.config(text="Tu nueva contraseña es: " + contrasena)

def copiarContrasena():
    ventana.clipboard_clear()
    ventana.clipboard_append(lblContrasena.cget("text").split(": ")[1])

ventana = tk.Tk()
ventana.title("Generador de Contraseña")
ventana.geometry("500x300")
ventana.resizable(width=False, height=False)

marco = tk.Frame(ventana)
marco.pack(pady=10)

varMinusculas = tk.BooleanVar()
varMinusculas.set(True)
varMayusculas = tk.BooleanVar()
varMayusculas .set(True)
varNumeros = tk.BooleanVar()
varNumeros.set(True)
varSimbolos = tk.BooleanVar()
varSimbolos.set(True)
varLongitud = tk.IntVar()
varLongitud.set(8)

lblInstruccion = tk.Label(marco, text="Selecciona los tipos de caracteres y la longitud para tu contraseña:")
lblInstruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

chkMinusculas = tk.Checkbutton(marco, text="Minúsculas", variable=varMinusculas)
chkMinusculas.grid(row=1, column=0, sticky=tk.W, padx=10)

chkMayusculas = tk.Checkbutton(marco, text="Mayúsculas", variable=varMayusculas)
chkMayusculas.grid(row=2, column=0, sticky=tk.W, padx=10)

chkNumeros = tk.Checkbutton(marco, text="Números", variable=varNumeros)
chkNumeros.grid(row=3, column=0, sticky=tk.W, padx=10)

chkSimbolos = tk.Checkbutton(marco, text="Símbolos", variable=varSimbolos)
chkSimbolos.grid(row=4, column=0, sticky=tk.W, padx=10)

lblLongitud = tk.Label(marco, text="Longitud:")
lblLongitud.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

optLongitud = tk.OptionMenu(marco, varLongitud, 8, 12, 15)
optLongitud.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

btnGenerar = tk.Button(marco, text="Generar Contraseña", command=generarContrasena)
btnGenerar.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

lblContrasena = tk.Label(marco, text="")
lblContrasena.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

btnCopiar = tk.Button(marco, text="Copiar Contraseña", command=copiarContrasena)
btnCopiar.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

ventana.mainloop()
