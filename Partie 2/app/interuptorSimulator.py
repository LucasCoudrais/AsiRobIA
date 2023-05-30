import requests
import json
import random
import time

def send_sensor_update():
    url = "http://localhost:5000/interuptor/1"
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    while True:
        print('Entrez 1 pour allumer l\'interupteur des toilettes et 0 pour l\'éteindre : ')
        isOn = input()
        if isOn == "1" :
            print("Requete envoyée pour allumer l'interrupteur des toilettes")
            data = {
                "id": 1,
                "name": "Intérupteur toilette",
                "isOn": True
            }
            payload = json.dumps(data)
            response = requests.put(url, headers=headers, data=payload)
            print("Code de statut de la réponse : ", response.status_code)
        elif isOn == "0" :
            print("Requete envoyée pour éteindre l'interrupteur des toilettes")
            data = {
                "id": 1,
                "name": "Intérupteur toilette",
                "isOn": False
            }
            payload = json.dumps(data)
            response = requests.put(url, headers=headers, data=payload)
            print("Code de statut de la réponse : ", response.status_code)
        else :
            print("Valeur entrée incorrecte veuillez réssayer.")

send_sensor_update()