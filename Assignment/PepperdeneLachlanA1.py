import csv
import operator


def main():
    ['R', 'C', 'A', 'M', 'Q']
    open_list = openCSVList()
    input_value = startUpMenu(open_list)

    while input_value != 'Q':
        if input_value == "R":
            required(open_list)

        elif input_value == "C":
            completed(open_list)

        elif input_value == "M":
            marked(open_list)

        elif input_value == "A":
            order_row = 0
            count_row = 0
            sum_cost = 0

            while True:
                try:
                    input_name = input("Enter the number of an item to mark as completed: ")
                    if input_name != "" or input_name !=" ":
                        print("Invalid number; Please choose number between 0 and {}".format(len(open_list)))
                        change_item = int(input("Enter the number of an item to mark as completed: "))
                    else:
                        print
                except ValueError:
                    print("That was not a valid name.")
            # if addNewItem == " ":
            #     print("Wrong")
            # elif addNewItem == "":
            #     print("Right")
            for row in open_list:
                if "a" in row:
                    print(order_row, row[0], "$", row[1], row[2])
                    order_row += 1
                    count_row += 1
                    row[1] = float(row[1])
                    sum_cost += row[1]

        else:
            print("Invalid input; input a valid letter from the list")

        printMenu()
        input_value = inputLetter()


def marked(open_list):
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
    while True:
        try:
            change_item = int(input("Enter the number of an item to mark as completed: "))
            if change_item >= len(required_list) or change_item < 0:
                print("Invalid number; Please choose number between 0 and {}".format(len(open_list)))
                change_item = int(input("Enter the number of an item to mark as completed: "))
            else:
                break
        except ValueError:
            print("Invalid character; Enter a valid number.")

    required_list[change_item][3] = 'c'
    print(required_list[change_item][0], "has been marked.")


    # print("Items to be marked:")
    # order_row = 0
    # count_row = 0
    # sum_cost = 0
    # for row in open_list:
    #     if "r" in row:
    #         print("{}. {:18} ${:6} ({})".format(order_row, row[0], row[1], row[2]))
    #         order_row += 1
    #         count_row += 1
    #         row[1] = float(row[1])
    #         sum_cost += row[1]
    # if sum_cost == 0:
    #     print("No unmarked items. \n")
    # else:
    #     print("Total expected price for {} item(s): $ {}".format(count_row, sum_cost))
    # while True:
    #     try:
    #         change_item = int(input("Enter the number of an item to mark as completed: "))
    #         break
    #     except ValueError:
    #         print("Invalid character; Enter a valid number.")


def required(open_list):
    print("Required items:")
    open_list.sort(key=operator.itemgetter(2))
    order_row = 0
    count_row = 0
    sum_cost = 0
    for row in open_list:
        if "r" in row:
            print("{}. {:18} ${:6} ({})".format(order_row, row[0], row[1], row[2]))
            order_row += 1
            count_row += 1
            row[1] = float(row[1])
            sum_cost += row[1]
    if "r" not in row:
        print("No required items \n")
    else:
        print("Total expected price for {} item(s): $ {} \n".format(count_row, sum_cost))


def completed(open_list):
    open_list.sort(key=operator.itemgetter(2))
    print("Completed items:")
    order_row = 0
    count_row = 0
    sum_cost = 0
    for row in open_list:
        if "c" in row:
            print("{}. {:18} ${:6} ({})".format(order_row, row[0], row[1], row[2]))
            order_row += 1
            count_row += 1
            row[2] = float(row[2])
            sum_cost += row[1]
    if "c" not in row:
        print("No completed items \n")
    else:
        print("Total expected price for {} item(s): $ {} \n".format(count_row, sum_cost))


def startUpMenu(open_list):
    count_row = sum(1 for row in open_list)
    print("Welcome to Shopping List 1.0 by Lachlan Pepperdene")
    print((count_row), "items loaded from {}".format(open_list))
    printMenu()
    input_value = (input("Enter a letter: "))
    input_value = input_value.upper()
    return input_value


def printMenu():
    print(
        "Menu: \n" + "R - List required items \n" + "C - List completed items \n" + "A - Add new item \n" + "M - Mark an item as completed \n" + "Q - Quit")


def inputLetter():
    input_value = (input("Enter a letter: "))
    input_value = input_value.upper()
    return input_value


def openCSVList():
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
