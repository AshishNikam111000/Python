import speech_recognition as sr
import pyttsx3, os
import webbrowser as wb

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

search = takeCommand().lower()
    
if 'search' in search or 'find' in search:
    speak("What should I search?")
    site = takeCommand().lower()
    osopen = os.system('start chrome /incognito '+ site)