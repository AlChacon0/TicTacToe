#Crear tablero de juego
tablero = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

#Mostrar tablero
fila = 0
columna = 0
for lista in tablero:
    while columna < 3:
        print(' ' + tablero[fila][columna] + ' |', end='')
        columna += 1
    print("")
    if fila < 2: print('---+---+---|')
    fila += 1
    columna = 0
