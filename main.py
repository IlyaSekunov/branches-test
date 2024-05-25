SUPPORTED_OPERATIONS = {
    "+": lambda a, b: a + b
}


def parse_input(input_string: str) -> float:
    first_number = int(input_string[0])
    second_number = int(input_string[2])
    operation = input_string[1]
    return calculate(first_number, second_number, operation)


def calculate(a: int, b: int, operation: str) -> float:
    if operation not in SUPPORTED_OPERATIONS:
        raise ValueError(f'Unsupported operation - {operation}')

    function = SUPPORTED_OPERATIONS[operation]
    return function(a, b)


if __name__ == '__main__':
    print()
