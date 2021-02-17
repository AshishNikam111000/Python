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

song = takeCommand().lower()

if 'play song' in song or 'song' in song:
    song_dir = "E:\\  ASHISH\\Songs\\Favourite"
    songs = os.listdir(song_dir)
    os.startfile(os.path.join(song_dir,songs[-2]))