import speech_recognition as sr
from googletrans import Translator

# Initialize the recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def listen_and_translate():
   # Use the microphone as the audio source
   with sr.Microphone() as source:
       print("Listening...")
       audio = recognizer.listen(source)

   try:
       # Recognize the speech using Google Speech Recognition
       print("Recognizing...")
       text = recognizer.recognize_google(audio, language='jp-JP')   # If you want to use other languages, change the language code. For example, Urdu is ur-PK.
       print(f"You said: {text}\n")

       # Translate the text into English
       translation = translator.translate(text, dest='en')
       print(f"Translation: {translation.text}\n")

   except Exception as e:
       print("Error:", e)

# Keep listening and translating in a loop
while True:
   listen_and_translate()
