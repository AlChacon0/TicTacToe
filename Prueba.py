#Crear tablero de juego
tablero = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

tableroGirado = [l.copy() for l in tablero]


tableroGirado[0][0] = str(tablero[0][2])
tableroGirado[0][1] = tablero[1][2]
tableroGirado[0][2] = tablero[2][2]

tableroGirado[1][0] = tablero[0][1]
tableroGirado[1][1] = tablero[1][1]
tableroGirado[1][2] = tablero[2][1]

tableroGirado[2][0] = tablero[0][0]
tableroGirado[2][1] = tablero[1][0]
tableroGirado[2][2] = tablero[2][0]

print(tableroGirado)