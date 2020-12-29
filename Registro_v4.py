import os
import sys
import getpass

if(len(sys.argv) == 1):
	print("\n¡No se encontraron argumentos!\n\nSaliendo del programa...\n")
	sys.exit()

if (os.path.exists(sys.argv[1]) == False):
	with open(sys.argv[1], "w+") as creator:
		creator.write("Cédula,Nombres,Apellidos,Edad,Ahorros,Contraseña\n")

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
	return str(Age)

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
		print("\n¡Las contraseñas no coinciden!\n")
		Password = (getpass.getpass("\nIngrese su contraseña: "))
		PasswordConfirm = (getpass.getpass("\nConfirme su contraseña: "))
		continue				
	return Password

while (True):
	Menu = input("\nCapturar (C) | Listar (L) | Buscar (B) | Editar (E) | Eliminar (X) | Salir (S) ----> ").upper()
	if(Menu == "C"):
		while(True):
			ID = F_ID()
			Name = F_Name()
			LastName = F_LastName()
			Age = F_Age() 
			Savings = F_Savings()
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
								writer.write(ID + "," + Name + "," + LastName + "," + Age + "," + Savings + "," + Password + "\n")
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
			NewAge = F_Age()
			NewSavings = F_Savings()
			NewPassword = F_Password()

			NewVals = (NewID + "," + NewName + "," + NewLastName + "," + NewAge + "," + NewSavings + "," + NewPassword + "\n")

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
