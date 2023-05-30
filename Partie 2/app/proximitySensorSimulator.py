import requests
import json
import random
import time

def send_sensor_update():
    url = "http://localhost:5000/proximitySensor/"
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    while True:
        datas = [
        {
            "id": 1,
            "name": "Capteur présence cuisine",
            "presence": bool(random.randint(0, 1))
        },
        {
            "id": 2,
            "name": "Capteur présence garage",
            "presence": bool(random.randint(0, 1))
        },
        {
            "id": 3,
            "name": "Capteur présence salon",
            "presence": bool(random.randint(0, 1))
        },
        {
            "id": 4,
            "name": "Capteur présence télé",
            "presence": bool(random.randint(0, 1))
        },
        {
            "id": 5,
            "name": "Capteur présence portail",
            "presence": bool(random.randint(0, 1))
        }
        ]
        for i in range(5):
            payload = json.dumps(datas[i])
            response = requests.put(url+str(i+1), headers=headers, data=payload)
            if(datas[i]["presence"]):
                print("Modification capteur de présence n° "+str(i+1)+" avec présence ")
            else :
                print("Modification capteur de présence n° "+str(i+1)+" sans présence ")
            print("Code de statut de la réponse:", response.status_code)

        time.sleep(random.randint(4, 10))

send_sensor_update()