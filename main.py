from TriquiBase import *
import random

print("Los modos disponibles son: ")
print("1.Un jugador")
print("2.Multijugador")
opcion = int(input("Ingrese el modo que desea jugar: "))
if opcion == 1:
    print("Lo sentimos, este modo aun se encuentra en desarrollo")

elif opcion == 2:
    print("Ha elegido el modo jugador contra jugador.\n")
    print("Por defecto el jugador1 tiene la X y el jugador2 tiene el 0")
    print("1.Jugar")
    print("2.Elegir turno")
    seleccion = int(input("Ingrese su opcion: "))
    if seleccion == 1:
        triqui = Triqui()
        triqui.iniciar()
    if seleccion == 2:
        print("Lo sentimos, esta opcion aun se encuentra en desarrollo")








'''def jugador_inicial():
    print("Antes de jugar podrá elegir si desea que el jugador inicial sea aleatorio o elegido previamente")
    inicio = int(input("Desea elegir el jugador inicial?: "))
    print("1).Si")
    print("2).No\n")
    if inicio == 1:
        turno_singleplayer = int(input("Quién jugará primero?\nEl jugador 1 o 2?: "))
        if turno_singleplayer == 1:
            pass
#Empieza el juego

        elif turno_singleplayer == 2:
            pass



    elif inicio == 2:
        print(f"Iniciará el jugador: {random.randint(1, 2)}")
        #empieza el juego'''

