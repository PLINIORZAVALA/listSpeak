# Proceso para que la interfas haga escuchar el audio de la palabra
from translate import Translator
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Inicialización de herramientas
translator = Translator(from_lang="en", to_lang="es")
engine = pyttsx3.init()

def configurar_tts(rate=100, volume=0.9):
    """Configura el motor de texto a voz con velocidad y volumen especificados."""
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

def traducir_texto(texto_ingles):
    """Traduce texto de inglés a español."""
    try:
        return translator.translate(texto_ingles)
    except Exception as e:
        messagebox.showerror("Error de Traducción", f"No se pudo traducir el texto: {e}")
        return None

def reproducir_texto(texto_ingles):
    """Reproduce el texto en inglés usando el motor de texto a voz."""
    if texto_ingles:
        engine.say(texto_ingles)
        engine.runAndWait()

def manejar_traduccion():
    """Maneja la traducción y muestra el resultado en la interfaz."""
    texto_ingles = entry_texto.get()
    if texto_ingles:
        traduccion_espanol = traducir_texto(texto_ingles)
        if traduccion_espanol:
            label_traduccion.config(text=f"Traducción en español: {traduccion_espanol}")
    else:
        messagebox.showwarning("Texto vacío", "Por favor ingresa un texto en inglés.")

def manejar_reproduccion():
    """Maneja la reproducción de texto en inglés."""
    texto_ingles = entry_texto.get()
    if texto_ingles:
        reproducir_texto(texto_ingles)
    else:
        messagebox.showwarning("Texto vacío", "Por favor ingresa un texto en inglés para reproducir.")

def crear_interfaz():
    """Crea la interfaz gráfica principal."""
    ventana = tk.Tk()
    ventana.title("Traductor y Lector de Inglés")
    ventana.geometry("400x300")
    
    tk.Label(ventana, text="Texto en inglés:").pack(pady=5)

    global entry_texto
    entry_texto = tk.Entry(ventana, width=50)
    entry_texto.pack(pady=5)

    tk.Button(ventana, text="Traducir a español", command=manejar_traduccion).pack(pady=10)

    global label_traduccion
    label_traduccion = tk.Label(ventana, text="Traducción en español: ", wraplength=350, justify="left")
    label_traduccion.pack(pady=5)

    tk.Button(ventana, text="Escuchar en inglés", command=manejar_reproduccion).pack(pady=10)

    ventana.mainloop()

# Configuración inicial del motor de texto a voz
configurar_tts()

# Lanzar la interfaz
crear_interfaz()
