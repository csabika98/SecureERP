import random
from model.crm import crm
from view import terminal as view



def list_customers():
    data = open("model/crm/crm.csv")
    mylist = str(data)
    mylist = data.read()
    output = "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in mylist.split("\n") if item), 1))
    print(output)


def add_customer():
    id = random.randint(0,100)
    print(id)
    whats_your_name = input("What's your name? ")
    whats_your_email = input("What's your email? ")
    whats_your_name = whats_your_name + ";"
    whats_your_email = whats_your_email + ";"
    if input("You are subscribed ? 0.yes/1.no ") == "0":
        print("Thanks for subscribing!")
        with open("model/crm/crmsubscribed.csv", "a+") as sub_only:
            sub_only.read()
            sub_only.write(whats_your_name)
            sub_only.write(whats_your_email)
            sub_only.write(str(id))
            sub_only.write("\n")
    else:
        with open("model/crm/crm.csv", "a+" ) as import_file:
            import_file.write(whats_your_name)
            import_file.write(whats_your_email)
            import_file.write(str(id))
            import_file.write("\n")
    



def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    data = open("model/crm/crm.csv")
    mylist = str(data)
    mylist = data.read()
    output = "\n".join(
    "{}\t{}".format(line_number, line)
    for line_number, line in enumerate(
        (item for item in mylist.split("\n") if item), 1))
    print(output)
    ask_which_customer_want_to_del = input("Please type which customer do you want to delete? please type linenumber (1-99)" )
    linenum = int(ask_which_customer_want_to_del)
    with open("model/crm/crm.csv", "r+") as f:
        lines = f.readlines()
        del lines[linenum-1]  
        f.seek(0)
        f.truncate()
        f.writelines(lines)
        f.close()


def get_subscribed_emails():
     with open("model/crm/crmsubscribed.csv", "r") as customer_list:
            i = customer_list.read()
            empty_list = []
            empty_list.append(i)
            removed = empty_list.pop()[7:23]   
            print(removed)



def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
