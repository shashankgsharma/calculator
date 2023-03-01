from os import system
from ascii_art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub, 
    "*": mul,
    "/": div
}

def calculate():
    print(logo)
    num1 = float(input("Number 1: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while(should_continue):
        operator = input("Select operator: ")
        num2 = float(input("Number 2: "))

        calc_function = operations[operator]
        result = calc_function(num1, num2)

        print(f"{num1} {operator} {num2} = {result}") 

        answer = input(f"Type 'y' for continue calculating on {result} or 'n' to start a new calculation: ")
        if answer == 'y':
            num1 = result
        elif answer == 'n':
            should_continue = False
            system('clear')
            calculate()     #recursion  

calculate()