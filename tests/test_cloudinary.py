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

# Exemple d'utilisation
image_path = "img/elephant.jpg"  # Spécifiez le chemin vers votre image
uploaded_url = upload_image(image_path)

if uploaded_url:
    print("L'image a été uploadée avec succès. URL de l'image :", uploaded_url)
else:
    print("Une erreur s'est produite lors de l'upload de l'image.")