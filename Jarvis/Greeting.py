import datetime, pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    engine.say(Time)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    engine.say(day)
    engine.say(month)
    engine.say(year)
    engine.runAndWait()

def wishme():
    speak("Welcome Commander!")
    speak("Current Time is")
    time()
    speak("And Current Date is")
    date()
    speak("Jarvis At your service, how can I help you?")

wishme()