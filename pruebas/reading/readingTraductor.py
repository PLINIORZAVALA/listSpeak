from translate import Translator

# Configura el traductor para traducir de inglés a español
translator = Translator(from_lang="en", to_lang="es")

# Texto en inglés que deseas traducir
texto_ingles = "This is a test translation from English to Spanish."

# Traducción al español
traduccion_espanol = translator.translate(texto_ingles)

# Muestra el resultado
print(f"Texto en inglés: {texto_ingles}")
print(f"Traducción en español: {traduccion_espanol}")
