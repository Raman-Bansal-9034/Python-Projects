from calculator_art import logo


# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Modulus
def modulus(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus
}


def calculator():
    print(logo)
    first_num = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation ")
        second_num = float(input("What's the next number?  "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_num, second_num)

        print(f"{first_num} {operation_symbol} {second_num} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation\n") == "y":
            first_num = answer
        else:
            should_continue = False
            calculator()


calculator()
