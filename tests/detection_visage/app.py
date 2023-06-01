import cv2

# Charger le classificateur de détection de visages pré-entraîné
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Charger l'image
image = cv2.imread('people.jpg')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Détecter les visages dans l'image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dessiner un rectangle autour de chaque visage détecté
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Afficher l'image avec les visages détectés
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()