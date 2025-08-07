#Librerias
import os
import time

from opc1 import cara
from opc2 import sello
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
                        print("\Grcias por su preferencia")
                        time.sleep(1)
                        print("Saliendo del programa...")
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
                                pass
                                # Pedir la imagen, puede ser con la ruta general o seria mejor que esta este enl a misma carpeta
                                # Leer la imagen cv.imread() creo
                                # Detectar los rostros en la imagen
                                # Por cada rostro extraer solo la region de interes (rostro)
                                # Aplicar el pixelado
                                # Mostrar la imagen en una ventana
                                        # Preguntar si desea guardar la imagen, 'nombre_pixelated.jpg'
                                # Volver al menu
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