import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)

        try:
            speech_text = r.recognize_google(audio)
            print("You said:", speech_text)
            if(speech_text=="exit"):
                break
        except sr.UnknownValueError:
            print("Could not understand")
            continue
        except sr.RequestError:
            print("Could not request result from Google")
            continue

        # Translate using deep_translator
        translated_text = GoogleTranslator(source='auto', target='hi').translate(speech_text)
        print("Translated:", translated_text)

        # Convert to speech
        voice = gTTS(translated_text, lang='hi')
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
