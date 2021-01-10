import sys
import os
import tty
import termios

if(len(sys.argv) == 1):
	print("\n¡No se encontraron argumentos!\n\nSaliendo del programa...\n")
	sys.exit()

if (os.path.exists(sys.argv[1]) == False):
	with open(sys.argv[1], "w+") as creator:
		creator.write("Cédula,Nombres,Apellidos,Ahorros,Contraseña,Datos\n")

def ID_Exist(C):
	with open(sys.argv[1], "r") as reader:
		if str(C) + "," in reader.read():
			return True

def Find():
	print("\nFavor ingresar la cédula a buscar: ")
	FindID = ReadInt()
	Found = ""

	if(ID_Exist(FindID)):
		with open(sys.argv[1], "r") as reader:
			data = reader.readlines()
			for i in data:
				Val = i[0:i.index(',') + 1]
				if (Val == FindID +  ',' and FindID != "Cédula"):
					Found = i

	if Found == "":
		print("\nLa cédula ingresada nunca ha sido registrada...")

	return Found, FindID

def Getch():

	FD = sys.stdin.fileno()

	OldSettings = termios.tcgetattr(FD)

	try:
		tty.setraw(FD)
		Ch = sys.stdin.read(1).strip('\n')

	finally:
		termios.tcsetattr(FD, termios.TCSADRAIN, OldSettings)

	return Ch

def ReadInt():

	Integer = ''

	while True:

		Char = Getch()

		if Char.isdigit():
			print(Char, end = '', flush = True)
			Integer += Char

		elif Char == '\x7f':
			print('\b \b', end = '', flush = True)
			Integer = Integer[:-1]

		elif Char == '\r':
			print('\r')
			break

	return Integer

def ReadChar():

	Stringer = ''

	while True:

		Char = Getch()

		if Char.isalpha():
			print(Char, end = '', flush = True)
			Stringer += Char

		elif Char == '\x7f':
			print('\b \b', end = '', flush = True)
			Stringer += Stringer[:-1]

		elif Char == '\r':
			print('\r')
			break

	return Stringer

def ReadDecimal():

	Integer = ''

	while True:

		Char = Getch()

		if Char.isdigit() or Char == '.' or Char == ',':
			print(Char, end = '', flush = True)
			Integer += Char

		elif Char == '\x7f':
			print('\b \b', end = '', flush = True)
			Integer = Integer[:-1]

		elif Char == '\r':
			print('\r')
			break

	Decimal = "%.2f" % float(Integer)

	return Decimal

def FirstPassword():

	F_Password = ''

	print("\nContraseña: ")

	while True:

		Char = Getch()

		if Char.isprintable():
			print('*', end = '', flush = True)
			F_Password += Char

		elif Char == '\x7f':
			print('\b \b', end = '', flush = True)
			F_Password = F_Password[:-1]

		elif Char == '\r':
			print('\r')
			break

	return F_Password

def ConfirmPassword():

	C_Password = ''

	print("\nConfirmar contraseña: ")

	while True:

		Char = Getch()

		if Char.isprintable():
			print('*', end = '', flush = True)
			C_Password += Char

		elif Char == '\x7f':
			print('\b \b', end = '', flush = True)
			C_Password = C_Password[:-1]

		elif Char == '\r':
			print('\r')
			break

	return C_Password

def ReadPassword():

	PassF = FirstPassword()
	PassC = ConfirmPassword()

	while(PassF != PassC):

		print("\n¡Las contraseñas no coinciden!")

		PassF = FirstPassword()
		PassC = ConfirmPassword()

	return PassF

def F_Encode():

	ret = 0 

	# ENCODE SEX

	Sex_V = int(0)

	while True:
		try:
			print("\nGénero (M|F): ")
			Sex = ReadChar().upper()
			if Sex in ["M","F"]:
				break
			else:
				print("\n¡Debe ingresar Masculino (M) o Femenino (F)!")
		except:
			continue

	if Sex == "M":
		Sex_V = int(0)
	elif Sex == "F":
		Sex_V = int(1)

	# ENCODE CIVIL STATUS

	Civil_V = int(0)

	while True:
		try:
			print("\nEstado civil (S|C): ")
			Civil = ReadChar().upper()
			if Civil in ["S","C"]:
				break
			else:
				print("\n¡Debe ingresar Solter@ (S) o Casad@ (C)!")
		except:
			continue

	if Civil == "S":
		Civil_V = int(0)
	elif Civil == "C":
		Civil_V = int(1)

	# ENCODE DEGREE

	print("\nGrado <--> N|B|G|P|D <--> Ninguno|Bachillerato|Grado|Posgrado|Doctorado")

	Degree_V = int(0)

	while True:
		try:
			print("\nGrado académico: ")
			Degree = ReadChar().upper()
			if Degree in ["N", "B", "G", "P" , "D"]:
				break
			else:
				print("\n¡Debe ingresar un caracter válido!")
				print("\nGrado: I|M|G|P| == Inicial|Medio|Grado|Posgrado")		
		except:
			continue

	if Degree == "I":
		Degree_V = int(0)
	elif Degree == "M":
		Degree_V = int(1)
	elif Degree == "G":
		Degree_V = int(2)
	elif Degree == "P":
		Degree_V = int(3)

	# AGE IS ON THE LEFTMOST

	print("\nEdad: ")

	Age = int(ReadInt())

	ret = Age

	# SEX POSITION

	ret = ret << 1 
	ret = ret | Sex_V

	# CIVIL POSITION

	ret = ret << 1
	ret = ret | Civil_V

	# DEGREE IS ON THE LEFTMOST

	ret = ret << 2 
	ret = ret | Degree_V

	return ret

