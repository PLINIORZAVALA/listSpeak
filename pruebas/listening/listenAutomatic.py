from translate import Translator
import pyttsx3

# Configura el traductor para traducir de inglés a español
translator = Translator(from_lang="en", to_lang="es")

# Texto en inglés que deseas traducir y escuchar
texto_ingles = "This is a test translation from English to Spanish."

# Traducción al español
traduccion_espanol = translator.translate(texto_ingles)

# Muestra la traducción
print(f"Texto en inglés: {texto_ingles}")
print(f"Traducción en español: {traduccion_espanol}")

# Configura el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty('rate', 100)  # Velocidad del habla
engine.setProperty('volume', 0.9)  # Volumen de la voz

# Reproduce el texto en inglés
engine.say(texto_ingles)
engine.runAndWait()
