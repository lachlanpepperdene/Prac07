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
