from flask import Flask, render_template, request
import speech_recognition as sr
from googletrans import Translator

app = Flask(__name__)

# Initialize the recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    language_code = request.form['language']
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Speech Recognition
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language=f'{language_code}-{language_code.upper()}')
        print(f"You said: {text}\n")

        # Translate the text into English
        translation = translator.translate(text, dest='en')
        translated_text = translation.text
        print(f"Translation: {translated_text}\n")

    except Exception as e:
        translated_text = f"Error: {e}"

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
