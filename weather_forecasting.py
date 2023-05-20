import requests
import json
import winsound

def get_weather_data(api_key, city):
    base_url = "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"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)
        return data
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", str(e))
        return None

def display_weather_info(weather_data):
    if weather_data is None:
        print("Unable to fetch weather data.")
        return

    main_data = weather_data.get("main")
    temperature = main_data.get("temp")
    humidity = main_data.get("humidity")

    weather_info = weather_data.get("weather")[0]
    description = weather_info.get("description")

    print(f"Weather forecast: {description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

    return temperature

def weather_forecasting_app(api_key, temp_limit):
    city = input("Enter the city name for weather forecasting: ")
    print("Fetching weather data...")

    weather_data = get_weather_data(api_key, city)
    current_temperature = display_weather_info(weather_data)

    if current_temperature is not None and current_temperature > temp_limit:
        print("Temperature limit exceeded! Alarm triggered.")
        winsound.PlaySound("WhatsApp Audio 2023-05-20 at 5.54.01 PM.aac", winsound.SND_ASYNC)

API_KEY = "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"

TEMPERATURE_LIMIT = 30

weather_forecasting_app(API_KEY, TEMPERATURE_LIMIT)

state = input("input the name of the state : \n ")
print(state)
city = input("input the name of the city under state we want to know the temperature: \n")
print(city)

print('Displaying weather report for:' + state + city)

url = 'https://wttr.in/{}'.format(state)
url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)