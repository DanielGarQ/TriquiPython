import random

class Triqui():

    def __init__(self):
        self.tablero = [['-','-','-'],
                        ['-','-','-'],
                        ['-','-','-']]

    def crear_Tablero(self):
        print(self.tablero)

    def cerrarJuego(self, opcion):
        while opcion == "N" :
            break


    def primer_jugador_aleatorio(self):
        return random.randint(1, 2)

    def llenar_casilla(self, fila, columna, jugador):
        self.tablero[fila][columna] = jugador

    def ganador(self, jugador):
        if (self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2]== jugador or self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0]== jugador or self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1]== jugador or self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2]== jugador or self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]== jugador or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]== jugador or self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2]== jugador or self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2]== jugador ):
            if jugador == "X":
                print("Gana el jugador 1")
            else:
                print("Gana el jugador 2")
            return True

    def tablero_lleno(self):
        for fila in self.tablero:
            for valor in fila:
                if valor == '-':
                    return False
        return True

    def cambiar_turno(self, jugador):
        return 'X' if jugador == '0' else '0'

    def mostrar_tablero(self):
        for fila in self.tablero:
            for valor in fila:
                print(valor, end="")
            print()

    def iniciar(self):
        jugador = 'X'if self.primer_jugador_aleatorio() == 1 else '0'
        for i in range (9):
            self.mostrar_tablero()
            print(f"Es turno del jugador {jugador}")

            fila = int(input("Ingresa la fila: "))
            columna = int(input("Ingresa la columna: "))

            self.llenar_casilla(fila - 1, columna - 1, jugador)

            if self.ganador(jugador)==True:
                print(f"El jugador {jugador} ha ganado el juego!")
                self.mostrar_tablero()
                break


            if self.tablero_lleno() :
                print("Empate")
            jugador = self.cambiar_turno(jugador)
        print("Juego Terminado")
        opcion = input("Desea Volver a iniciar S/N: ")
        if opcion == "S" or opcion == "s":
            triqui = Triqui()
            triqui.iniciar()

        elif opcion == "N" or opcion == "n":
            opcion = "N"
            self.cerrarJuego(opcion)

        else:
            print("Ingreso una opcion no valida")



        print()
        self.mostrar_tablero()