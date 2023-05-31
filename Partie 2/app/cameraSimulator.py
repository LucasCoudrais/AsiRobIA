import requests
import json
import random
import time

def send_sensor_update():
    url = "http://localhost:5000/imageCamera/1"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    urlImgs = [
        "https://www.illico-travaux.com/wp-content/uploads/2018/02/am%C3%A9nagements-ext%C3%A9rieurs.jpeg",
        "https://prod-saint-gobain-fr.content.saint-gobain.io/sites/saint-gobain.fr/files/2020-07/amenager-espace-exterieur.jpg",
        "https://resize.elle.fr/article/var/plain_site/storage/images/deco/exterieur/jardin/15-belles-idees-pour-amenager-son-jardin/70174525-2-fre-FR/L-amenagement-du-jardin-en-20-idees.jpg",
        "https://archzine.fr/wp-content/uploads/2021/04/decoration-exterieur-jardin-moderne-revetement-de-sol-bois-parasol-escalier-sans-contremarches-cloture-bois.jpg",
        "https://fac.img.pmdstatic.net/fit/https.3A.2F.2Fi.2Epmdstatic.2Enet.2Ffac.2F2021.2F06.2F01.2F218803bc-e0c1-4e41-b265-fd7b473ca407.2Ejpeg/1200x900/quality/80/crop-from/center/focus-point/2897%2C3164/jardin-nos-conseils-pour-une-decoration-zen-et-un-exterieur-apaisant.jpeg"
    ]
    while True:
        print('Entrez un entier entre 1 et 5 pour choisir une image que la caméra doit envoyer ')
        nbImage = int(input())
        if nbImage < 6 and nbImage > 0 :
            print("Requete envoyée pour envoyer l'image "+str(nbImage))
            data = {
                "id": 1,
                "name": "Image actuelle caméra extérieure",
                "url": urlImgs[nbImage-1]
            }
            payload = json.dumps(data)
            response = requests.put(url, headers=headers, data=payload)
            print("Code de statut de la réponse : ", response.status_code)
        else : 
            print("Valeur entrée incorrecte veuillez réssayer.")


send_sensor_update()