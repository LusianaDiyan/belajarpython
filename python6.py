def lambda1():
	x = lambda a : a + 10
	print(x(5))

def lambda2():
	x = lambda a, b : a * b
	print(x(5, 6))

def lambda3():
	x = lambda a, b, c : a + b +c
	print(x(5, 6, 2))

def array1():
	cars = ["Ford", "Volvo", "BMW"]

	print(cars)

def array2():
	cars = ["Ford", "Volvo", "BMW"]

	x = cars[0]

	print(x)

def array3():
	cars = ["Ford", "Volvo", "BMW"]

	cars[0] = "Toyota"

	print(cars)

def array4():
	cars = ["Ford", "Volvo", "BMW"]

	x = len(cars)

	print(x)

def array5():
	cars = ["Ford", "Volvo", "BMW"]

	for x in cars:
	  print(x)

def array6():
	cars = ["Ford", "Volvo", "BMW"]

	cars.append("Honda")

	print(cars)

def array7():
	cars = ["Ford", "Volvo", "BMW"]

	cars.pop(1)

	print(cars)

def array8():
	cars = ["Ford", "Volvo", "BMW"]

	cars.remove("Volvo")

	print(cars)

def finalrun():
	print("adds 10 to the number passed in as an argument")
	lambda1()
	print()

	print("multiplies argument a with argument b")
	lambda2()
	print()

	print("sums argument a, b, and c")
	lambda3()
	print()

	print("array")
	array1()
	print()
	array2()
	print()
	array3()
	print()

	print("The length of an array")
	array4()
	print()

	print("Looping array elements")
	array5()
	print()

	print("Adding array elements")
	array6()
	print()

	print("Removing array elements")
	array7()
	print()
	array8()
	print()

finalrun()
