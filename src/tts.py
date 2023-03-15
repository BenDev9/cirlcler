import pyttsx3

# Initialise the pyttsx3 engine
engine = pyttsx3.init()


def speak(text: str):
    """Wrapper function for the `pyttsx3.say()` function"""
    engine.say(text)
    engine.runAndWait()
