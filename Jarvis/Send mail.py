import speech_recognition as sr
import pyttsx3, smtplib

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','123')
    server.sendmail('abc@gmail.com',to ,content)
    server.close()

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

mail = takeCommand().lower()
    
if 'send mail' in mail:
    speak("To whom you want to send")
    to = takeCommand().lower()
    speak("What should I say?")
    content = takeCommand()
    sendmail(to,content)
    speak("Mail has been sent, sir")
