from os import system
from ascii_art import logo
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Not defined!"
    return n1 / n2

go_same = False
flag = True

while(flag): 
    if go_same:
        num1 = result
    else:
        print(logo)
        num1 = float(input("Enter first number: "))
    operators = {
                    "+": add, 
                    "-": sub, 
                    "*": mul, 
                    "/": div, 
                }
    for symbol in operators:
        print(symbol)
    opr = input("Choose an operator: ")
    num2 = float(input("Enter second number: "))
    function = operators[opr]
    if num2 == 0 and opr == "/":
        print(f"{num1} / 0 = {div(num1, 0)}")
        go_same = False
    else:
        result = function(num1, num2)
        print(f"{num1} {opr} {num2} = {result}")

        wrong_ans = True
        while(wrong_ans):
            ans = input(f"Type 'y' to continue calculation with {result}, 'n' to start new calculation, 'e' to end the calculator: ").lower()
            if ans == "y":
                go_same = True
                wrong_ans = False
            elif ans == "n":
                go_same = False
                wrong_ans = False
                system('clear')
            elif ans == "e":
                wrong_ans = False
                flag = False
                system('clear')
                print("Goodbye!")
            else:
                print("Wrong choice! Answer only from the given choice of words.")
            
