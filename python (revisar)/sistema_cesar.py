def msgCaesarSystem(level, message):

	msg = message
	lvl = level
	result = ""
	indice = 0
	alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	# Iteramos cada letra de la palabra introducida
	for i in msg:
		
		# Por cada letra, recorremos nuestra alfabeto, almacenando en x el indice que estamos iterando
		for x in range(len(alf)):
			if i == alf[x]:				# Si la letra que se está iterando es igual a alf[letra del diccionario iterada]
				indice = x + level		# Indice valdra el indice de la letra del diccionario + el nivel introducido
				break

		if i == " " or i == "," or i == "." or i == "¡" or i == "!" or i == "¿" or i == "?":
			result += i
		else:
			result += alf[indice]

	return(result)


def CaeSysMsg(level, message):
	msg = message
	lvl = level
	result = ""
	indice = 0
	alf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	# Iteramos cada letra de la palabra introducida
	for i in msg:
		
		# Por cada letra, recorremos nuestra alfabeto, almacenando en x el indice que estamos iterando
		for x in range(len(alf)):
			if i == alf[x]:				# Si la letra que se está iterando es igual a alf[letra del diccionario iterada]
				indice = x - level		# Indice valdra el indice de la letra del diccionario + el nivel introducido
				break

		if i == " " or i == "," or i == "." or i == "¡" or i == "!" or i == "¿" or i == "?":
			result += i
		else:
			result += alf[indice]

	return result


print("--------------------------- BIENVENIDO AL ENCRIPTADOR/DESENCRIPTADOR EN SISTEMA CESAR ---------------------------\n\n")


while True:

	

	try:

		opc = int(input(" ========== ¿Qué deseas hacer? ============\n    - 1. Encriptar un mensaje\n    - 2. Desencriptar un mensaje\n    - 3. Salir\n\n>> "))
		if opc == 1:
			mensaje = input("\nEscribe a continuación el mensaje que deseas encriptar: \n\n>> ")
			mensaje = mensaje.upper()
			nivel = int(input("\nIndica el nivel de encriptación: \n\n>> "))
			print("")
			print("MENSAJE ENCRIPTADO: " + msgCaesarSystem(nivel,mensaje) + "\n")

		elif opc == 2:
			mensaje = input("\nEscribe a continuación el mensaje que deseas desencriptar: \n\n>> ")
			mensaje = mensaje.upper()
			nivel = int(input("\nIndica el nivel de encriptación en el que está codificado: \n\n>> "))
			print("")
			print("MENSAJE DESENCRIPTADO: " + CaeSysMsg(nivel,mensaje) + "\n")

		elif opc == 3:
			break

	except ValueError:
		print("\n---- ERROR. INTRODUCE UNA OPCIÓN VALIDA ESCRIBIENDO EL NUMERO CORRESPONDIENTE ----\n")