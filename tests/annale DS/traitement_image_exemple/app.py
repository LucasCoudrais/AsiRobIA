import cv2

# Charger l'image
image_path = "img1.jpg"  # Spécifiez le chemin vers votre image
image = cv2.imread(image_path)

# Vérifier si l'image est chargée correctement
if image is not None:
    # Convertir l'image en niveau de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou gaussien à l'image en niveaux de gris
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Détecter les contours sur l'image floue
    edges = cv2.Canny(image, 30, 150)

    # Afficher les images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.imshow("Blurred Image", blurred_image)
    cv2.imshow("Edges", edges)

    # Attendre l'appui sur une touche pour fermer les fenêtres
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erreur lors du chargement de l'image.")
