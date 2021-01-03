# Sex M|F (MALE|FEMALE)
# Civil Status: S|C (SINGLE|MARRIED)
# Degre: N|B|G|P|D (NONE|HIGH-SCHOOL|UNDERGRADUATE|MASTERS|DOCTORATE)

def Encode(Sex, Civil, Degree, Age):
	
	ret = 0 

	# ENCODE SEX

	sex_val = int(0)

	if Sex == "M":
		sex_val = int(0)
	elif Sex == "F":
		sex_val = int(1)

	# ENCODE CIVIL STATUS

	civil_val = int(0)

	if Civil == "S":
		civil_val = int(0)
	elif Civil == "C":
		civil_val = int(1)

	# ENCODE DEGREE

	d_val = int(0)

	if Degree == "N":
		d_val = int(0)
	elif Degree == "B":
		d_val = int(1)
	elif Degree == "G":
		d_val = int(2)
	elif Degree == "P":
		d_val = int(3)
	elif Degree == "D":
		d_val = int(4)

	# AGE IS ON THE LEFTMOST

	ret = Age

	# SEX POSITION

	ret = ret << 1 
	ret = ret | sex_val

	# CIVIL POSITION

	ret = ret << 1
	ret = ret | civil_val

	# DEGREE POSITION

	ret = ret << 2 
	ret = ret | d_val 

	return ret

def Decode(data):

		Sex = "M"
		Civil = "S"
		Degree = "N"
		Age = 0

		# GET THE TWO BITS FROM RIGHT TO GET DEGREE

		bit2 = 3 # 0000011

		d_val = data & bit2

		if d_val == 0:
			Degree = "Ninguno"
		elif d_val == 1:
			Degree = "Bachillerato"
		elif d_val == 2:
			Degree = "Grado"
		elif d_val == 3:
			Degree = "Maestría"
		elif d_val == 4:
			Degree = "Doctorado"

		# GET THE 1 BIT FROM RIGHT TO GET CIVIL STATUS

		data = data >> 2

		bit1 = 1 # 0000001
		
		civil_val = data & bit1

		if civil_val == 0:
			Civil = "Soltero"
		elif civil_val == 1:
			Civil = "Casado"

		# GET THE 1 BIT FROM RIGHT TO GET SEX

		data = data >> 1
		bit1 = 1 # 0000001

		sex_val = data & bit1

		if sex_val == 0:
			Sex = "Masculino"
		elif sex_val == 1:
			Sex = "Femenino"

		# GET THE REMAINING BITS FOR AGE

		data = data >> 1 

		Age = data

		return Sex, Civil, Degree, Age

