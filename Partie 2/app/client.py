import requests
import curses
import cv2
import urllib.request
import numpy as np

def make_request(stdscr):
    urlSensors = "http://127.0.0.1:5000/tempSensors"
    urlProximitySensors = "http://127.0.0.1:5000/proximitySensors"
    urlInteruptors = "http://127.0.0.1:5000/interuptors"
    urlimgCamera = "http://127.0.0.1:5000/imageCameras"
    urlimgGeneratedCamera = "http://127.0.0.1:5000/imageGeneratedCameras"

    # Configuration de la fenêtre curses
    curses.curs_set(0)  # Masquer le curseur
    stdscr.nodelay(1)  # Mode non bloquant pour la lecture de l'entrée

    # Boucle principale
    while True:
        stdscr.clear()  # Effacer l'écran

        # Effectuer la requête HTTP
        responseSensors = requests.get(urlSensors)
        dataSensors = responseSensors.json()
        
        # Effectuer la requête HTTP
        responseProximitySensors = requests.get(urlProximitySensors)
        dataProximitySensors = responseProximitySensors.json()
        
        # Effectuer la requête HTTP
        responseInteruptors = requests.get(urlInteruptors)
        dataInteruptors = responseInteruptors.json()
        
        # Effectuer la requête HTTP
        responseImgCamera = requests.get(urlimgCamera)
        dataImgCamera = responseImgCamera.json()
        
        # Effectuer la requête HTTP
        responseImgGeneratedCamera = requests.get(urlimgGeneratedCamera)
        dataImgGeneratedCamera = responseImgGeneratedCamera.json()

        # Afficher les résultats dans l'interface curses
        height, width = stdscr.getmaxyx()
        y = 1

        for item in dataSensors:
            name = item['name']
            temp = item['temp']
            output = f"{name} : {temp} °C"
            stdscr.addstr(y, 0, output)
            y += 1
            
        y += 1
          
        for item in dataProximitySensors:
            name = item['name']
            presence = item['presence']
            if(presence): 
                output = f"{name} : Oui"
            else: 
                output = f"{name} : Non"

            stdscr.addstr(y, 0, output)
            y += 1
            
        y += 1
          
        for item in dataInteruptors:
            name = item['name']
            presence = item['isOn']
            if(presence): 
                output = f"{name} : Allumé"
            else: 
                output = f"{name} : Eteint"

            stdscr.addstr(y, 0, output)
            y += 1
            
        y += 1
          
        for item in dataImgCamera:
            
            # req = urllib.request.urlopen(item['url'])
            # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            # img = cv2.imdecode(arr, -1) # 'Load it as it is'
            # imS = cv2.resize(img, (600, 400))                # Resize image
            # cv2.imshow(item['name'], imS)
            # cv2.waitKey(500) # on attend 0.5 secondes
            # # cv2.destroyAllWindows()

                  
            name = item['name']
            url = item['url']
            output = f"{name}, URL : {url}"
            
            stdscr.addstr(y, 0, output)
            y += 1
        
        y += 1
          
        for item in dataImgGeneratedCamera:
            
            req = urllib.request.urlopen(item['url'])
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1) # 'Load it as it is'
            imS = cv2.resize(img, (600, 400))                # Resize image
            cv2.imshow(item['name'], imS)
            cv2.waitKey(500) # on attend 0.5 secondes
            # cv2.destroyAllWindows()
                  
            name = item['name']
            url = item['url']
            output = f"{name}, URL : {url}"

            stdscr.addstr(y, 0, output)
            y += 1

        stdscr.refresh()  # Rafraîchir l'écran

        # Lire l'entrée utilisateur
        key = stdscr.getch()
        if key == ord('q'):
            break

# Appel de la fonction principale avec curses
curses.wrapper(make_request)