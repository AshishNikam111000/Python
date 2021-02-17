import speech_recognition as sr
import pyttsx3, os
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    img = pyautogui.screenshot()
    img.save('E:\\  ASHISH\\StudioCode\\Python\\Jarvis\\Screenshot data\\test.jpeg')

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

ss = takeCommand().lower()

if 'screen shot' in ss or 'screenshot' in ss:
    screenshot()
    speak("screenshot taken...")