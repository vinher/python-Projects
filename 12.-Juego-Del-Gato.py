#Fecha: 12/11/21
#Descripción:Juego del gato o tic tac toe como también se le conoce
import time

tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def dibujar_tablero(tablero):
    print(" %c | %c | %c " % (tablero[0],tablero[1],tablero[2]))
    print("---+---+---")
    print(" %c | %c | %c " % (tablero[3],tablero[4],tablero[5]))
    print("---+---+---")
    print(" %c | %c | %c " % (tablero[6],tablero[7],tablero[8]))

def estado_del_juego(tablero):
    #Lineas horizontales
    if(tablero[0] == tablero[1] == tablero[2] !=' '):
        estado_actual = "Ganador"
    elif(tablero[3]==tablero[4]==tablero[5] != ' '):
        estado_actual = "Ganador"
    elif(tablero[6] == tablero[7] == tablero[8] != ' '):
        estado_actual = "Ganador"
    #Líneas verticales
    elif(tablero[0] == tablero [3] == tablero[6] !=' '):
        estado_actual = "Ganador"
    elif(tablero[1] == tablero[4] == tablero[7] !=' '):
        estado_actual = "Ganador"
    elif(tablero[2] == tablero[5] == tablero[6] !=' '):
        estado_actual = "Ganador"
    #Líneas Diagonales
    elif(tablero[0] == tablero[4] == tablero[8] != ' '):
        estado_actual = "Ganador"
    elif(tablero[6] == tablero[4] == tablero[2] != ' '):
        estado_actual = "Ganador"

    else:
        estado_actual = "Jugando"

    return estado_actual


#Constantes iniciales
jugador_actual = "X"
jugador_actual = "X"
estado_actual = "Jugando"

turno = 1
print("Estructura Del Tablero: ")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print("El jugador X Comienza: ")

while(True):

    print("Turno del Jugador %s" % jugador_actual)
    posicion = int(input("Elija la poscion donde tirar: (1-9): ")) - 1

    if posicion>=0 or posicion<=9:

        if tablero[posicion] != " ":
            print("La casilla ocupada %s, Seleccióne Otra Ubicación " % str(posicion))
            continue
        else:
            tablero[posicion] = jugador_actual
            turno = turno + 1
    else:
        print("Posicion no valida")
        continue

    dibujar_tablero(tablero)

    estado_actual = estado_del_juego(tablero)

    if estado_actual == "Jugando":

        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("Ganador: %s" % jugador_actual)
        break

    if turno >= 10:
        print("Empate")
        break
