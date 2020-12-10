import random
import string
from model.hr import hr
from view import terminal as view


def list_employees():
    data = open("model/hr/hr.csv")
    mylist = str(data)
    mylist = data.read()
    header ="Sr.no.  ID             NAME     EMAIL              DATE OF BIRTH     DP       C\n"
    mylist = mylist.replace(";", "     ")
    output = header + "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in mylist.split("\n") if item), 1))
    print(output)
    

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



def add_employee():
    random1 = get_random_string(10)
    whats_your_name = input("What's your name? ")
    whats_your_email = input("What's your email? ")
    birth_date =input("When were you born? yyyy-mm-dd ")
    department = input("Please type what your department is: sales/production ")
    clearence_level = input("Type your clearence level: 0(lowest) 7(highest) ")
    whats_your_name = whats_your_name + ";"
    whats_your_email = whats_your_email + ";"
    birth_date = birth_date + ";"
    random1 = random1 + ";"
    department = department + ";"
    clearence_level = clearence_level + ";"

    with open("model/hr/hr.csv", "a" ) as import_file:
        import_file.write(str(random1))
        import_file.write(whats_your_name)
        import_file.write(whats_your_email)
        import_file.write(birth_date)
        import_file.write(department)
        import_file.write(clearence_level)
        import_file.write("\n")



def update_employee():
    view.print_error_message("Not implemented yet.")


def delete_employee():
    data = open("model/hr/hr.csv")
    mylist = str(data)
    mylist = data.read()
    output = "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in mylist.split("\n") if item), 1))
    print(output)
    ask_which_employee_want_to_del = input("Please type which employee do you want to delete? please type linenumber (1-99)" )
    linenum = int(ask_which_employee_want_to_del)
    with open("model/hr/hr.csv", "r+") as f:
        lines = f.readlines()
        del lines[linenum-1]  
        f.seek(0)
        f.truncate()
        f.writelines(lines)
        f.close()


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
            "List employees",
            "Add new employee",
            "Update employee",
            "Remove employee",
            "Oldest and youngest employees",
            "Employees average age",
            "Employees with birthdays in the next two weeks",
            "Employees with clearance level",
            "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
