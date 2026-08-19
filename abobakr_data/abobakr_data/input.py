digit_values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def calculate_length(items):
    count = 0

    for item in items:
        count += 1

    return count


def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def generate_range(number):
    result = []
    current_number = 0

    while current_number != number:
        result += [current_number]
        current_number += 1

    return result


def generate_range_two(start, stop):
    result = []
    current_number = start

    while current_number != stop:
        result += [current_number]
        current_number += 1

    return result


def strip_string(text):
    while text != "" and text[0] == " ":
        text = text[1:]

    while text != "" and text[calculate_length(text) - 1] == " ":
        text = text[:calculate_length(text) - 1]

    return text


def remove_spaces(text):
    while " " in text:
        for index in generate_range(calculate_length(text)):
            if text[index] == " ":
                text = text[:index] + text[index + 1:]
                break

    return text


def reverse_python(items):
    result = []
    length = calculate_length(items)

    for index in generate_range(length):
        result += [items[length - 1 - index]]

    return result


def is_digit(number):
    number = remove_spaces(number)

    if number == "":
        return False

    start_index = 0

    if number[0] == "-":
        if calculate_length(number) == 1:
            return False

        start_index = 1

    for index in generate_range_two(
        start_index,
        calculate_length(number)
    ):
        if number[index] not in digit_values:
            return False

    return True


def int_python(number):
    number = remove_spaces(number)

    if not is_digit(number):
        return ""

    is_negative = False
    digits = []

    if number[0] == "-":
        is_negative = True
        number = number[1:]

    for character in number:
        digits += [digit_values[character]]

    result = 0

    for digit in digits:
        result = result * 10 + digit

    if is_negative:
        return -result

    return result


def float_python(number):
    number = remove_spaces(number)

    is_negative = False

    if number == "":
        return ""

    if number[0] == "-":
        is_negative = True
        number = number[1:]

    dot_index = -1

    for index in generate_range(calculate_length(number)):
        if number[index] == ".":
            dot_index = index
            break

    if dot_index == -1:
        return ""

    integer_part_text = number[:dot_index]
    decimal_part_text = number[dot_index + 1:]

    if integer_part_text == "":
        integer_part = 0
    elif is_digit(integer_part_text):
        integer_part = int_python(integer_part_text)
    else:
        return ""

    if decimal_part_text == "" or not is_digit(decimal_part_text):
        return ""

    decimal_digits = int_python(decimal_part_text)

    decimal_length = calculate_length(decimal_part_text)

    denominator = 1

    for index in generate_range(decimal_length):
        denominator = denominator * 10

    decimal_part = decimal_digits / denominator

    result = integer_part + decimal_part

    if is_negative:
        return -result

    return result


def input_int(message: str) -> int:
    while True:
        user_input = input(message)
        number = int_python(user_input)

        if number != "":
            return number


def input_float(message: str) -> float:
    while True:
        user_input = input(message)
        number = float_python(user_input)

        if number != "":
            return number


def input_string(message: str) -> str:
    user_input = input(message)

    while strip_string(user_input) == "" or is_digit(user_input):
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


def find_smallest_length(sequences):
    length = calculate_length(sequences[0])

    for sequence in sequences:
        sequence_length = calculate_length(sequence)

        if sequence_length < length:
            length = sequence_length

    return length


def zip_to_list_of_tuples(sequences):
    length = find_smallest_length(sequences)

    result = [
        convert_list_to_tuple(
            [sequence[index] for sequence in sequences]
        )
        for index in generate_range(length)
    ]

    return result


def zip_to_set_of_tuples(sequences):
    length = find_smallest_length(sequences)

    result = {
        convert_list_to_tuple(
            [sequence[index] for sequence in sequences]
        )
        for index in generate_range(length)
    }

    return result


def calculate_average(numbers):
    return calculate_sum(numbers) / calculate_length(numbers)