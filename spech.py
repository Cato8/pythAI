import pyttsx3
import requests
from decouple import config
from datetime import datetime 
import speech_recognition as sr
from random import choice 
from utils import opening_text
from pprint import pprint
from online_ops import find_my_ip, search_on_wikipedia, search_on_google 

USERNAME = 'Toine'
BOTNAME = 'JARVIS'


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

if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Votre adresse ip est {ip_address}.\n Je vous l'imprime à l'écran")
            print(f'Votre adresse ip est {ip_address}')

        elif 'wikipedia' in query:
            speak('Que voulez vous chercher sur wikipedia {USERNAME} ?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"Voilà les résultats sur wikipédia, {results}")
            speak("Je vous l'imprime à l'écran")
            print(results)
        
        elif 'search on google' in query:
            speak('Que voulez-vous chercher sur google {USERNAME}?')
            query = take_user_input().lower()
            search_on_google(query)
        


