SUPPORTED_OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b
}


def parse_input(input_string: str) -> float:
    input_tokens = input_string.split(" ")
    first_number = int(input_tokens[0])
    second_number = int(input_tokens[2])
    operation = input_tokens[1]
    return calculate(first_number, second_number, operation)


def calculate(a: int, b: int, operation: str) -> float:
    if operation not in SUPPORTED_OPERATIONS:
        raise ValueError(f'Unsupported operation - {operation}')

    function = SUPPORTED_OPERATIONS[operation]
    return function(a, b)


if __name__ == '__main__':
    print("Welcome to integer calculator!")
    while True:
        print("Input a string in format: 'int number' 'operation' 'int number' or -1 to exit")
        input_string = input()
        if input_string == "-1":
            break

        result = parse_input(input_string)
        print(f'Result: {result}')
