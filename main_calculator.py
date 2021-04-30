import calculatorArt


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# higher order function - function which takes a function - good for event listener
def final_calculate(n1, n2, func):
    return func(n1, n2)


result = final_calculate(2, 3, add)
print(result)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(calculatorArt.logo)

    num1 = float(input("What is the first number? "))

    for operation in operations:
        print(operation)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick one operation: ")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation") == 'y':
            num1 = answer
        else:
            should_continue = False
            print('\n' * 25)
            calculator()


calculator()