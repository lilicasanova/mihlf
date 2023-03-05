import numpy as np
import variables

def crear_tablero(size=10):
    tablero = np.full((size,size), " ")
    return tablero

def obtener_coordenadas_aleatorias ():
    orientacion
    coord_x_random = np.random.randint(10)
    coord_y_random = np.random.randint(10)
    return coord_x_random, coord_y_random, orientacion


#función para colocar barcos de 1 de eslora
def colocar_barcos1(tablero_barcos_j1, eslora):
    counter = 0
    eslora = 1
    tablero_barcos_j1

    while True:
            obtener_coordenadas_aleatorias
            if eslora == 1:
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = print("O")
                counter = counter + 1            
            elif counter == 4:
                break

            return tablero_barcos_j1

 #función para colocar barcos de 2 de eslora
def colocar_barcos2(tablero_barcos_j1, eslora):

    counter = 0
    eslora = 2
    
    while True:
            
            obtener_coordenadas_aleatorias

            if eslora == 2:
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = print("O")
                counter = counter + 1

            if orientacion == "E":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "O":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random - eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "S":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_x_random - eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "N":
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_x_random + eslora] = "O"
                return tablero_barcos_j1
            
            if counter == 3:
                break

            return tablero_barcos_j1


def colocar_barco2(tablero_barcos_j1, barcos, jugador_1):
    barcos1 = 4
    barcos2= 3
    barcos3 = 2
    barcos4 = 1
    if jugador_1 == jugador_1:
        print("Imprimiendo los barcos del jugador 1...")
    else:
        print("Imprimiendo los barcos del jugador 2...")
    print(f"Barcos de uno de eslora: {barcos1}\nBarcos de dos de eslora: {barcos2}\nBarcos de tres de eslora: {barcos3}\nBarcos de cuatro de eslora: {barcos4}\nTotal de barcos a flote: {barcos1+barcos2+barcos3+barcos4}")
    tablero_barcos_j1 = colocar_barcos4(barcos4, tablero_barcos_j1)
    tablero_barcos_j1 = colocar_barcos3(barcos3, tablero_barcos_j1)
    tablero_barcos_j1 = colocar_barcos2(barcos2, tablero_barcos_j1)
    tablero_barcos_j1 = colocar_barcos1(barcos1, tablero_barcos_j1)
    return tablero_barcos_j1


#función para colocar barcos de 3 de eslora
def colocar_barcos3(tablero_barcos_j1, eslora):

    counter = 0
    eslora = 3

    while True:
            
            obtener_coordenadas_aleatorias

            if eslora == 3:
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = print("O")
                counter = counter + 1

            if orientacion == "E":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "O":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random - eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "S":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_x_random - eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "N":
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_x_random + eslora] = "O"
                return tablero_barcos_j1
            
            if counter == 2:
                break

            return tablero_barcos_j1
    
#función para colocar barcos de 4 de eslora
def colocar_barcos4(tablero_barcos_j1, eslora):
    counter = 0
    eslora = 4

    while True:
            
            obtener_coordenadas_aleatorias

            if eslora == 4:
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = print("O")

            if orientacion == "E":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random + eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "O":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_y_random - eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "S":
                        tablero_barcos_j1[coord_x_random, coord_y_random : coord_x_random - eslora] = "O"
                        return tablero_barcos_j1
            if orientacion == "N":
                tablero_barcos_j1[coord_x_random, coord_y_random : coord_x_random + eslora] = "O"
                return tablero_barcos_j1

            break

    return tablero_barcos_j1

#función para evitar que se monten unos barcos sobre otros con las coordenadas aleatorias

def evitar_solapar(tablero_barcos_j1, coord_x_random, coord_y_random, eslora, orientacion):
    orientacion
    eslora
    #colocar barco siempre que se pueda evitar solapar
    while not evitar_solapar (tablero_barcos_j1, coord_x_random, coord_y_random, eslora, orientacion):
       coord_x_random, coord_y_random = coord_x_random(tablero_barcos_j1), coord_y_random(tablero_barcos_j1)
       orientacion = random.choice(["N", "S", "E", "O"])
       colocar_barco(tablero_barcos_j1, coord_x_random, coord_y_random, eslora, orientacion)
       #aquí intentamos marcar el límite del tablero
    if orientacion == "E" or orientacion == "O":
        if coord_x_random + eslora > len(tablero_barcos_j1[0]):
            return False
    for i in range(eslora):
      if tablero_barcos_j1[coord_x_random][coord_y_random+i] == " ":
            return False
      else:
        if orientacion == "N" or orientacion == "S" + eslora > len(tablero_barcos_j1):
            return False
    for i in range(eslora):
      if tablero_barcos_j1[coord_x_random+i][coord_y_random] == " ":
        return False
    return True

#función para solicitar las coordenadas de disparo a través de input al jugador 1

