import random
from Prac08.taxi import UnreliableCar, Taxi


def main():
#     bad_car = UnreliableCar("Ford Fiesta", 100)
#     if bad_car.does_drive(distance=30):
#         print(bad_car)
#     else:
#         print("failed")
#
#     taxi = Taxi("Prius 1", 100)
#     taxi.drive(40)
#
#     print(taxi)
#     print("Fare for this trip: ", taxi.get_fare())
#
#     taxi.start_fare()
#
#     taxi.drive(100)
#     print(taxi)
#     print("Fare for this trip: ", taxi.get_fare())
#
#     taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
#              SilverServiceTaxi("Hummer", 200, 4)]
#     bill = [0]

    def menu():
        menuOptions = ['q', 'c', 'd']
        print("Let's drive!")
        menu_choice = input("q)uit, c)hoose taxi, d)rive")
        while menu_choice not in menuOptions:
            print("incorrect answer try again")
            menu_choice = input("q)uit, c)hoose taxi, d)rive")
        return menu_choice


    def run_taxi_choice(taxis, bill):
        x = 0
        print("Taxis available: ")
        for row in taxis:
            print(x, "-", taxis[x])
            x += 1
        taxi_choice = int(input("Choose taxi:"))
        bill[0] += 10
        print("Bill to date: ${:.2f}".format(bill[0]))
        return taxi_choice, bill


    def run_drive(taxis, bill):
        distance = int(input("Drive how far? "))
        # print("Your Prius trip cost you ${:.2f}".format())

        print(taxis[taxi_choice[0]].get_fare)

        taxis[taxi_choice[0]].drive(distance)
        print(taxis[taxi_choice[0]])
        bill[0] += 52.50
        print("Bill to date: ${:.2f}".format(bill[0]))


    menu_choice = menu()

    while menu_choice != "q":
        if menu_choice == "c":
            taxi_choice = run_taxi_choice(taxis, bill)
            menu_choice = menu()
        elif menu_choice == "d":
            drive = run_drive(taxis, bill)
            menu_choice = menu()
    print("bye")
    print(bill)

main()

