import datetime, pyttsx3

engine = pyttsx3.init()

def time():
    engine.say("Today's Time is")
    engine.runAndWait()
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    engine.say(Time)
    engine.runAndWait()

def date():
    engine.say("And Date is")
    engine.runAndWait()
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    engine.say(day)
    engine.say(month)
    engine.say(year)
    engine.runAndWait()

time()
date()