import cv2

def detectar_rostros(imagen):
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        rostros = face_cascade.detectMultiScale(gris, scaleFactor = 1.1, minNeighbors = 3)
        return rostros