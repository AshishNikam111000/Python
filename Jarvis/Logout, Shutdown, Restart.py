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

cmd = takeCommand().lower()

if 'shut down' in cmd or 'shutdown' in cmd:
    speak("shuting Down...")
    res = os.system('shutdown /s')
elif 'restart' in cmd:
    speak("Restarting Now...")
    res = os.system('shutdown /r')
elif 'log out' in cmd or 'logout' in cmd:
    speak("Logging Out...")
    res = os.system('shutdown /l')
else:
    speak("I didn't understand")