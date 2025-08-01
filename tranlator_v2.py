import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

# Function to get target language from user
def get_languages():
    print("\nAvailable Languages:")
    print("1. English ↔ Hindi")
    print("2. English ↔ Tamil")
    print("3. English ↔ Telugu")
    choice = input("Choose language pair (1/2/3): ")

    if choice == "1":
        direction = input("Translate from English to Hindi (1) or Hindi to English (2)? ")
        return ("en", "hi") if direction == "1" else ("hi", "en")
    elif choice == "2":
        direction = input("Translate from English to Tamil (1) or Tamil to English (2)? ")
        return ("en", "ta") if direction == "1" else ("ta", "en")
    elif choice == "3":
        direction = input("Translate from English to Telugu (1) or Telugu to English (2)? ")
        return ("en", "te") if direction == "1" else ("te", "en")
    else:
        print("Invalid choice. Defaulting to English to Hindi.")
        return ("en", "hi")

# Ask for language pair
src_lang, tgt_lang = get_languages()

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("\nSpeak now! (say 'exit' to quit)")
        audio = r.listen(source)

        try:
            speech_text = r.recognize_google(audio, language=src_lang)
            print("You said:", speech_text)
            if speech_text.lower() == "exit":
                break
        except sr.UnknownValueError:
            print("Could not understand")
            continue
        except sr.RequestError:
            print("Could not request result from Google")
            continue

        # Translate using deep_translator
        translated_text = GoogleTranslator(source=src_lang, target=tgt_lang).translate(speech_text)
        print("Translated:", translated_text)

        # Convert to speech
        voice = gTTS(translated_text, lang=tgt_lang)
        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
