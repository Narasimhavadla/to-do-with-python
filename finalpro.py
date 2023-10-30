import requests
import json

api_key = "22245bd297ccb7a693f1e0be899688cc"
base_url = "https://api.openweathermap.org/data/2.5/weather"

city_name = input("Enter city name: ")
complete_url = f"{base_url}?q={city_name}&appid={api_key}"
response = requests.get(complete_url)
data = response.json()

if data["cod"] != "404":
    if "main" in data:
        main_data = data["main"]
        coord = data["coord"]
        speed = data["wind"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        lattitude = coord["lat"]
        longitude = coord["lon"]
        pressure = main_data["pressure"]
        wind_speed = speed["speed"]
        weather_data = data["weather"][0]
        description = weather_data["description"]

        print(f"Temperature: {temperature-273}°C")
        print(f"Humidity: {humidity}%")
        print(f"lattitude : {lattitude}")
        print(f"longitude: {longitude}")
        print(f"pressure : { pressure}")
        print(f"wind speed : {wind_speed}")
        print(f"Description: {description}")

    else:
        print("Main data not found in the API response.")
else:
    print("City not found")

