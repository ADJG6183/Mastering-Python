import math

def plus():
    a = float(input("Choose the first value to add: "))
    print("###################")
    b = float(input("Choose the second value: "))
    result = a + b
    print(f"Result: {a} + {b} = {result}")
    return result

def minus():
    a = float(input("Choose the first value to subtract from: "))
    b = float(input("Choose the second value to subtract: "))
    result = a - b
    print(f"Result: {a} - {b} = {result}")
    return result

def times():
    a = float(input("Choose the first value to multiply: "))
    b = float(input("Choose the second value to multiply: "))
    result = a * b
    print(f"Result: {a} * {b} = {result}")
    return result

def split():
    a = float(input("Choose the dividend: "))
    b = float(input("Choose the divisor: "))
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    result = a / b
    print(f"Result: {a} / {b} = {result}")
    return result

def logar():
    a = float(input("Choose your value: "))
    print("---------------------------")
    b = float(input("Choose the base you would like to use: "))
    
    if a <= 0 or b <= 0 or b == 1:
        print("Error: Invalid values for logarithm!")
        return None
    
    result = math.log(a, b)
    print(f"Result: log base {b} of {a} = {result}")
    return result

def main():
    print("WELCOME TO MY CALCULATOR. YOU ARE HELPING MASTER PYTHON!!!!")
    print("Choose an option from those you see here:")

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. LOG")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    option = input("What will it be??? ")

    if option == '1':
        plus()
    elif option == '2':
        minus()
    elif option == '3':
        times()
    elif option == '4':
        split()
    elif option == '5':
        logar()
    else:
        print("Invalid option! Please choose 1-5.")

main()


