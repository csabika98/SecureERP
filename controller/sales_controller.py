import random
import string
from model.sales import sales
from view import terminal as view


def list_transactions():
    data = open("model/sales/sales.csv")
    mylist = str(data)
    mylist = data.read()
    header ="Sr.no.  ID              CUSTOMER(ID)     PRODUCT            PRICE            DATE  \n"
    mylist = mylist.replace(";", "      ")
    mylist = mylist.center(0)
    output = header + "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in mylist.split("\n") if item), 1))
    print(output)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



def add_transaction():
    random1 = get_random_string(10)
    random2 = get_random_string(11)
    product = input("What's the product name? ")
    price = input("How much does it cost? ")
    date =input("When was the transaction made? ")
    
    product += ";"
    date += ";"
    random1 += ";"
    random2 += ";"
    price += ";"
    
    with open("model/sales/sales.csv", "a" ) as import_file:
        import_file.write(random1)
        import_file.write(random2)
        import_file.write(product)
        import_file.write(price)
        import_file.write(date)
        import_file.write("\n")

def update_transaction():
    data = open("model/sales/sales.csv")
    get_id_from_here = str(data)
    get_id_from_here = data.read()
    header ="Sr.no.  ID           CUSTOMER(ID)      PRODUCT     PRICE      DATE  \n"
    get_id_from_here = get_id_from_here.replace(";", "   ")
    output = header + "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in get_id_from_here.split("\n") if item), 0))
    print(output)
    with open("model/sales/sales.csv", "r+") as f:
        old_product = input("Type your old product: ")
        new_product = input("Type your new product: ")
        old_price = input("Type your old price: ")
        new_price = input("Type your new price: ")
        old_date = input("Type your old date:")
        new_date = input("Type your new date:")
        string = f.read()
        string = string.replace(old_product, new_product)
        string = string.replace(old_price, new_price)
        string = string.replace(old_date, new_date)
        f.truncate(0)
        f.seek(0)
        f.write(string)


def delete_transaction():
    data = open("model/sales/sales.csv")
    get_id_from_here = str(data)
    get_id_from_here = data.read()
    header ="Sr.no.  ID           CUSTOMER(ID)      PRODUCT     PRICE      DATE  \n"
    get_id_from_here = get_id_from_here.replace(";", "   ")
    output = header + "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in get_id_from_here.split("\n") if item), 0))
    print(output)
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
