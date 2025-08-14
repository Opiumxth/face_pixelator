from detector import detectar_rostros
from pixelator import pixelar_rostros

import os
import time
import cv2

def menu():
        while True:
                os.system("clear")
                print("""
=== PIXELADOR DE ROSTROS ===
Bienvenido al pixelador de rostros.
Menu de opciones:
        1. Pixelar en desde la camara.
        2. Pixelar imagenes
        3. Detalles del programa
        4. Salir
                """)

                while True:
                        try:
                                opc = int(input("\nSeleccione una opcion: "))
                                if 1 <= opc <= 4:
                                        break
                                else:
                                        print("\nOpcion fuera de rango!")
                                        print("Ingrese una opcion valida!\n")
                        except ValueError as error:
                                print(f"\nSe produjo un error del tipo: {error}")
                                print("Ingrese una opcion valida!\n")

                if opc == 4:
                        print("\nGrcias por su preferencia")
                        time.sleep(1)
                        print("Saliendo del programa...\n")
                        time.sleep(1.5)
                        break

                # Para ambas opciones seran con el haar cascade -> escala de grises y eso
                match opc:
                        case 1:
                                pass
                                # Iniciar la camara
                                # Leer frame por frame en tiempo real
                                # Detectar los rostros de cada frame
                                # Por cada rostro extraer solo la region de interes (rostro)
                                # Aplicar el pixelado a este rostro frame por frame
                                # Reemplazar el rostro original con el pixelado
                                # Mostrar el rostro en la misma ventana
                                # Ademas tener la opcion de presionar una tecla para salir de la camara
                                # Cerrar camara
                                # Volver al menu

                        case 2:
                                print("\n[ Pixelar Imagen ]")
                                # Pedir la imagen y verificar que exista, puede ser con la ruta general o seria mejor que esta este enl a misma carpeta
                                while True:
                                        nombre_imagen = input("Ingrese el nombre de la imagen(con extension): ").strip() # Pedir solo el nombre ya que estara en la misma carpeta
                                        ruta_imagen = os.path.join("images", nombre_imagen)

                                        if os.path.exists(ruta_imagen): # Verificar que exista
                                                print("Procesando imagen...")
                                                time.sleep(1)
                                                break
                                        else:
                                                print("\n[ERROR]: No se encontro el archivo en la carpeta 'images'. Intente de nuevo")
                                                time.sleep(1)

                                # Leer la imagen cv.imread() creo
                                img = cv2.imread(ruta_imagen)

                                if img is None:
                                        print("[ERROR]: No se pudo leer la imagen. Verifique el archivo")
                                        break

                                rostros = detectar_rostros(img)

                                # Verificar si se detectaron rostros
                                if len(rostros) == 0:
                                        print("[INFO]: No se detectaron rostros")
                                        time.sleep(1)
                                else:
                                        # Aplicar el pixelado
                                        img_pixelada = pixelar_rostros(img, rostros)

                                        # Presionar Enter para salir de la ventana
                                        print("[INFO]: Presione Enter para salir")
                                        # Mostrar la imagen en una ventana
                                        cv2.imshow("Imagen Pixelada", img_pixelada)

                                        # Pedir la tecla d esalida
                                        while True:
                                                salir = cv2.waitKey(0) & 0xFF
                                                if salir == 13:
                                                        break

                                        cv2.destroyAllWindows()
                                        # Preguntar si desea guardar la imagen, 'pixelated_nombre.jpg'
                                        guardar = input("Desea guardar la imagen picelada(s/n): ").lower()
                                        if guardar == 's':      
                                                ruta_salida = os.path.join("images-outputs", f"pixelated_{nombre_imagen}")
                                                cv2.imwrite(ruta_salida, img_pixelada)
                                                print(f"[INFO]: Imagen guardada en '{ruta_salida}'")
                                # Volver al menu
                                print("")
                                input("Presione Enter para continuar...")
                                time.sleep(1)
                                print("Redirigiendo...")
                                time.sleep(1.5)

                        case 3:
                                os.system("clear")
                                print("""
Bienvenido a la guia de uso del programa 'face pixelator', este programa cuenta con dos
opciones principales, una que se encarga de pixelear el rostro de la(s) presona(s) que se
encuentre(n) frente a la camara y la otra es una que se encarga de pixelear el rostro de
la(s) persona(s) que se encuentre(n) en una imagen.

A continuacion una descripcion detallada.

Opcion 1:
        Al seleccionar esta opcion se carga blah blah blah

Opcion 2:
        Al seleccionar esta opcion se carga blah blah blah

""")
                                input("Presione Enter para continuar...")
                                time.sleep(1)
                                print("Redirigiendo...")
                                time.sleep(1.5)



if __name__ == "__main__":
        menu()