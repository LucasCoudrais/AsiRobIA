import cv2

# URL de l'API de streaming vidéo
url = 'http://localhost:5000/streamCamera'

# Ouvrir le flux vidéo en utilisant OpenCV
cap = cv2.VideoCapture(url)

while True:
    # Lire une trame du flux vidéo
    ret, frame = cap.read()

    if not ret:
        break

    # Afficher la trame dans une fenêtre
    cv2.imshow('Video Stream', frame)

    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()