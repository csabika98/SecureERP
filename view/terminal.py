# colors
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGRAY = '\033[37m'
DARKGRAY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'

print("
                                                                                                                 
                                                                                                                 
        CCCCCCCCCCCCC   SSSSSSSSSSSSSSS                AAA               RRRRRRRRRRRRRRRRR   RRRRRRRRRRRRRRRRR   
     CCC::::::::::::C SS:::::::::::::::S              A:::A              R::::::::::::::::R  R::::::::::::::::R  
   CC:::::::::::::::CS:::::SSSSSS::::::S             A:::::A             R::::::RRRRRR:::::R R::::::RRRRRR:::::R 
  C:::::CCCCCCCC::::CS:::::S     SSSSSSS            A:::::::A            RR:::::R     R:::::RRR:::::R     R:::::R
 C:::::C       CCCCCCS:::::S                       A:::::::::A             R::::R     R:::::R  R::::R     R:::::R
C:::::C              S:::::S                      A:::::A:::::A            R::::R     R:::::R  R::::R     R:::::R
C:::::C               S::::SSSS                  A:::::A A:::::A           R::::RRRRRR:::::R   R::::RRRRRR:::::R 
C:::::C                SS::::::SSSSS            A:::::A   A:::::A          R:::::::::::::RR    R:::::::::::::RR  
C:::::C                  SSS::::::::SS         A:::::A     A:::::A         R::::RRRRRR:::::R   R::::RRRRRR:::::R 
C:::::C                     SSSSSS::::S       A:::::AAAAAAAAA:::::A        R::::R     R:::::R  R::::R     R:::::R
C:::::C                          S:::::S     A:::::::::::::::::::::A       R::::R     R:::::R  R::::R     R:::::R
 C:::::C       CCCCCC            S:::::S    A:::::AAAAAAAAAAAAA:::::A      R::::R     R:::::R  R::::R     R:::::R
  C:::::CCCCCCCC::::CSSSSSSS     S:::::S   A:::::A             A:::::A   RR:::::R     R:::::RRR:::::R     R:::::R
   CC:::::::::::::::CS::::::SSSSSS:::::S  A:::::A               A:::::A  R::::::R     R:::::RR::::::R     R:::::R
     CCC::::::::::::CS:::::::::::::::SS  A:::::A                 A:::::A R::::::R     R:::::RR::::::R     R:::::R
        CCCCCCCCCCCCC SSSSSSSSSSSSSSS   AAAAAAA                   AAAAAAARRRRRRRR     RRRRRRRRRRRRRRR     RRRRRRR
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
                                                                                                                 
")
print("
 _____  _____  _____  _   _ ______  _____   _____ ______ ______ 
/  ___||  ___|/  __ \| | | || ___ \|  ___| |  ___|| ___ \| ___ \
\ `--. | |__  | /  \/| | | || |_/ /| |__   | |__  | |_/ /| |_/ /
 `--. \|  __| | |    | | | ||    / |  __|  |  __| |    / |  __/ 
/\__/ /| |___ | \__/\| |_| || |\ \ | |___  | |___ | |\ \ | |    
\____/ \____/  \____/ \___/ \_| \_|\____/  \____/ \_| \_|\_|    
                                                                
                                                                
")

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    order_number = 0
    print(BOLD + '\n'*2 + title + RESET)
    for option in list_options:
        print(BOLD + "     (" + str(order_number) + ") ", option + RESET)
        order_number += 1
   


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(BLUE + "MESSAGE: " + message + RESET)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table, title_list):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    row_width = []
    for width in title_list:
        row_width.append(len(width))
    for line in range(0, len(table)):
        for index in range(0, len(table[line])):
            if len(table[line][index]) > row_width[index]:
                row_width[index] = len(table[line][index])

    table_lenght = 0
    for index in range(0, len(row_width)):
        row_width[index] += 2
        table_lenght += row_width[index]

    print(GREEN + "/" + "-" * (table_lenght+len(title_list)-1) + "\\" + RESET)

    for i in range(0, len(title_list)):
        temp = round((row_width[i] - len(title_list[i]))/2)
        print(GREEN + "|" + " " * temp + BOLD + title_list[i], end='')
        print(GREEN + " " * (row_width[i] - (temp + len(title_list[i]))), end='')
    print("|" + RESET)

    for line in range(0, len(table)):
        for width in row_width:
            print(GREEN + "|" + "-" * width, end='')
        print("|" + RESET)
        for index in range(0, len(table[line])):
            temp = round((row_width[index] - len(table[line][index]))/2)
            print(GREEN + "|" + " " * temp + BLUE + table[line][index], end='')
            print(GREEN + " " * (row_width[index]-temp-len(table[line][index])), end='')
        print("|" + RESET)

    print(GREEN + "\\" + "-" * (table_lenght+len(title_list)-1) + "/" + RESET)

    input(REVERSE + "Press enter to continue" + RESET)
    


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    inputs = get_inputs([CYAN + "Please enter a number: " + RESET], "")
    return inputs[0]



def get_inputs(labels, title):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    inputs = []
    print(CYAN + title + RESET)
    for label in labels:
        user_input = input(label)
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(RED + "ERROR:" + message + RESET)
