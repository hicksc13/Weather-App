import requests

API_KEY = "83536a95d4dd86b3883578912f0f2d0f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature_kelvin = round(data["main"]["temp"] - 273.15, 2)
    temperature = round(temperature_kelvin*1.8+32, 2)

    print("Weather:", weather)
    print("Temperature:",temperature, "Fahrenheit")
else:
    print("An error has occurred.")
