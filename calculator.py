from abobakr_data import get_float, get_int


def binary_operations(operation):
    first_number = get_float("Enter the first number: ")
    second_number = get_float("Enter the second number: ")

    if operation in ["/", "%", "//"]:
        while second_number == 0:
            print("The program cannot perform this operation when the second number is 0.")
            stopping = input(
                "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
            )

            if stopping == "stop":
                return

            second_number = get_float("Enter the second number: ")

    if operation == "+":
        number = first_number + second_number
    elif operation == "-":
        number = first_number - second_number
    elif operation == "*":
        number = first_number * second_number
    elif operation == "/":
        number = first_number / second_number
    elif operation == "%":
        number = first_number % second_number
    elif operation == "//":
        number = first_number // second_number

    print(f"Result: {number}")


def power_operation():
    the_number = get_int("Enter the number: ")
    power = get_int("Enter the exponent: ")

    while the_number == 0 and power < 0:
        print(
            "The program cannot calculate 0 raised to a negative exponent."
        )

        stopping = input(
            "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
        )

        if stopping == "stop":
            return

        the_number = get_int("Enter the number: ")
        power = get_int("Enter the exponent: ")

    number = the_number ** power
    print(f"Result: {number}")


def square_root_operation():
    the_number = get_float("Enter the number: ")

    while the_number < 0:
        print("The number under the root cannot be less than 0.")

        stopping = input(
            "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
        )

        if stopping == "stop":
            return

        the_number = get_float("Enter the number: ")

    root = get_float("Enter the root: ")

    while root <= 0:
        print("The root must be greater than 0.")

        stopping = input(
            "If you want to stop the program, type 'stop'. Otherwise, press Enter: "
        )

        if stopping == "stop":
            return

        root = get_float("Enter the root: ")

    number = the_number ** (1 / root)
    print(f"Result: {number}")


def main():
    explain = [
        "+     : Addition",
        "-     : Subtraction",
        "*     : Multiplication",
        "/     : Division (may return a decimal number)",
        "//    : Floor division",
        "%     : Modulo (remainder)",
        "^     : Exponentiation (example: 2^3 = 8)",
        "sqrt  : Root (example: sqrt 25 = 5)",
    ]

    for operation in explain:
        print(operation)

    while True:
        operation = input(
            "Enter an operation (+, -, *, /, ^, %, //, sqrt): "
        )

        if operation in ["+", "-", "*", "/", "%", "//"]:
            binary_operations(operation)
        elif operation == "sqrt":
            square_root_operation()
        elif operation == "^":
            power_operation()
        elif operation == "stop":
            return
        else:
            continue


main()