import speech_recognition as sr
import pyttsx3, os
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def jokes():
    speak(pyjokes.get_jokes())

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again, please!")
        return None

    return query

joke = takeCommand().lower()

if 'joke' in joke or 'jokes' in joke:
    jokes()