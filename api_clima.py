import requests


# API pública do Open-Meteo para Curitiba
url = "https://api.open-meteo.com/v1/forecast?latitude=-25.453&longitude=-49.31&current_weather=true"

# Fazendo a requisição
resp = requests.get(url)
clima = resp.json()

# Exibindo apenas informações úteis
print("Temperatura atual:", clima["current_weather"]["temperature"], "°C")
print("Velocidade do vento:", clima["current_weather"]["windspeed"], "km/h")