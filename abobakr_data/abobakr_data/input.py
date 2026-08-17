
def input_float(message:str) -> float:
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            continue


def input_int(message:str) -> int:
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            continue
            
def input_string(message:str) -> str:
    input_string = input(message)
    while input_string.strip() == "" or input_string.isdigit():
        input_string = input(message)
    return input_string

def print_line(number:int) -> None:
    print("=" * number)

def tuple_python(list_tuple):
    new_list = ()
    for x in list_tuple:
        new_list += (x,)
    return new_list


def zip_python_list_list(list_zip):
    smallest= len(list_zip[0])
    for x in list_zip:
        if len(x) < smallest:
            smallest = len(x)

    new_list = [ (n[i] for n in list_zip) for i in range(smallest)]
    return new_list


average = lambda numbers: sum(numbers) / len(numbers)
