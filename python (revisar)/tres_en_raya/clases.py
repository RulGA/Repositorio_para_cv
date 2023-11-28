class Entorno:

    def __init__(self):
        
        self.tableroActual = ["_","_","_"],["_","_","_"],["_","_","_"]
        self.dibujoTablero = """
           _ _ _
        1 |_|_|_|
        2 |_|_|_|
        3 |_|_|_|
           a b c
        """
        self.jugadorActual = 1
        self.victoria = False
        self.ganador = 0

    def dibujarTablero(self):

        self.dibujoTablero = """
           _ _ _
        1 |{0}|{3}|{6}|
        2 |{1}|{4}|{7}|
        3 |{2}|{5}|{8}|
           a b c
        """.format(self.tableroActual[0][0], self.tableroActual[1][0], self.tableroActual[2][0], self.tableroActual[0][1], self.tableroActual[1][1], self.tableroActual[2][1], self.tableroActual[0][2], self.tableroActual[1][2], self.tableroActual[2][2])

        print(self.dibujoTablero)

    def realizarJugada(self, jugada, ficha):
        if jugada == "a1":
            self.tableroActual[0][0] = ficha
            
        elif jugada == "a2":
            self.tableroActual[1][0] = ficha
        elif jugada == "a3":
            self.tableroActual[2][0] = ficha

        elif jugada == "b1":
            self.tableroActual[0][1] = ficha

        elif jugada == "b2":
            self.tableroActual[1][1] = ficha

        elif jugada == "b3":
            self.tableroActual[2][1] = ficha

        elif jugada == "c1":
            self.tableroActual[0][2] = ficha

        elif jugada == "c2":
            self.tableroActual[1][2] = ficha

        elif jugada == "c3":
            self.tableroActual[2][2] = ficha

        else:
            print("Jugada incorrecta. Introduce una jugada válida.")
            return

        if self.jugadorActual == 1:
            self.jugadorActual = 2
        else:
            self.jugadorActual = 1
        self.dibujarTablero()

    def comprobarVictoria(self):
        if self.tableroActual[0][0] == self.tableroActual[0][1] == self.tableroActual[0][2] != " " and self.tableroActual[0][0] != "_" or self.tableroActual[1][0] == self.tableroActual[1][1] == self.tableroActual[1][2] != " " and self.tableroActual[1][0] != "_" or self.tableroActual[2][0] == self.tableroActual[2][1] == self.tableroActual[2][2] != " " and self.tableroActual[2][0] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[1][0] == self.tableroActual[1][1] == self.tableroActual[1][2] != " " and self.tableroActual[1][0] != "_" or self.tableroActual[1][0] == self.tableroActual[1][1] == self.tableroActual[1][2] != " " and self.tableroActual[1][0] != "_" or self.tableroActual[1][0] == self.tableroActual[1][1] == self.tableroActual[1][2] != " " and self.tableroActual[1][0] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[2][0] == self.tableroActual[2][1] == self.tableroActual[2][2] != " " and self.tableroActual[2][0] != "_" or self.tableroActual[2][0] == self.tableroActual[2][1] == self.tableroActual[2][2] != " " and self.tableroActual[2][0] != "_" or self.tableroActual[2][0] == self.tableroActual[2][1] == self.tableroActual[2][2] != " " and self.tableroActual[2][0] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[0][0] == self.tableroActual[1][0] == self.tableroActual[2][0] != " " and self.tableroActual[0][0] != "_" or self.tableroActual[0][1] == self.tableroActual[1][1] == self.tableroActual[2][1] != " " and self.tableroActual[0][1] != "_" or self.tableroActual[0][2] == self.tableroActual[1][2] == self.tableroActual[2][2] != " " and self.tableroActual[0][2] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[0][1] == self.tableroActual[1][1] == self.tableroActual[2][1] != " " and self.tableroActual[0][1] != "_" or self.tableroActual[0][1] == self.tableroActual[1][1] == self.tableroActual[2][1] != " " and self.tableroActual[0][1] != "_" or self.tableroActual[0][1] == self.tableroActual[1][1] == self.tableroActual[2][1] != " " and self.tableroActual[0][1] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[0][2] == self.tableroActual[1][2] == self.tableroActual[2][2] != " " and self.tableroActual[0][2] != "_" or self.tableroActual[0][2] == self.tableroActual[1][2] == self.tableroActual[2][2] != " " and self.tableroActual[0][2] != "_" or self.tableroActual[0][2] == self.tableroActual[1][2] == self.tableroActual[2][2] != " " and self.tableroActual[0][2] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[0][0] == self.tableroActual[1][1] == self.tableroActual[2][2] != " " and self.tableroActual[0][0] != "_" or self.tableroActual[0][0] == self.tableroActual[1][1] == self.tableroActual[2][2] != " " and self.tableroActual[0][0] != "_" or self.tableroActual[0][0] == self.tableroActual[1][1] == self.tableroActual[2][2] != " " and self.tableroActual[0][0] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        elif self.tableroActual[0][2] == self.tableroActual[1][1] == self.tableroActual[2][0] != " " and self.tableroActual[0][2] != "_" or self.tableroActual[0][2] == self.tableroActual[1][1] == self.tableroActual[2][0] != " " and self.tableroActual[0][2] != "_" or self.tableroActual[0][2] == self.tableroActual[1][1] == self.tableroActual[2][0] != " " and self.tableroActual[0][2] != "_":
            self.victoria = True
            if self.jugadorActual == 1:
                print("¡El jugador 2 ha ganado!")
                self.ganador = 2
            else:
                print("¡El jugador 1 ha ganado!")
                self.ganador = 1
        else:
            self.victoria = False

class Jugador():

    def __init__(self):
        self.victoria = False

    def elegirFicha(self, ficha):
        self.ficha = ficha
    
    def declararVictoria(self):
        self.victoria = True