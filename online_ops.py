import requests
import wikipedia 
import pywhatkit as kit
from decouple import config

OPENWEATHER_APP_ID = config("1d100c745149ebfeb3ff7adc02eedf54")


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json')
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences = 2)
    return results

def search_on_google(query):
    kit.search(query)

def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", header)
    return res["joke"]