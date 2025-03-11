# Building a basic calculator
def calculator():
    first_num = float(input("Type the first number; "))
    second_num = float(input("Type the second number; "))
    sign = input("Give the operation (-, +, *, /); ")

    if sign == '-':
        result = first_num - second_num
        print(result)
    elif sign == "+":
        result = first_num + second_num
        print(result)
    elif sign == "*":
        result = first_num * second_num
        print(result)
    elif sign == "/":
        if second_num == 0:
            print("Invalid, second_num should not be zero")
        else:
            result = first_num / second_num
            print(result)
    else:
        print("Invalid operation")

calculator()