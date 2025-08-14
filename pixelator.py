import cv2

def pixelar_rostros(imagen, rostros, pixel_size = 10):
        for(x, y, w, h) in rostros:
                rostro = imagen[y:y+h, x:x+w]
                rostro_peq = cv2. resize(rostro, (w // pixel_size, h // pixel_size), interpolation = cv2.INTER_LINEAR)
                rostro_pixelado = cv2.resize(rostro_peq, (w, h), interpolation = cv2.INTER_NEAREST)
                imagen[y:y+h, x:x+w] = rostro_pixelado
        return imagen