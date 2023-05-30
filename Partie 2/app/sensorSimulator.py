import requests
import json
import random
import time

def send_sensor_update():
    url1 = "http://localhost:5000/sensors/1"
    url2 = "http://localhost:5000/sensors/2"
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    while True:
        temperature1 = random.randint(0, 100)
        temperature2 = random.randint(0, 100)
        data1 = {
            "id": 1,
            "name": "Capteur chambre",
            "temp": temperature1
        }
        data2 = {
            "id": 2,
            "name": "Capteur séjour",
            "temp": temperature2
        }
        payload1 = json.dumps(data1)
        payload2 = json.dumps(data2)

        response1 = requests.put(url1, headers=headers, data=payload1)
        response2 = requests.put(url2, headers=headers, data=payload2)
        print("Modification capteur n° 1 avec température de "+str(temperature1))
        print("Code de statut de la réponse:", response1.status_code)
        print("Modification capteur n° 2 avec température de "+str(temperature2))
        print("Code de statut de la réponse:", response2.status_code)

        time.sleep(10)

send_sensor_update()