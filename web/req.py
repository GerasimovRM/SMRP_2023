import requests
from pprint import pprint

params = {"latitude": 58.0105,
          "longitude": 56.2502,
          "current_weather": True,
          "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m"}

result = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
pprint(result.json())
