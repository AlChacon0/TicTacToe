#Crear tablero de juego
tablero = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
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
    tableroGirado = [l.copy() for l in tablero]
    ganador = False
    
    for lista in tablero:
        #Revisar Filas
        if lista == ganadorXFila or lista == ganadorOFila:
            ganador = True
        
    #Girar Tablero
    while fila < 3:
        while columna < 3:
            tableroGirado[fila][columna] = tablero[columna][2-fila]
            columna += 1
        fila += 1

    return ganador    

def girarTablero():
    fila = 0
    columna = 0
    tableroGirado =[l.copy() for l in tablero]
    '''
    while fila < 3:
        while columna < 3:
            tableroGirado[fila][columna] = tablero[columna][2-fila]

            columna += 1
        fila += 1
        columna = 0
        '''
    tableroGirado[0][0] = tablero[0][2]
    tableroGirado[0][1] = tablero[1][2]
    tableroGirado[0][2] = tablero[2][2]

    tableroGirado[1][0] = tablero[0][1]
    tableroGirado[1][1] = tablero[1][1]
    tableroGirado[1][2] = tablero[2][1]

    tableroGirado[2][0] = tablero[0][0]
    tableroGirado[2][1] = tablero[1][0]
    tableroGirado[2][2] = tablero[2][0]
    for lista in tableroGirado:
        print(lista)

girarTablero()

#Iniciar juego
jugando = False
error = False
jugadores = ['X', 'O']
jugador = 0
while jugando:
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
            if revisarTablero(): break
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
    
