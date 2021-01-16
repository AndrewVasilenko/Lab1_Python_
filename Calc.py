from sys import exit


def getNum():
	while True:
			try:
				num = int(input("Запишіть число: "))
				return num
			except:
				print("Хибне число, повторіть")


def getOperation():
	while True:
		try:
			operation = input("Впишіть операцію: ")
			if operation in ("+", "-", "*", "/", "%", "//"):
				return operation
		except:
			print("Хибна операція, повторіть")


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
		print("Не можна ділити на нуль")
		exit()
	result = num1 / num2
elif operation == "%":
	result = num1 % num2
else:
	result = num1 // num2

print(f"{num1} {operation} {num2} = {result}")
