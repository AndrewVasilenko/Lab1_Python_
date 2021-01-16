from sys import exit


def getNum():
	while True:
			try:
				num = int(input("Write number: "))
				return num
			except:
				print("Wrong number, try again")


def getOperation():
	while True:
		try:
			operation = input("Write operation: ")
			if operation in ("+", "-", "*", "/", "%", "//"):
				return operation
		except:
			print("Wrong operation, try again")


num1 = getNum()
num2 = getNum()
operation = getOperation()
result = 0

if operation == "+":
	result = num1 + num2
elif operation == "-":
	result = num1 - num2
elif operation == "*":
	result = num1 * num2
elif operation == "/":
	if num2 == 0:
		print("Cannot be divided by zero!")
		exit()
	result = num1 / num2
elif operation == "%":
	result = num1 % num2
else:
	result = num1 // num2

print(f"{num1} {operation} {num2} = {result}")