from translate import Translator
from gtts import gTTS
import os

# Configura el traductor para traducir de inglés a español
translator = Translator(from_lang="en", to_lang="es")

# Texto en inglés que deseas traducir y escuchar
texto_ingles = "This is a test translation from English to Spanish."

# Traducción al español
traduccion_espanol = translator.translate(texto_ingles)

# Muestra la traducción
print(f"Texto en inglés: {texto_ingles}")
print(f"Traducción en español: {traduccion_espanol}")

# Genera y reproduce el audio del texto en inglés
tts = gTTS(text=texto_ingles, lang='en')
tts.save("texto_ingles.mp3")
os.system("texto_ingles.mp3")

