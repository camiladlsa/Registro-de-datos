import os
import sys

if(len(sys.argv) == 1):
    print("\n¡No se encontraron argumentos!\n\nSaliendo del programa...\n")
    sys.exit()

if (os.path.exists(sys.argv[1]) == False):
    with open(sys.argv[1], "w+") as creator:
        creator.write("Cédula,Nombres,Apellidos,Edad\n")

def ID_Exist(C):
    with open(sys.argv[1], "r") as reader:
        if C + "," in reader.read():
            return True

def Find():
	FindID = input("\nIngrese la cédula a buscar: ")
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

while (True):
    Menu = input("\nCapturar (C) | Listar (L) | Buscar (B) | Editar (E) | Eliminar (X) | Salir (S) ----> ").upper()
    if(Menu == "C"):
        while(True):
            ID = input("\nCédula: ")
            Name = input("\nNombres: ")
            LastName = input("\nApellidos: ")
            Age = input("\nEdad: ")
            
            if(ID == "" and Name == "" and LastName == "" and Age == ""):
                print("\nError: ¡Ningún dato ingresado!.\n\nSaliendo del programa...")
                break    

            if(ID_Exist(ID)):
                print("\n¡Cédula existente!\n\nFavor ingresar cédula correcta...\n")
            else:
                while (True):
                    Option = input("\nAgregar (A) | Grabar (G) | Salir (S) ---> ").upper()

                    if(Option == "A"):
                        break
                    elif(Option == "G"):
                        Grabar = input("\nGrabar: (Y/N) --> ").upper()
                        if(Grabar == "Y"):
                            with open(sys.argv[1], "a") as writer:
                                writer.write(ID + "," + Name + "," + LastName + "," + Age + "\n")
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
    	Found, FindID = Find()
    	print("\n",Found)

    elif (Menu == "E"):
    	Found, FindID = Find()

    	if(Found == "" and FindID  == ""):
    		continue

    	print(Found)

    	while(True):

    		print("Favor ingresar los nuevos datos:")
    		NewID = input("\nCédula: ")
    		NewName = input("\nNombres: ")
    		NewLastName = input("\nApellidos: ")
    		NewAge = input("\nEdad: ")
    		NewVals = NewID + "," + NewName + "," + NewLastName + "," + NewAge + "\n"

    		if(NewID == "" and NewName == "" and NewLastName == "" and NewAge == ""):
    			print("\nError: ¡Ningún dato ingresado!.\n")
    			break

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