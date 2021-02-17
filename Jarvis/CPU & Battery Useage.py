import speech_recognition as sr
import pyttsx3, os
import psutil

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def CPU():
    usage = str(psutil.cpu_percent())
    speak("CPU is Running at "+usage+" percentage")

def Battery():
    usage = psutil.sensors_battery()
    speak("Battery is at "+str(usage.percent)+" percent")

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

status = takeCommand().lower()

if 'status' in status:
    CPU()
    Battery()
    pass