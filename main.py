import requests
from setting import API_KAYS


def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    # urls = (f'https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={api_key}')
    resp = requests.get(url)
    return resp.json()



def process_weather_data(data):
    """
    функция для добычи погоды
    :param data: берет ключи от погоды
    :return: вернули погоду
    """
    main_data = data['main']
    mein_wind = data['wind']
    weather_data = {
        'температура': main_data['temp'],
        'давление': main_data['pressure'],
        'влажность': main_data['humidity'],
        'ветер': mein_wind['speed']
    }
    return weather_data


if __name__ == '__main__':
    user = 'Донецк'
    get_weather_requests = get_weather(user, api_key=API_KAYS)
    weather = process_weather_data(get_weather_requests)


    # Построчный вывод
    for k,v in weather.items():
        print(f"{k} : {v}")
    # print(weather)
