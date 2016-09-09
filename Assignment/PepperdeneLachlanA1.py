import csv
import operator


def main():
    open_list = open_csv_list()
    input_value = start_menu(open_list)

    while input_value != 'Q':
        if input_value == "R":
            required_item(open_list)

        elif input_value == "C":
            completed_item(open_list)

        elif input_value == "M":
            marked_item(open_list)

        elif input_value == "A":
            add_item(open_list)

        else:
            print("Invalid input; input a valid letter from the list")

        print_menu()
        input_value = input_letter()

    quit_list(open_list)


def quit_list(open_list):
    with open('items.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(open_list)


def add_item(open_list):
    add_item_list = []
    priority_list = [1, 2, 3]
    while True:
        try:
            input_name = str(input("Enter the name for the item: "))
            if input_name == "":
                print("Cannot leave blank.")
            else:
                break
        except ValueError:
            print("Invalid character; Enter a valid number.")
    add_item_list.append(input_name)
    while True:
        try:
            input_price = float(input("Enter the item's price: "))
            if input_price < 0:
                print("Price must be greater than $0")
            else:
                break
        except ValueError:
            print("Invalid input; Enter a valid number.")
    add_item_list.append(input_price)
    while True:
        try:
            input_priority = int(input("Enter the item's priority: "))
            if input_priority in priority_list:
                break
            else:
                print("Priority must be; 1, 2 or 3.")
        except ValueError:
            print("Invalid input; Enter a valid number.")
    add_item_list.append(input_priority)
    add_item_list.append('r')

    print("{}, {} (priority {}) added to shopping list.".format(input_name, input_price, input_priority))

    open_list.append(add_item_list)


def marked_item(open_list):
    i = -1
    sum_cost = 0
    required_list = []
    for row in open_list:
        if "r" in row:
            i += 1
            required_list.append(row)
            print("{}. {:15} ${:6} ({})".format(i, row[0], row[1], row[2]))
            row[1] = float(row[1])
            sum_cost += row[1]
    print("Total expected price for {} item(s): $ {}".format(i, sum_cost))
    if not required_list:
        print("All item's marked")
    else:
        while True:
            try:
                change_item = int(input("Enter the number of an item to mark as completed: "))
                if change_item >= len(required_list) or change_item < 0:
                    print("Invalid number; Please choose number between 0 and {}".format(len(required_list)))
                    change_item = int(input("Enter the number of an item to mark as completed: "))
                else:
                    break
            except ValueError:
                print("Invalid character; Enter a valid number.")

        required_list[change_item][3] = 'c'
        print(required_list[change_item][0], "has been marked.")


def required_item(open_list):
    print("Required items:")
    open_list.sort(key=operator.itemgetter(2))
    count_row = 0
    sum_cost = 0
    for row in open_list:
        if "r" in row:
            print("{}. {:18} ${:6} ({})".format(count_row, row[0], row[1], row[2]))
            count_row += 1
            row[1] = float(row[1])
            sum_cost += row[1]
    if "r" not in row:
        print("No required items \n")
    else:
        print("Total expected price for {} item(s): $ {} \n".format(count_row, sum_cost))


def completed_item(open_list):
    open_list.sort(key=operator.itemgetter(2))
    print("Completed items:")
    count_row = 0
    sum_cost = 0
    for row in open_list:
        if "c" in row:
            print("{}. {:18} ${:6} ({})".format(count_row, row[0], row[1], row[2]))
            count_row += 1
            row[2] = float(row[2])
            sum_cost += row[1]
    if "r" in row == len(open_list):
        print("No completed items \n")
    else:
        print("Total expected price for {} item(s): $ {} \n".format(count_row, sum_cost))


def start_menu(open_list):
    print("Welcome to Shopping List 1.0 by Lachlan Pepperdene")
    print("{} items loaded from {} \n".format(len(open_list), "items.csv"))
    print_menu()
    input_value = (input("Enter a letter: "))
    input_value = input_value.upper()
    return input_value


def print_menu():
    print(
        "Menu: \n" + "R - List required items \n" + "C - List completed items \n" + "A - Add new item \n" + "M - Mark an item as completed \n" + "Q - Quit")


def input_letter():
    input_value = (input("Enter a letter: "))
    input_value = input_value.upper()
    return input_value


def open_csv_list():
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