def F_Decode(): # MAY BE NEEDED LATER ON

	F_Data = F_Encode()

	# GET THE TWO BITS FROM RIGHT TO GET DEGREE

	bit2 = 3 # 0000011

	Degree_V = F_Data & bit2

	if Degree_V == 0:
		Degree = "Inicial"
	elif Degree_V == 1:
		Degree = "Medio"
	elif Degree_V == 2:
		Degree = "Grado"
	elif Degree_V == 3:
		Degree = "Posgrado"
		
	# GET THE 1 BIT FROM RIGHT TO GET CIVIL STATUS

	F_Data = F_Data >> 2

	bit1 = 1 # 0000001
		
	Civil_V = F_Data & bit1

	if Civil_V == 0:
		Civil = "Soltero"
	elif Civil_V == 1:
		Civil = "Casado"

	# GET THE 1 BIT FROM RIGHT TO GET SEX

	F_Data = F_Data >> 1

	bit1 = 1 # 0000001

	Sex_V = F_Data & bit1

	if Sex_V == 0:
		Sex = "Masculino"
	elif Sex_V == 1:
		Sex = "Femenino"

	# GET THE REMAINING BITS FOR AGE

	F_Data = F_Data >> 1 

	Age = F_Data

	return Sex, Civil, Degree, Age

while (True):
	Menu = input("\nCapturar (C) | Listar (L) | Buscar (B) | Editar (E) | Eliminar (X) | Salir (S) ----> ").upper()
	if(Menu == "C"):
		while(True):

			print("\nCédula: ")
			ID = ReadInt()
			print("\nNombres: ")
			Name = ReadChar()
			print("\nApellidos: ")
			LastName = ReadChar()
			print("\nAhorros: ")
			Savings = ReadDecimal()
			FinalData = F_Encode()
			Password = ReadPassword()

			if(ID_Exist(ID)):
				print("\n¡Cédula existente!\n\nFavor ingresar cédula correcta...")
			else:
				while (True):
					Option = input("\nAgregar (A) | Grabar (G) | Salir (S) ---> ").upper()

					if(Option == "A"):
						break
					elif(Option == "G"):
						Grabar = input("\nGrabar: (Y/N) --> ").upper()
						if(Grabar == "Y"):
							with open(sys.argv[1], "a") as writer:
								writer.write(ID + "," + Name + "," + LastName + "," + Savings + "," + Password + "," + str(FinalData) + "\n")
						elif(Grabar == "N"):
							continue
					elif(Option == "S"):
						print("\nSaliendo del programa...\n")
						sys.exit()
					else:
						continue

	elif (Menu == "L"):
		print()
		with open(sys.argv[1], "r") as reader:
			data = reader.readlines()
			for i in data:
				datos = i.replace("\n", "")
				print(datos)

	elif (Menu == "B"):
		Found,FindID = Find()
		print(Found)

	elif (Menu == "E"):
		Found, FindID = Find()

		print("\n"+Found)

		while(True):

			print("\nFavor ingresar los nuevos datos: ")
			print("\nCédula: ")
			NewID = ReadInt()
			print("\nNombres: ")
			NewName = ReadChar()
			print("\nApellidos: ")
			NewLastName = ReadChar()
			print("\nAhorros: ")
			NewSavings = ReadDecimal()
			NewFinalData = F_Encode()
			NewPassword = ReadPassword()

			NewVals = (NewID + "," + NewName + "," + NewLastName + "," + NewSavings + "," + NewPassword + "," + str(NewFinalData) + "\n")

			if(ID_Exist(NewID)):
				print("\n¡Cédula existente!\n\nFavor ingresar cédula correcta...\n")
			else:
				with open(sys.argv[1], "r+") as reader, open(sys.argv[1], "a") as writer:
					data = reader.readlines()
					reader.truncate(0)
					for line in data:
						if Found in line:
							line = line.replace(Found, NewVals)
						writer.write(line)
				break

	elif (Menu == "X"):

		Found, FindID = Find()

		if(Found == "" and FindID  == ""):
			continue

		print(Found)

		while(True):
			Eliminate = input("¿Está seguro que desea eliminar el usuario? (Y/N) ---> ").upper()

			if(Eliminate == "Y"):
				with open(sys.argv[1], "r+") as reader:
					data = reader.readlines()

				os.remove(sys.argv[1])

				with open(sys.argv[1], "w+") as creator:
					for line in data:
						if Found in line:
							line = ""
						creator.write(line)
				break

			elif(Eliminate == "N"):
				break
			else:
				print("¡La opción ingresada no es válida!\n")
				break

	elif (Menu == "S"):
		print("\nSaliendo del programa...\n")
		sys.exit()
	else:
		print("\nLa opción ingresada no es válida...\n\nFavor intente nuevamente...")
		continue
