import csv
import operator


def main():  # The main function which contains all the project's code.
    open_list = open_csv_list()  # The main function calling the csv list from it's function.
    input_value = start_menu(open_list)  # The main function calling the input letter from the menu function.

    while input_value != 'Q':  # This while loop will always run until 'Q' is entered.
        if input_value == "R":  # Checking for 'R' from the input to run the 'required' function.
            required_item(open_list)

        elif input_value == "C":  # Checking for 'C' from the input to run the 'required' function.
            completed_item(open_list)

        elif input_value == "M":  # Checking for 'M' from the input to run the 'required' function.
            marked_item(open_list)

        elif input_value == "A":  # Checking for 'A' from the input to run the 'required' function.
            add_item(open_list)

        else:  # This else statement is an error checker so that if an incorrect letter is entered it will loop.
            print("Invalid input; input a valid letter from the list")

        print_menu()  # Calls for the print menu function so after each letter function is it prints again.
        input_value = input_letter()  # Makes the new input_value replace the old one.

    quit_list(open_list)  # Wait for the while loop to break then runs the 'quit' function.


def quit_list(open_list):  # A function that writes all data stored on the memory to the CSV.
    with open('items.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(open_list)
    print("{} items saved to items.csv".format(len(open_list)))
    print("Have a nice day :) \n")


""" # Pseudocode for the add_item function.
function add_item:
    new item list = blank list
    priority list = [1, 2, 3]

    get name from input
    if name is blank:
        print("Cannot be blank.")
    elif name is a integer:
        print("Must be a string of letters")
    else:
        print(name, "has been added")
        add name to new item list

    get price from input
    if price < 0:
        print("Must be greater than $0")
    elif price is not a float:
        print("Invalid price")
    else:
        print(price, "has been added")
        add price to new item list

    get priority from input
        if priority in priority list:
            print(priority "has been added")
            add priority to new item list
        elif priority is not an integer:
            print("Incorrect, Enter a number.")
        else:
            print("Priority must be 1, 2 or 3.")

    required = 'r'
    add require to new item list('r')

    print(input_name, input_price, input_priority, "added to shopping list")

    add new item list to list
"""


def add_item(open_list):  # A function that adds an item to a new list, then adds the new list to the original list.
    add_item_list = []
    priority_list = [1, 2, 3]
    while True:  # Error checking for a name that is entered that is blank name or numbers in the name.
        try:
            input_name = str(input("Enter the name for the item: \n>>> "))
            if input_name and input_name.strip():
                break
            else:
                print("Cannot leave blank.")
        except ValueError:
            print("Invalid character; Enter a valid number.")
    add_item_list.append(input_name)
    while True:  # Error checking for an entered price that is less than 0 or is not a number.
        try:
            input_price = float(input("Enter the item's price: \n>>> "))
            if input_price < 0:
                print("Price must be greater than $0")
            else:
                break
        except ValueError:
            print("Invalid input; Enter a valid number.")
    add_item_list.append(input_price)
    while True:  # Error checking for an entered priority that is not from the priority list or is not a number.
        try:
            input_priority = int(input("Enter the item's priority: \n>>> "))
            if input_priority in priority_list:
                break
            else:
                print("Priority must be; 1, 2 or 3.")
        except ValueError:
            print("Invalid input; Enter a valid number.")
    add_item_list.append(input_priority)
    add_item_list.append('r')  # Adds 'r' to list because all new items are required to be marked as completed manually.

    print("{}, ${} (priority {}) added to shopping list.".format(input_name, input_price, input_priority))

    open_list.append(add_item_list)  # Adds new item list to the original list after all values have been entered right.


def marked_item(open_list):  # A function that marks an item with an 'r' then changes it to a 'c' for completed.
    count_row = 0
    sum_cost = 0
    required_list = []  # Makes a new list for only the entities with 'r' for required.
    for row in open_list:  # Repeats the loop for how many rows there are in the list so all rows are checked.
        if "r" in row:
            required_list.append(row)
            print("{}. {:15} ${:6} ({})".format(count_row, row[0], row[1], row[2]))
            row[1] = float(row[1])
            sum_cost += row[1]
            count_row += 1
    print("Total expected price for {} item(s): $ {}".format(count_row, sum_cost))
    if not required_list:  # Checks if there are any required items or if all have been marked.
        print("All item's marked")
    else:
        while True:  # Error checking for an entered item number that it is a valid number for the range of items.
            try:
                change_item = int(input("Enter the number of an item to mark as completed: \n>>> "))
                if change_item >= len(required_list) or change_item < 0:
                    print("Invalid number; Please choose number between 0 and {}".format(len(required_list)))
                    change_item = int(input("Enter the number of an item to mark as completed: \n>>> "))
                else:
                    break
            except ValueError:
                print("Invalid character; Enter a valid number.")

        required_list[change_item][3] = 'c'  # Changes the 'r' value to a 'c' which removes it from the required_list.
        print(required_list[change_item][0], "has been marked.")


def completed_item(open_list):  # A function that checks for completed items and then prints them.
    open_list.sort(key=operator.itemgetter(2))  # Sorts the list by a selected row.
    print("Completed items:")
    count_row = 0
    sum_cost = 0
    for row in open_list:  # Repeats the loop for how many rows there are in the list so all rows are checked.
        if "c" in row:
            print("{}. {:18} ${:6} ({})".format(count_row, row[0], row[1], row[2]))
            count_row += 1
            row[2] = float(row[2])
            sum_cost += row[1]
    if "r" in row == len(open_list):  # Checks to see if any 'c' values are in rows otherwise there are none completed.
        print("No completed items \n")
    else:
        print("Total expected price for {} item(s): $ {} \n".format(count_row, sum_cost))


def required_item(open_list):  # A function that checks for required items and then prints them.
    print("Required items:")
    open_list.sort(key=operator.itemgetter(2))  # Sorts the list by a selected row.
    count_row = 0
    sum_cost = 0
    for row in open_list:  # Repeats the loop for how many rows there are in the list so all rows are checked.
        if "r" in row:
            print("{}. {:18} ${:6} ({})".format(count_row, row[0], row[1], row[2]))
            count_row += 1
            row[1] = float(row[1])
            sum_cost += row[1]
    if "r" not in row:
        print("No required items \n")
    else:
        print("Total expected price for {} item(s): $ {} \n".format(count_row, sum_cost))


def start_menu(open_list):  # A function that prints the start up menu and is only used once.
    print("Welcome to Shopping List 1.0 by Lachlan Pepperdene")
    print("{} items loaded from {} \n".format(len(open_list), "items.csv"))
    print_menu()
    input_value = (input("Enter a letter: \n>>> "))
    input_value = input_value.upper()
    return input_value


def print_menu():  # A function designed to hold the print menu code so that it can be called from main.
    print(
        "Menu: \n" + "R - List required items \n" + "C - List completed items \n" + "A - Add new item \n" + "M - Mark an item as completed \n" + "Q - Quit")


def input_letter():  # A function that prompts the user to input a letter which is used in main in the while loop.
    input_value = (input("Enter a letter: \n>>> "))
    input_value = input_value.upper()
    return input_value


"""
function open_csv_list:
            open "items.csv" as fileIn for reading
            new list from "items.csv"
            for each row in list:
                 make item[1] a float
                 make item[2] an int
            close OPEN_CSV
            sort list by row[2]
            return list
"""


def open_csv_list():  # A function that opens the CSV, then creates a list with the CSV values and then closes the CSV.
    open_csv = open('items.csv')
    read_csv = csv.reader(open_csv)
    open_list = list(read_csv)
    for item in open_list:
        item[1] = float(item[1])
        item[2] = int(item[2])
    open_csv.close()
    open_list.sort(key=operator.itemgetter(2))
    return open_list


main()
