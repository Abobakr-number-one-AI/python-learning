from abobakr_data import get_string
from sys import exit

def main():
    to_do_list = []
    start_a_program_get_string = get_string_any_word()
    while start_a_program_get_string.lower().strip() in ["add", "view", "delete", "end task", "find task number", "count", "sort", "reverse", "stop"]:
        match start_a_program_get_string.lower().strip():
        
            case "add":
                task = get_string("what task would you like to add?: ")
                print("the task added")
                to_do_list.append(task)
                start_a_program_get_string = error_message("the task appended")
            case "view":
                if len(to_do_list) == 0:
                    start_a_program_get_string = error_message("No tasks.")
                else: 
                    print("your tasks are:")
                    for task in to_do_list:
                        print(task)
                    start_a_program_get_string = get_string_any_word()

            case "delete":
                delete_task = get_string("what task would you like to delete?: ")
                if delete_task in to_do_list:
                    to_do_list.remove(delete_task)
                    start_a_program_get_string = error_message("the task deleteed")
            case "end task":
                end_task = get_string("what task would you like to end?: ")
                if end_task in to_do_list:
                    number_count = to_do_list.index(end_task)
                    to_do_list.pop(number_count)
                    print("the task end and deleted")
                    start_a_program_get_string = get_string_any_word()

                else:
                   start_a_program_get_string = error_message()
            case "find task number" :
                select_task = get_string("what is it task: ")
                if select_task in to_do_list:
                    select_task_number = to_do_list.index(select_task) + 1
                    print(f"task number is {select_task_number}")
                    start_a_program_get_string = get_string_any_word()
                else:
                   start_a_program_get_string = error_message()
            case "count":
                task_count = get_string("what is it task: ")
                count_task_number = to_do_list.count(task_count)
                print(f"count is {count_task_number}")
                start_a_program_get_string = get_string_any_word()
            case "sort" :
                if to_do_list:
                    while True:
                        select_task_sort = get_string("what`s sort working (len task or letters): ")
                        match select_task_sort :
                            case "len task":
                                to_do_list.sort(key=len)
                                print(to_do_list)
                                break
                            case "letters":
                                to_do_list.sort()
                                print(to_do_list)
                                break
                            case _:
                                continue
                    
                else:
                    start_a_program_get_string = error_message("i do not find task" , False)
                start_a_program_get_string = get_string_any_word()
            case "reverse":
                if to_do_list:
                    to_do_list.reverse()
                    print(to_do_list)
                    start_a_program_get_string = get_string_any_word()
                else:
                    start_a_program_get_string = error_message("i do not find task" , False)          
                
            
            
            case "stop":
                sure = get_string("are you sure to stop this program (Yes/No): ")
                while sure.lower().strip() not in  ["yes","no"]:
                    sure = get_string("are you sure to stop this program (Yes/No): ")
                if sure.lower().strip() == "yes":
                    print("The program stopped")
                    exit()
                elif sure.lower().strip() == "no":
                    start_a_program_get_string = get_string_any_word()



def error_message(message: str = "the task not fond" , boolen_mesage: bool = True) -> str:
    if boolen_mesage:
        print(message)

    x = input("write any thing or never write thing  to continue or write stop: ")
    if x.lower().strip() == "stop":
        start_a_program_get_string = "stop"
    else:
        start_a_program_get_string = get_string_any_word()
    return start_a_program_get_string



def get_string_any_word():
    start_a_program_get_string = get_string("Would you like to add, view, delete, end task , find task number, count, sort, reverse, or stop? (add/view/delete/end task/find task number/count/sort/reverse/stop): ")
    while True:
        if start_a_program_get_string.lower().strip() not in ["add", "view", "delete", "end task", "find task number", "count", "sort", "reverse", "stop"]:
            start_a_program_get_string = get_string("Would you like to add, view, delete, end task, find task number, count, sort, reverse, or stop? (add/view/delete/end task/find task number/count/sort/reverse/stop): ")
            continue
        else:
            break

    return start_a_program_get_string


main()

