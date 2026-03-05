from googletrans import Translator

translator = Translator()

def translate_text(text, src_lang, dest_lang):
    result = translator.translate(text, src=src_lang, dest=dest_lang)
    return result.text