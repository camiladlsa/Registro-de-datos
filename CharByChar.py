import getpass

def HasDigits(string):
	return any(char.isdigit() for char in string)


Name = input("\nNombres: ")

while HasDigits(Name):
	print("\nEl nombre solo debe contener letras.\n\nFavor intente nuevamente.")
	Name = input("\nNombres: ")

LastName = input("\nApellidos: ")
while HasDigits(LastName):
	print("\nEl apellido solo debe contener letras.\n\nFavor intente nuevamente.")
	LastName = input("\nApellidos: ")


while True:
	try:
		Age = int(input("\nEdad: "))
		break
	except:
		print("\n¡Favor ingresar un entero!")

while True:
	try:
		Ahorros = float(input("\nAhorros: "))
		break
	except:
		print("\n¡Favor ingresar valor decimal!")

print("\nIngrese su contraseña: ", end = "")
Password = getpass.getpass()
print("\nConfirme su contraseña: ", end = "")
PasswordConfirm = getpass.getpass()

if Password == PasswordConfirm:
	print("\n¡Éxito!\n")
else:
	print("\n¡Las contraseñas no coinciden!\n")
