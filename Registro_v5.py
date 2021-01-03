import os
import sys
import getpass

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

def HasDigits(string):
	return any(char.isdigit() for char in string)

def Find():

	FindID = F_ID()
	Found = ""

	if(FindID == ""):
		print("Error: No se ha introducido ningún dato")
	elif(ID_Exist(FindID)):
		with open(sys.argv[1], "r") as reader:
			data = reader.readlines()
			for i in data:
				Val = i[0:i.index(',') + 1]
				if (Val == FindID +  ',' and FindID != "Cédula"):
					Found = i

	if Found == "":
		print("\nLa cédula ingresada nunca ha sido registrada...")

	return Found, FindID

def F_ID():
	while True:
		try:
			ID = int(input("\nCédula: "))
			break
		except:
			print("\n¡Favor ingresar un entero!")
	return str(ID)

def F_Name():
	Name = input("\nNombres: ")
	while HasDigits(Name):
		print("\nEl nombre solo debe contener letras.\n\nFavor intente nuevamente.")
		Name = input("\nNombres: ")
	return Name

def F_LastName():
	LastName = input("\nApellidos: ")
	while HasDigits(LastName):
		print("\nEl apellido solo debe contener letras.\n\nFavor intente nuevamente.")
		LastName = input("\nApellidos: ")
	return LastName

def F_Age():
	while True:
		try:
			Age = int(input("\nEdad: "))
			break
		except:
			print("\n¡Favor ingresar un entero!")
	return Age

def F_Savings():
	while True:
		try:
			Savings = float(input("\nAhorros: "))
			break
		except:
			print("\n¡Favor ingresar un valor decimal!")
	return str(Savings)

def F_Password():
	Password = (getpass.getpass("\nIngrese su contraseña: "))
	PasswordConfirm = (getpass.getpass("\nConfirme su contraseña: "))
	while(Password != PasswordConfirm):
		print("\n¡Las contraseñas no coinciden!")
		Password = (getpass.getpass("\nIngrese su contraseña: "))
		PasswordConfirm = (getpass.getpass("\nConfirme su contraseña: "))
		continue				
	return Password

def F_Encode():

	ret = 0 

	# ENCODE SEX

	Sex_V = int(0)

	Sex = input("\nGénero (M|F): ").upper()
	if Sex not in ["M", "F"]:
		while True:
			print("\n¡Debe ingresar Masculino (M) o Femenino (F)!")
			Sex = input("\nGénero (M|F): ").upper()
			break

	if Sex == "M":
		Sex_V = int(0)
	elif Sex == "F":
		Sex_V = int(1)

	# ENCODE CIVIL STATUS

	Civil_V = int(0)

	Civil = input("\nEstado civil (S|C): ").upper()
	if Civil not in ["S", "C"]:
		while True:
			print("\n¡Debe ingresar Solter@ (S) o Casad@ (C)!")
			Civil = input("\nEstado civil (S|C): ").upper()
			break

	if Civil == "S":
		Civil_V = int(0)
	elif Civil == "C":
		Civil_V = int(1)

	# ENCODE DEGREE

	print("\nGrado <--> N|B|G|P|D <--> Ninguno|Bachillerato|Grado|Posgrado|Doctorado")

	Degree_V = int(0)

	Degree = input("\nGrado académico: ").upper()
	if Degree not in ["N", "B", "G", "P" , "D"]:
		while True:
			print("\n¡Debe ingresar un caracter válido!")
			print("\nGrado: N|B|G|P|D == Ninguno|Bachillerato|Grado|Posgrado|Doctorado")
			Degree = input("\nGrado académico: ").upper()
			break

	if Degree == "N":
		Degree_V = int(0)
	elif Degree == "B":
		Degree_V = int(1)
	elif Degree == "G":
		Degree_V = int(2)
	elif Degree == "P":
		Degree_V = int(3)
	elif Degree == "D":
		Degree_V = int(4)

	# AGE IS ON THE LEFTMOST

	Age = F_Age()

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

def F_Decode(F_Data): # MAY BE NEEDED LATER ON

	F_Encode()

	# GET THE TWO BITS FROM RIGHT TO GET DEGREE

	bit2 = 3 # 0000011

	Degree_V = F_Data & bit2

	if Degree_V == 0:
		Degree = "Ninguno"
	elif Degree_V == 1:
		Degree = "Bachillerato"
	elif Degree_V == 2:
		Degree = "Grado"
	elif Degree_V == 3:
		Degree = "Posgrado"
	elif Degree_V == 4:
		Degree = "Doctorado"

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
			ID = F_ID()
			Name = F_Name()
			LastName = F_LastName()
			Savings = F_Savings()
			FinalData = F_Encode()
			Password = F_Password()

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

			print("Favor ingresar los nuevos datos:")
			NewID = F_ID()
			NewName = F_Name()
			NewLastName = F_LastName()
			NewSavings = F_Savings()
			NewFinalData = F_Encode()
			NewPassword = F_Password()

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
		print("\nLa opción ingresada no es válida.\n\nFavor intente nuevamente...")
		continue