def solicitar_coordenadas(jugador_1):
    print("Solicitando coordenadas al jugador...")

    '''Primero nos aseguramos de que todo esté correcto en la coordenada X, para poder continuar después con la coordenada Y. 
    Contemplamos las posibilidades de error, como salir del tablero o ingresar un caracter no válido'''

    while True:
        coordenada_x_jugador1 = int(input("Introduce una coordenada X"))
        if coordenada_x_jugador1 > 11:
            print("El número debe estar comprendido entre el 1 y el 10")
        if coordenada_x_jugador1 < 1: 
            print("El número debe estar comprendido entre el 1 y el 10")
        if coordenada_x_jugador1 == str:
            print("Debes introducir un número entero")
        if coordenada_x_jugador1 <= 10:
            break
        else: print ("No es válido, inténtalo de nuevo")

    while True: 
        coordenada_y_jugador1 = int(input("Introduce una coordenada Y"))
        if coordenada_y_jugador1 > 11:
            print("El número debe estar comprendido entre el 1 y el 10")
        if coordenada_y_jugador1 < 1: 
            print("El número debe estar comprendido entre el 1 y el 10")
        if coordenada_y_jugador1 == str:
            print("Debes introducir un número entero")
        if coordenada_y_jugador1 <= 10:
            print("Es correcto, vamos a ver si has hundido algo")
            break
        else: print ("No es válido, inténtalo de nuevo")

    return coordenada_x_jugador1, coordenada_y_jugador1, orientacion

#disparos jugador 2
def coordenadas_aleatorias(tablero_barcos_j1):
    coord_x_random = np.random.randint(10)[tablero_barcos_j1]
    coord_y_random = np.random.randint(10)[tablero_barcos_j1]

    while jugador_2 == jugador_2:
        obtener_coordenadas_aleatorias
        
        if tablero_barcos_j1[coord_x_random][coord_y_random] == "O":
          print("Has acertado! Sigue jugando")
          tablero_barcos_j1[coord_x_random][coord_y_random] == "X"
          return tablero_barcos_j1
        if tablero_barcos_j1[coord_x_random][coord_y_random] == " ":
          print("Lo siento, has fallado, suerte en la próxima")
          tablero_barcos_j1[coord_x_random][coord_y_random] == "-"
          vidascpu = vidascpu - 1
          return tablero_barcos_j1
        if tablero_barcos_j1[coord_x_random] not in range(10):
          print("Por favor, introduce coordenadas válidas")
        if tablero_barcos_j1[coord_y_random] not in range(10): 
          print("Por favor, introduce coordenadas válidas")
        if tablero_barcos_j1[coord_x_random][coord_y_random] == "X":
          print("Ya dijiste esa")
          tablero_barcos_j1[coord_x_random][coord_y_random] == "-"
          print(tablero_barcos_j2)
          vidascpu = vidascpu - 1
        return tablero_barcos_j1
    else:  
        print("¡No hundiste mi barco! Es el turno de la CPU")
        vidascpu = vidascpu - 1
        print("Te quedan {vidascpu} vidas")
        return tablero_barcos_j1


#función para que el jugador 1 dispare a través de input, con todas sus condicionales

def disparo_j1(tablero_barcos_j2, vidas):
    disparo_correcto = "X"
    orientacion
    while jugador_1 == jugador_1:
        solicitar_coordenadas(jugador_1)
        if tablero_barcos_j2[coordenada_x_jugador1][coordenada_y_jugador1] == "O":
          print("Has acertado! Sigue jugando")
          tablero_barcos_j2[coordenada_x_jugador1][coordenada_y_jugador1] == "X"
          return tablero_barcos_j2
        if tablero_barcos_j2[coordenada_x_jugador1][coordenada_y_jugador1] == " ":
          print("Lo siento, has fallado, suerte en la próxima")
          tablero_barcos_j2[coordenada_x_jugador1][coordenada_y_jugador1] == "-"
          vidas = vidas - 1
          return tablero_barcos_j2
        if tablero_barcos_j2[coordenada_x_jugador1] not in range(10):
          print("Por favor, introduce coordenadas válidas")
        if tablero_barcos_j2[coordenada_y_jugador1] not in range(10): 
          print("Por favor, introduce coordenadas válidas")
        if tablero_barcos_j2[coordenada_x_jugador1][coordenada_y_jugador1] == "X":
          print("Ya dijiste esa")
          tablero_barcos_j2[coordenada_x_jugador1][coordenada_y_jugador1] == "-"
          print(tablero_barcos_j2)
          vidas = vidas - 1
        return tablero_barcos_j2
    else:  
        print("¡No hundiste mi barco! Es el turno de la CPU")
        vidas = vidas - 1
        print("Te quedan {vidas} vidas")
        return tablero_barcos_j2
    
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

