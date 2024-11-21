# Программа для получения текущей погоды в заданном городе с помощью модуля requests
 
import requests

def get_weather(city):
    # URL для запроса текущей погоды
    url = f"http://wttr.in/{city}?format=%C+%t"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

    return response.text

city = 'Moscow'  # Укажите необходимый город
weather = get_weather(city)

if weather:
    print(f"Текущая погода в {city.capitalize()}: {weather}")
