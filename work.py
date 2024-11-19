import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    else:
        print("Indian voice not found. Using default voice.")
    rate = engine.getProperty('rate')
    engine.setProperty('rate',int(rate*0.6))
    engine.say(text)
    engine.runAndWait()


text = "workout"
speak(text)