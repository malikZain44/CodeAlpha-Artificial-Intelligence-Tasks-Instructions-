from gtts import gTTS
import uuid

def text_to_speech(text, lang):
    filename = f"audio_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename