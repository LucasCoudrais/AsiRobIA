import requests
import json
import random
import time

def send_sensor_update():
    url = "http://localhost:5000/interuptor/"
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    while True:
        print('Entrez un entier entre 1 et 10 pour choisir un interupteur ')
        nbInteruptor = int(input())
        if nbInteruptor < 11 and nbInteruptor > 0 :
            print('Entrez 1 pour allumer l\'interupteur '+str(nbInteruptor)+' et 0 pour l\'éteindre : ')
            isOn = input()
            if isOn == "1" :
                print("Requete envoyée pour allumer l'interrupteur "+str(nbInteruptor))
                data = {
                    "id": nbInteruptor,
                    "name": "Intérupteur "+str(nbInteruptor),
                    "isOn": True
                }
                payload = json.dumps(data)
                response = requests.put(url+str(nbInteruptor), headers=headers, data=payload)
                print("Code de statut de la réponse : ", response.status_code)
            elif isOn == "0" :
                print("Requete envoyée pour éteindre l'interrupteur "+str(nbInteruptor))
                data = {
                    "id": nbInteruptor,
                    "name": "Intérupteur "+str(nbInteruptor),
                    "isOn": False
                }
                payload = json.dumps(data)
                response = requests.put(url, headers=headers, data=payload)
                print("Code de statut de la réponse : ", response.status_code)
            else :
                print("Valeur entrée incorrecte veuillez réssayer.")
        else : 
            print("Valeur entrée incorrecte veuillez réssayer.")


send_sensor_update()