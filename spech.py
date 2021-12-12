import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')
#Set rate 
engine.setProperty('rate', 190)

#Set volume 
engine.setProperty('volume', 1.0)

#Set voice 
voices = engine.setProperty('voices')
engine.setProperty('voice', voices[1].id)

#Text to speech conversion 
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()
    
