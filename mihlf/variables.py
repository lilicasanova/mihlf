filas= 10
columnas= 10
mar= " "
jugador_1 = "j1"
jugador_2 = "j2"
tablero_barcos_j1 = crear_tablero()
tablero_disparos_j1= crear_tablero()
tablero_barcos_j2= crear_tablero()
eslora= 1, 2, 3, 4
eslora1 = 1
eslora2 = 2
eslora3 = 3
eslora4 = 4
vidas = 20
vidascpu = 20
barcos = 10
disparo_correcto = "X"
coordenada_x_jugador1= int(input("Introduce una coordenada X"))
coordenada_y_jugador1= int(input("Introduce una coordenada Y"))
coordenadas_jugador1 = coordenada_x_jugador1 + coordenada_y_jugador1
coord_x_random = np.random.randint(10)
coord_y_random = np.random.randint(10)
orientacion = np.random.choice(("N", "S", "E", "O"))
turno_actual = jugador_1
turno_contricante = jugador_2
barco_1_1= [(3,9)]
barco_1_2= [(6,1)]
barco_1_3= [(4,7)]
barco_1_4= [(9,9)]
barco_2_1= [(4,4), (5,4)]
barco_2_2= [(6,7), (6,8)]
barco_2_3= [(8,2), (9,2)]
barco_3_1= [(1,7), (1,8), (1,9)]
barco_3_2= [(2,2), (2,3), (2,4)]
barco_4_1= [(8,4), (8,5), (8,6), (8,7)]
size= 10

lista_barcos_jugador1= [barco_1_1,barco_1_2,barco_1_3,barco_1_4,barco_2_1,barco_2_2,barco_2_3,barco_3_1,barco_3_2,barco_4_1]

barcoj2_1_1= [(2,2)]
barcoj2_1_2= [(3,8)]
barcoj2_1_3= [(9,2)]
barcoj2_1_4= [(6,4)]
barcoj2_2_1= [(9,4), (9,5)]
barcoj2_2_2= [(9,7), (9,8)]
barcoj2_2_3= [(3,5), (3,6)]
barcoj2_3_1= [(5,6), (5,7), (5,8)]
barcoj2_3_2= [(7,6), (7,7), (7,8)]
barcoj2_4_1= [(4,2), (5,2), (5,3), (5,4)]

lista_barcos_jugador2= [barcoj2_1_1, barcoj2_1_2, barcoj2_1_3, barcoj2_1_4, barcoj2_2_1, barcoj2_2_2, barcoj2_2_3, barcoj2_3_1, barcoj2_3_2, barcoj2_4_1]