import speech_recognition as sr
import pyttsx3, os

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

remember = takeCommand().lower()

if 'remember' in remember:
    speak("What should I remember?")
    data = takeCommand()
    speak("Writing....")
    speak(data)
    speak('to the file')
    rem = open('E:\\  ASHISH\\StudioCode\\Python\\Jarvis\\Rememer Fuction data\\data.txt','w')
    rem.write(data)
    rem.close()

