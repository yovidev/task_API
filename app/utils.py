import requests
import os


def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info['ip']

def get_ip_location(ip: str):
    #consulta de la ubicación de la ip con el servicio IP-API
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json()

def get_weather(country: str):
    #obtener el clima del país utilizando la API de OpenWeatherMap
    api_key = os.getenv("WEATHER_API_KEY")
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}")
    return response.json()




