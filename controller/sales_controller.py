import random
import sys
from model.sales import sales
from view import terminal as view


def list_transactions():
    with open("model/sales/sales.csv", "r") as transaction_list:
        for line in transaction_list:
            strip_line = line.replace(";","  ",)
            print(strip_line)


def add_transaction():
    id = random.randint(0,100)
    print(id)
    whats_your_name = input("What's your name? ")
    whats_your_email = input("What's your email? ")
    you_are_subscribed =input("You are subscribed ? 1.   yes  0.  no ")
    whats_your_name = whats_your_name + ";"
    whats_your_email = whats_your_email + ";"
    you_are_subscribed = you_are_subscribed + ";"
    

    with open("model/sales/sales.csv", "a" ) as import_file:
        import_file.write(whats_your_name)
        import_file.write(whats_your_email)
        import_file.write(you_are_subscribed)
        import_file.write(str(id))
        import_file.write("\n")

def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    with open("model/sales/sales.csv", "r") as transaction_list:
        for line in transaction_list:
            strip_line = line.replace(";","  ",)
            print(strip_line)
    ask_which_transaction_want_to_del = input("Please type which transaction do you want to delete? please type linenumber (1-99)" )
    linenum = int(ask_which_transaction_want_to_del)
    with open("model/sales/sales.csv", "r+") as f:
        lines = f.readlines()
        del lines[linenum-1]  
        f.seek(0)
        f.truncate()
        f.writelines(lines)
        f.close()

def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
            "List transactions",
            "Add new transaction",
            "Update transaction",
            "Remove transaction",
            "Get the transaction that made the biggest revenue",
            "Get the product that made the biggest revenue altogether",
            "Count number of transactions between",
            "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
