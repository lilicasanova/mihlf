import numpy as np
import variables
import functions

def juego():
    #lo primero que hacemos es dar la bienvenida e imprimir el tablero
    print("Bienvenido a Hundir la Flota, Jugador 1. Vamos a empezar imprimiendo el tablero y los barcos")
    tablero_barcos_j1 = crear_tablero (size=10)
    tablero_barcos_j2 = crear_tablero (size=10)
    while vidas > 0:
        if turno_actual == jugador_1:
            '''
            a continuación, con el bucle while haciendo referencia al número de vidas mínimo para poder seguir jugando, 
            empezamos con la función colocar barco y vamos en orden
            '''
            colocar_barco2(tablero_barcos_j1, barcos, jugador_1)
            colocar_barcos1(tablero_barcos_j1, eslora)
            colocar_barcos2(tablero_barcos_j1, eslora)
            colocar_barcos3(tablero_barcos_j1, eslora)
            colocar_barcos4(tablero_barcos_j1, eslora)

            print(tablero_barcos_j1)

            '''
            una vez impresos, empezamos a pedir coordenadas al usuario para empezar a disparar a los barcos ya colocados
            '''

            disparo_j1

            if disparo_j1(tablero_barcos_j2) == vidas -1:
                turno_actual = jugador_2
            
            #si perdemos una vida, es el turno de jugador 2 (CPU)
                     
            if turno_contricante == jugador_2:
                #empezamos imprimiendo su tablero y sus barcos
                colocar_barco2(tablero_barcos_j2, barcos, jugador_2)
                colocar_barcos1(tablero_barcos_j2, eslora)
                colocar_barcos2(tablero_barcos_j2, eslora)
                colocar_barcos3(tablero_barcos_j2, eslora)
                colocar_barcos4(tablero_barcos_j2, eslora)

            print(tablero_barcos_j2)

            coordenadas_aleatorias

            if coordenadas_aleatorias(tablero_barcos_j1) == vidascpu -1:
                turno_actual = jugador_1


