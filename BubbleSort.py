def BubbleSort(Array):

	Number = len(Array)

	for i in range(Number - 1):
		for j in range(0, Number - i - 1):
			if(Array[j] > Array[j+1]):
				Array[j], Array[j+1] = Array[j+1], Array[j]

Array = [64, 34, 25, 12, 22, 11, 90, 14, 14, 21, 23, 30, 29, 28, 9]

BubbleSort(Array)

print("\nEl arreglo ordenado es: [", end = '')
for i in range(len(Array)):
	print("%d" %Array[i], end = '')
	if (i < (len(Array) - 1)):
		print(", ", end = '')
	else:
		print("]\n")
