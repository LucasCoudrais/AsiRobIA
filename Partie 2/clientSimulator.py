import requests
import time

def make_request():
    url = "http://127.0.0.1:5000/sensors"

    while True:
        response = requests.get(url)
        data = response.json()

        for item in data:
            name = item['name']
            temp = item['temp']
            print(f"{name} : {temp} °C")

        time.sleep(5)  # Attendre 5 secondes avant la prochaine requête

make_request()