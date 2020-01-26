number1 = input("Enter the first number: ")
if not number1.isdigit():
    number1 = input("Invalid input 1 ")

number2 = input("Enter the second number: ")
if not number2.isdigit():
    number2 = input("Invalid input 2 ")    


operation = input("Choose the operation (+, -, /, *): ")

number1 = int(number1)
number2 = int(number2)

if operation == "+":
    answer = number1+number2
elif operation == "-":
    answer = number1-number2
elif operation == "*":
    answer = number1*number2
elif operation == "/":
    answer = number1/number2

print("the answeris %s" % (answer))