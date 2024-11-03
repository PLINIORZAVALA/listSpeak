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

# ===================== Funciones de Traducción y Audio =====================
def traducir_texto(texto_ingles):
    """Traduce el texto en inglés a español."""
    try:
        return translator.translate(texto_ingles)
    except Exception as e:
        messagebox.showerror("Error de Traducción", f"No se pudo traducir el texto: {e}")
        return None

def guardar_audio(texto_ingles):
    """Genera un archivo de audio a partir del texto en inglés."""
    try:
        tts = gTTS(text=texto_ingles, lang='en')
        os.makedirs(ruta_audio, exist_ok=True)
        tts.save(ruta_completa_audio)
        return ruta_completa_audio
    except Exception as e:
        messagebox.showerror("Error al Guardar Audio", f"No se pudo guardar el audio: {e}")
        return None

def reproducir_audio():
    """Reproduce el archivo de audio generado."""
    try:
        if os.path.exists(ruta_completa_audio):
            pygame.mixer.music.load(ruta_completa_audio)
            pygame.mixer.music.play()
        else:
            messagebox.showwarning("Audio no encontrado", "No se ha generado el audio aún.")
    except Exception as e:
        messagebox.showerror("Error de Reproducción", f"No se pudo reproducir el audio: {e}")

# ===================== Funciones de Manejo de la Interfaz =====================
def manejar_traduccion():
    """Maneja la traducción del texto ingresado y actualiza la interfaz."""
    texto_ingles = entry_texto.get()
    if texto_ingles:
        traduccion_espanol = traducir_texto(texto_ingles)
        if traduccion_espanol:
            label_traduccion.config(text=f"Traducción en español: {traduccion_espanol}")
    else:
        messagebox.showwarning("Texto vacío", "Por favor ingresa un texto en inglés.")

def manejar_guardar_y_reproducir():
    """Guarda el audio del texto ingresado y lo reproduce."""
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
    """Crea la interfaz principal de la aplicación."""
    global ventana  # Hacer la variable ventana global
    ventana = tk.Tk()  # Inicializar la ventana principal
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

    # Botón para iniciar la escucha activa
    tk.Button(ventana, text="Escucha Activa", command=iniciar_escucha_activa).pack(pady=5)

    global button_play
    button_play = tk.Button(ventana, text="Play", command=reproducir_audio, state="disabled")
    button_play.pack(pady=5)

    ventana.mainloop()

# ===================== Funciones de Escucha Activa =====================
def iniciar_escucha_activa():
    """Inicia el proceso de escucha activa y abre la ventana correspondiente."""
    global ventana  # Hacer la variable ventana global
    ventana.withdraw()  # Oculta la ventana principal
    
    # Crear nueva ventana para el paso 1
    ventana_escucha = tk.Toplevel()
    ventana_escucha.title("Escucha Activa - Paso 1")
    ventana_escucha.geometry("450x300")

    # Subtítulo en español
    subtitulo_espanol = traducir_texto(entry_texto.get())
    tk.Label(ventana_escucha, text=f"Palabra/Frase: {entry_texto.get()}\nSubtítulo en español: {subtitulo_espanol}", wraplength=400, justify="left").pack(pady=10)

    # Botón para reproducir el audio
    tk.Button(ventana_escucha, text="Reproducir Audio", command=reproducir_audio).pack(pady=10)

    # Botón para pasar al paso 2
    tk.Button(ventana_escucha, text="Siguiente (Paso 2)", command=lambda: pasar_paso(ventana_escucha, 2)).pack(pady=10)

# ===================== Funciones de Creación de Interfaz =====================
def pasar_paso(ventana_actual, paso):
    """Maneja la transición entre los pasos de la escucha activa."""
    ventana_actual.destroy()  # Cerrar ventana actual

    if paso == 2:
        # Crear nueva ventana para el paso 2
        ventana_escucha = tk.Toplevel()
        ventana_escucha.title("Escucha Activa - Paso 2")
        ventana_escucha.geometry("450x300")

        # Mostrar subtítulo en inglés
        tk.Label(ventana_escucha, text=f"Palabra/Frase: {entry_texto.get()}", wraplength=400, justify="left").pack(pady=10)

        # Botón para reproducir el audio
        tk.Button(ventana_escucha, text="Reproducir Audio", command=reproducir_audio).pack(pady=10)

        # Botón para pasar al paso 3
        tk.Button(ventana_escucha, text="Siguiente (Paso 3)", command=lambda: pasar_paso(ventana_escucha, 3)).pack(pady=10)

    elif paso == 3:
        # Crear nueva ventana para el paso 3
        ventana_escucha = tk.Toplevel()
        ventana_escucha.title("Escucha Activa - Paso 3")
        ventana_escucha.geometry("450x300")

        # Solo audio
        tk.Label(ventana_escucha, text="Reproduciendo Audio...").pack(pady=10)

        # Botón para reproducir el audio
        tk.Button(ventana_escucha, text="Reproducir Audio", command=reproducir_audio).pack(pady=10)

        # Botón para finalizar y regresar a la ventana principal
        tk.Button(ventana_escucha, text="Finalizar", command=lambda: regresar_inicio(ventana_escucha)).pack(pady=10)

# ===================== Ejecución de la Interfaz =====================
def regresar_inicio(ventana_actual):
    """Regresa a la interfaz principal."""
    ventana_actual.destroy()  # Cerrar ventana actual
    ventana.deiconify()  # Mostrar la ventana principal

# Ejecutar la interfaz principal
crear_interfaz()
