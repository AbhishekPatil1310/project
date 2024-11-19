import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',int(rate*0.6))
    engine.say(text)
    engine.runAndWait()


text = "workout"
speak(text)