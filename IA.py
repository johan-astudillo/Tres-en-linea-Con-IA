# Autores: Johan Astudillo, Luis Pedraza


# Importamos el modulo random
import random


def DibujarTablero(tablero):
    # "tablero" es una lista de 10 cadenas que representamos en el tablero (Ignoramos index0)

    # Marcamos lugar de juego y lugar de instrucciones
    print("")
    print('   Juego' + "     Instrucciones")
    print("")

    # Imprimos el tablero con sus respectivas intrucciones 

    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9] + "     7 | 8 | 9")

    print('-----------' + "   -----------")

    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6] + "     4 | 5 | 6")

    print('-----------' + "   -----------")

    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3] + "     1 | 2 | 3")


def IngresarLetraJugador():
    # Ingresar la letra con la que queremos jugar

    # return: Letra de nuestro jugador como 1 elemento y la de la IA como segundo 
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('Elige O o X para poder Jugar')

        # Hacer que la entrada aparezca en mayusculas
        letra = input().upper()

    # si el primer elemento que el jugador escoja estara de primero en la tupla, el otro será el computador
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def primerJugada():

    # Un random escoge la persona que va primero
    # randint escoge entre 2 numeros X o O
    if random.randint(0, 1) == 0:
        return 'Inteligencia Artificial'
    else:
        return 'jugador'


def jugarDeNuevo():
    # esta función va a retornar True si el jugador quiere jugar de nuevo si la inicial tiene s o S retorna si inmediatamente
    print('Quieres jugar de nuevo (sisas o nonas)')
    return input().lower().startswith('s')


# Moverse en el tablero segun la letra que pongas
def moverse(tablero, letra, mover):
    tablero[mover] = letra


# ES GANADOR SI ACUMULO UNA LETRA POR FILA COLUMNA O DIAGONAL
def esGanador(tab, le):
    # Según la letra de ljugador está función va devolver si el jugador o la maquina ha ganado
    # cambiamos tablero por tab y le por letra
    return ((tab[7] == le and tab[8] == le and tab[9] == le) or
            (tab[4] == le and tab[5] == le and tab[6] == le) or  # medio
            (tab[1] == le and tab[2] == le and tab[3] == le) or  # abajo
            (tab[7] == le and tab[4] == le and tab[1] == le) or  # izquierd
            (tab[8] == le and tab[5] == le and tab[2] == le) or  # mitad
            (tab[9] == le and tab[6] == le and tab[3] == le) or  # derecha
            (tab[7] == le and tab[5] == le and tab[3] == le) or  # diagonal iz
            (tab[9] == le and tab[5] == le and tab[1] == le))  # diagonal de


def copiaTablero(tablero):
    # dusplicado del tablero
    duptablero = []

    # Reccorremos tablero y anexamos en la posicion duplicamos
    for i in tablero:
        duptablero.append(i)

    return duptablero


# Es un espacio vació al mover el tablero
def espacioVacio(tablero, mover):
    # return true si esta libre el tablero 
    return tablero[mover] == ' '


# Movimiento de jugador
def movimientoJug(tablero):
    # el jugador escribira su movimiento, mientran no se cumpla la condición retorne lo mismo
    mover = ' '

    # Transformar cadena en lista si hay una letra ya posicionada imprimira lo mismo si no hay imprimira la letra en la posicion del numero
    while mover not in '1 2 3 4 5 6 7 8 9'.split() or not espacioVacio(tablero, int(mover)):
        print('Tu siguiente movimiento del (1-9) si esta seleccionado escoja otra posicion')
        mover = input()
    return int(mover)


# Elegir un movimiento Random de la lista
def elegirMovimientoRandom(tablero, moversList):
    # return movimiento valido de la lista del tablero
    # returns None si no hay un movimiento valido
    possiblemovers = []
    for i in moversList:
        if espacioVacio(tablero, i):
            possiblemovers.append(i)

    if len(possiblemovers) != 0:
        return random.choice(possiblemovers)
    else:
        return None


# Obtener el movimiento de la IA
def getMovIA(tablero, letraIA):
    # Si la letra de la IA es X por ende la letra del Jugador es la O y viceversa
    if letraIA == 'X':
        jugadorLetra = 'O'
    else:
        jugadorLetra = 'X'

    # ALGORITMO DEL A INTELIGENCIA ARTIFICIAL

    # Primero Verificamos  si podemos ganar en el proximo movimiento
    for i in range(1, 10):
        copiar = copiaTablero(tablero)
        if espacioVacio(copiar, i):
            moverse(copiar, letraIA, i)
            if esGanador(copiar, letraIA):
                return i

    # Comprobamos si el jugador puede ganar en su proximo movimiento
    for i in range(1, 10):
        copiar = copiaTablero(tablero)
        if espacioVacio(copiar, i):
            moverse(copiar, jugadorLetra, i)
            if esGanador(copiar, jugadorLetra):
                return i

    # Intenta tomar las esquinas si estan libres
    mover = elegirMovimientoRandom(tablero, [1, 3, 7, 9])
    if mover != None:
        return mover

    # Intenta tomar el centro, si esta libre
    if espacioVacio(tablero, 5):
        return 5

    # Mover en uno de los lados
    return elegirMovimientoRandom(tablero, [2, 4, 6, 8])


def tableroLleno(tablero):
    # Retorna true si se ocupa cada espacio en el tablero, en lo contrario es false
    for i in range(1, 10):
        if espacioVacio(tablero, i):
            return False
    return True


print('Bienvenidos a Triqui Vs IA')

while True:
    # Reiniciar el tablero
    elTablero = [' '] * 10
    jugadorLetra, letraIA = IngresarLetraJugador()
    turno = primerJugada()
    print(' ' + turno + ' Empieza primero')
    estaJugando = True

    # SI EL JUGADOR JUEGA
    while estaJugando:
        if turno == 'jugador':
            # Player's turno.
            DibujarTablero(elTablero)
            mover = movimientoJug(elTablero)
            moverse(elTablero, jugadorLetra, mover)

            if esGanador(elTablero, jugadorLetra):
                DibujarTablero(elTablero)
                print('¡GANASTEEEEEEEEEEEEEEEEEE!')
                estaJugando = False
            else:
                if tableroLleno(elTablero):
                    DibujarTablero(elTablero)
                    print('El juego es un empate')
                    break
                else:
                    turno = 'Inteligencia Artificial'

        else:
            # Turno del computador SI LA IA JUEGA
            mover = getMovIA(elTablero, letraIA)
            moverse(elTablero, letraIA, mover)

            if esGanador(elTablero, letraIA):
                DibujarTablero(elTablero)
                print('JAJA TE GANARON')
                estaJugando = False
            else:
                if tableroLleno(elTablero):
                    DibujarTablero(elTablero)
                    print('¡EMPATEEEEEEEEEEEEEEEEEEEEE!')
                    break
                else:
                    turno = 'jugador'

    if not jugarDeNuevo():
        break
