tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#Crear tablero de juego
def limpiarTablero():
    tablero = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

#Mostrar tablero
def printTablero(Mapa):
    fila, columna = 0, 0
    if Mapa:
        print(' 1   2   3')
        print(' |   |   |')
        print(' v   v   v')
    for lista in tablero:
        while columna < 3:
            print(' ' + tablero[fila][columna] + ' |', end='')
            columna += 1
        if Mapa:
            print('<-' + str(fila+1))
        else:
            print("")
        if fila < 2: print('---+---+---|')
        fila += 1
        columna = 0

#Revisar si alguien a gando
def revisarTablero():
    fila, columna = 0, 0

    ganadorXFila = ['X', 'X', 'X']
    ganadorOFila = ['O', 'O', 'O']
    ganadorXDiagonal1 = tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X'
    ganadorXDiagonal2 = tablero[0][2] == 'X' and tablero[1][1] == 'X' and tablero[2][0] == 'X'
    ganadorODiagonal1 = tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O'
    ganadorODiagonal2 = tablero[0][2] == 'O' and tablero[1][1] == 'O' and tablero[2][0] == 'O'
    ganadorDiagonal = ganadorXDiagonal1 or ganadorODiagonal1 or ganadorXDiagonal2 or ganadorODiagonal2
    tableroGirado = [l.copy() for l in tablero]
    ganador = False
    
    #Revisar Filas
    for lista in tablero:
        if lista == ganadorXFila or lista == ganadorOFila:
            ganador = True
        
    #Revisar Columnas
    tableroGirado = girarTablero()
    for lista in tableroGirado:
        if lista == ganadorXFila or lista == ganadorOFila:
            ganador = True

    #Revisar Diagonales
    if ganadorDiagonal:
        ganador = True
    return ganador    

def girarTablero():
    fila = 0
    columna = 0
    tableroGirado =[l.copy() for l in tablero]
    
    while fila < 3:
        while columna < 3:
            tableroGirado[fila][columna] = tablero[columna][2-fila]

            columna += 1
        fila += 1
        columna = 0
    return tableroGirado


#Iniciar juego
jugando = True
error = False
jugadores = ['X', 'O']
jugador = 0
while jugando:
    limpiarTablero()
    printTablero(False)
    casilla = input('Jugador ' + jugadores[jugador] + ': fila,columna: ')

    if casilla == 'salir':
        break

    try:
        filaCasilla = int(casilla[0]) - 1
        colCasilla = int(casilla[2]) - 1
    except:
        print('Error: elija fila y columna ej. 1,2')
        error = True
    
    if not error:
        if tablero[filaCasilla][colCasilla] == ' ':
            tablero[filaCasilla][colCasilla] = jugadores[jugador]
            print("")
            if revisarTablero(): 
                printTablero(False)
                print('GANADOR JUGADOR '+ jugadores[jugador])
                print('')
                respuesta = input('Volver a jugar (Y,N)?')
                if respuesta == 'Y':
                    limpiarTablero()
                else:
                    break
            if jugador == 0:
                jugador = 1
            else:
                jugador = 0
        else:
            print("Casilla ocupada")
        
    else:
        error = False
        printTablero(True)
        print('')