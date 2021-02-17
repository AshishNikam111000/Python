import speech_recognition as sr
import wikipedia
import pyttsx3

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

command = takeCommand().lower()
    
if 'wikipedia' in command:
    speak("Searching...")
    command = command.replace('wikipedia','')
    result = wikipedia.summary(command, sentences = 5)
    print(result)
    speak(result)