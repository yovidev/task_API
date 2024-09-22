import requests
import os
import socket


def get_ip():
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_ip_location(ip: str):
    # Consultamos la ubicación del IP usando el servicio IP-API
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json().get("country")

def get_weather(country: str):
    # Obtenemos el clima del país utilizando la API de OpenWeatherMap
    api_key = os.getenv("WEATHER_API_KEY")
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={country}&appid={api_key}")
    return response.json()


def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info['ip']

print("IP pública:", get_public_ip())

ip = get_ip()
ip_location = get_ip_location(get_public_ip())

print("IP local:", ip)
print("LOcation: ", ip_location)
print("clima: ", get_weather(ip_location))