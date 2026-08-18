def input_int(message: str) -> int:
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            continue


def input_float(message: str) -> float:
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            continue


def input_string(message: str) -> str:
    user_input = input(message)

    while user_input.strip() == "" or user_input.isdigit():
        user_input = input(message)

    return user_input


def print_separator(length: int) -> None:
    print("=" * length)


def convert_list_to_tuple(items):
    result = ()

    for item in items:
        result += (item,)

    return result


def set_union(first_set, second_set):
    return first_set | second_set


def set_intersection(first_set, second_set):
    return first_set & second_set


def set_difference(first_set, second_set):
    return first_set - second_set


def set_symmetric_difference(first_set, second_set):
    return first_set ^ second_set


def smallest_length(sequences):
    length = len(sequences[0])

    for sequence in sequences:
        if len(sequence) < length:
            length = len(sequence)

    return length


def zip_to_list_of_tuples(sequences):
    length = smallest_length(sequences)

    result = [
        convert_list_to_tuple([sequence[i] for sequence in sequences])
        for i in range(length)
    ]

    return result


def zip_to_set_of_tuples(sequences):
    length = smallest_length(sequences)

    result = {
        tuple(sequence[i] for sequence in sequences)
        for i in range(length)
    }

    return result



average = lambda numbers: sum(numbers) / len(numbers)