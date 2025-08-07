import os
import time

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

                match opc:
                        case 1:
                                pass
                        case 2:
                                pass
                        case 3:
                                os.system("clear")
                                print("""
Bienvenido a la guia de uso del programa 'face pixelator', este programa cuenta con dos
opciones principales, una que se encarga de pixelear el rostro de la presona que se
encuentre frente a la camara y la otra es una que se encarga de pixelear el rostro de
la(s) personas que se encuentren en una imagen
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