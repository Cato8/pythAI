import requests
import wikipedia 
import pywhatkit as kit
from decouple import config



def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json')
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences = 2)
    return results

def search_on_google(query):
    kit.search(query)

