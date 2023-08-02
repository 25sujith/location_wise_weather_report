import  json

import requests as requests


def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] == "404":
            return "City not found."

        city = data["name"]
        weather_desc = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = f"Weather in {city}: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
        return result
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "8eba49b53561de7fa04c127428ca0a5b"  # Replace with your actual API key
    weather_info = get_weather(city_name, api_key)
    print(weather_info)

