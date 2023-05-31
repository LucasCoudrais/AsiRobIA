import requests
import json
import cloudinary
import cloudinary.uploader

def upload_image(image_path):
    cloudinary.config( 
    cloud_name = "dnesprvqu", 
    api_key = "321391161964924", 
    api_secret = "x_E7suSQmJYiz0qZC7Xk8JFPq8A" 
    )


    response = cloudinary.uploader.upload(image_path)

    if 'secure_url' in response:
        return response['secure_url']
    else:
        return None

def send_sensor_update():
    url = "http://localhost:5000/imageGeneratedCamera/1"
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    pathImgs = [
        "img/img1.jpg",
        "img/img2.jpg",
        "img/img3.jpg",
        "img/img4.jpg",
        "img/img5.jpg"
    ]
    while True:
        print('Entrez un entier entre 1 et 5 pour choisir une image que la caméra doit envoyer ')
        nbImage = int(input())
        if nbImage < 6 and nbImage > 0 :
            # Exemple d'utilisation
            image_path = pathImgs[nbImage-1] # Spécifiez le chemin vers votre image
            uploaded_url = upload_image(image_path)
            print("Requete envoyée pour uploader l'image sur interet et récupérer l'url et envoyer l'image dans l'api "+str(nbImage))
            data = {
                "id": 1,
                "name": "Image actuelle caméra intérieure",
                "url": uploaded_url
            }
            payload = json.dumps(data)
            response = requests.put(url, headers=headers, data=payload)
            print("Code de statut de la réponse : ", response.status_code)
        else : 
            print("Valeur entrée incorrecte veuillez réssayer.")


send_sensor_update()