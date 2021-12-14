import pyttsx3
from decouple import config
from datetime import datetime 
import speech_recognition as sr
from random import choice 
from utils import opening_text

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

def greet_user():
    hour = datetime.now().hour
    if (hour >=6) and (hour < 16):
        speak(f"Bonjour {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Bonsoir {USERNAME}")
    speak(f"Je suis {BOTNAME}. Comment puis-je vous aidez?")

def take_user_input():
    """Takes user input, recognizes it using Speech recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='fr-CH')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak(f"Bonne nuit {USERNAME}, prenez soins de vous !")
            else:
                speak(f"Passez une bonne journée {USERNAME}")
    except Exception:
        speak("Pardonnez moi je n'ai pas compris pouvez vous répeter s'il vous plaît ?")
        query = 'None'
    return query

