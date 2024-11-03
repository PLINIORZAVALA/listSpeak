import os
from translate import Translator
from gtts import gTTS
import pygame
import tkinter as tk
from tkinter import messagebox

# Inicialización del traductor y la ruta de audio
translator = Translator(from_lang="en", to_lang="es")
ruta_audio = 'pruebas/listening/listenDowload'
nombre_archivo = 'audio_ingles.mp3'
ruta_completa_audio = os.path.join(ruta_audio, nombre_archivo)

# Configuración para `pygame`
pygame.mixer.init()

def traducir_texto(texto_ingles):
    try:
        return translator.translate(texto_ingles)
    except Exception as e:
        messagebox.showerror("Error de Traducción", f"No se pudo traducir el texto: {e}")
        return None

def guardar_audio(texto_ingles):
    try:
        tts = gTTS(text=texto_ingles, lang='en')
        os.makedirs(ruta_audio, exist_ok=True)
        tts.save(ruta_completa_audio)
        return ruta_completa_audio
    except Exception as e:
        messagebox.showerror("Error al Guardar Audio", f"No se pudo guardar el audio: {e}")
        return None

def reproducir_audio():
    try:
        if os.path.exists(ruta_completa_audio):
            # Reproducir el audio
            pygame.mixer.music.load(ruta_completa_audio)
            pygame.mixer.music.play()
        else:
            messagebox.showwarning("Audio no encontrado", "No se ha generado el audio aún.")
    except Exception as e:
        messagebox.showerror("Error de Reproducción", f"No se pudo reproducir el audio: {e}")

# Interfaz gráfica
def manejar_traduccion():
    texto_ingles = entry_texto.get()
    if texto_ingles:
        traduccion_espanol = traducir_texto(texto_ingles)
        if traduccion_espanol:
            label_traduccion.config(text=f"Traducción en español: {traduccion_espanol}")
    else:
        messagebox.showwarning("Texto vacío", "Por favor ingresa un texto en inglés.")

def manejar_guardar_y_reproducir():
    texto_ingles = entry_texto.get()
    if texto_ingles:
        ruta_audio_generado = guardar_audio(texto_ingles)
        if ruta_audio_generado:
            button_play.config(state="normal")
            messagebox.showinfo("Audio guardado", f"El audio se ha guardado en: {ruta_audio_generado}")
            reproducir_audio()  # Reproduce el audio inmediatamente después de guardarlo
    else:
        messagebox.showwarning("Texto vacío", "Por favor ingresa un texto en inglés para reproducir.")

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Traductor y Lector de Inglés")
    ventana.geometry("450x300")

    tk.Label(ventana, text="Texto en inglés:").pack(pady=5)

    global entry_texto
    entry_texto = tk.Entry(ventana, width=50)
    entry_texto.pack(pady=5)

    tk.Button(ventana, text="Traducir a español", command=manejar_traduccion).pack(pady=10)

    global label_traduccion
    label_traduccion = tk.Label(ventana, text="Traducción en español:", wraplength=400, justify="left")
    label_traduccion.pack(pady=5)

    tk.Button(ventana, text="Guardar y Reproducir Audio", command=manejar_guardar_y_reproducir).pack(pady=5)

    global button_play
    button_play = tk.Button(ventana, text="Play", command=reproducir_audio, state="disabled")
    button_play.pack(pady=5)

    ventana.mainloop()

# Ejecutar la interfaz
crear_interfaz()
