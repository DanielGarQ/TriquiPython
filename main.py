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


