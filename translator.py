from googletrans import Translator

translator = Translator()

text = input("Enter text to translate: ")
lang = input("Enter target language (hi for Hindi, fr for French): ")

translated = translator.translate(text, dest=lang)

print("Translated Text:", translated.text)
