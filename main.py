#Crear tablero de juego
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#Mostrar tablero
def printTablero(Mapa):
    fila = 0
    columna = 0
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

#Iniciar juego
jugando = True
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
        tablero[filaCasilla][colCasilla] = jugadores[jugador]
        print("")
        if jugador == 0:
            jugador = 1
        else:
            jugador = 0
        
    else:
        error = False
        printTablero(True)
        print('')
    

'''
->Evitar uso de una casilla ya marcada
->Declarar ganador
'''