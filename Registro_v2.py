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

while (True):
    Menu = input("\nCapturar (C) | Listar (L) | Buscar (B) | Salir (S) ----> ").upper()
    if(Menu == "C"):
        while(True):

            ID = input("\nCédula: ")
            Name = input("\nNombres: ")
            LastName = input("\nApellidos: ")
            Age = input("\nEdad: ")
            
            if(ID == "" and Name == "" and LastName == "" and Age == ""):
                print("\n¡Ningún dato ingresado!.\n\nSaliendo del programa...\n")
                break    

            if(ID_Exist(ID)):
                print("\n¡Cédula existente!\n\nFavor ingresar cédula correcta...\n")
            else:
                while (True):
                    Option = input("\nAgregar (A) | Grabar (G) | Salir (S) ---> ").upper()

                    if (Option == "G"):
                        Grabar = input("\nGrabar: (Y/N) --> ").upper()
                        if(Grabar == "Y"):
                            with open(sys.argv[1], "a") as writer:
                                writer.write(ID + "," + Name + "," + LastName + "," + Age + "\n")
                        elif(Grabar == "N"):
                            continue
                    elif(Option == "A"):
                        break
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
        FindID = input("\nIngrese la cédula a buscar: ")
        print("")
        if(ID_Exist(FindID)):
            with open(sys.argv[1], "r") as reader:
                data = reader.readlines()
                for i in data:
                    if FindID + "," in i:
                        print(i)
        else:
            print("La cédula ingresada nunca ha sido registrada...")
            continue

    elif (Menu == "S"):
        print("\nSaliendo del programa...\n")
        sys.exit()

    else:
        print("La opción introducida no es válida.\n\nIntente nuevamente...\n")
