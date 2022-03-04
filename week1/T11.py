num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Enter operator");
operation = input("Enter operation among +, -, *, / ")
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2 == 0:
        return 0
    else:
        return num1/num2
resultant = 0
if operation=='+':
    resultant = add(num1,num2)
    print(f"\nAddition Result = {resultant}")
elif operation=="-":
    resultant = subtract(num1,num2)
    print(f"\nSubtract Result = {resultant}")
elif operation=="*":
    resultant = multiplication(num1,num2)
    print(f"\nMultiplication Result = {resultant}")
elif operation=="/":
    resultant =division(num1,num2)
    print(f"\nDivision Result ={resultant}")
else:
    print("operation not supported");