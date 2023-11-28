from clases import *

# Creamos el tablero, y los jugadores.

a = 1
b = 0
c = 0

print(a == b == c)


tablero = Entorno()
jugador1 = Jugador()
jugador2 = Jugador()

# Dibujamos el tablero:

tablero.dibujarTablero()


print("Bienvenido al juego del tres en raya para dos jugadores.")

# Creamos al jugador 1 y le decimos qué ficha quiere usar:
ficha = input("Jugador 1, elige tu ficha: X o O --> ")
jugador1.elegirFicha(ficha)

# Creamos al jugador 2 y le cedemos la ficha contraria:
if jugador1.ficha == "x":
    jugador2.elegirFicha("o")
else:
    jugador2.elegirFicha("x")



while tablero.victoria == False:
    
    # Solicitamos la jugada al jugador actual:
    jugada = input("Jugador "+ str(tablero.jugadorActual) + " es tu turno. ¿Dónde quieres colocar tu ficha? --> ")
    
    # Si el jugador actual es el 1, ejecutaremos la jugada para el jugador1, sino, para el 2.
    if tablero.jugadorActual == 1:
        tablero.realizarJugada(jugada, jugador1.ficha)
    else:
        tablero.realizarJugada(jugada, jugador2.ficha)
    
    tablero.comprobarVictoria()
    
    if tablero.ganador == 1:
        jugador1.declararVictoria()
    elif tablero.ganador == 2:
        jugador2.declararVictoria()
    else:
        pass

    
    # A partir de aqui, preguntar si se quiere volver a jugar y poner todo a 0 (sobre todo comprobarVictoria y ganador)