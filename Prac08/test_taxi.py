import random
from Prac08.taxi import Taxi, UnreliableCar, SilverServiceTaxi

bill = 0


def main():

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    def get_menu():
        menu_options = ['q','c','d']
        print("Let's drive!")
        choose_menu = input("q)uit, c)hoose taxi, d)rive: ")
        while choose_menu not in menu_options:
            print("incorrect answer try again")
            choose_menu = input("q)uit, c)hoose taxi, d)rive: ")
        return choose_menu

    def run_taxi_choice(taxis):
        counter = 0
        print("Taxis available: ")
        for row in taxis:
            print(counter, "-", taxis[counter])
            counter += 1
        input_taxi_choice = int(input("Choose taxi: "))
        return input_taxi_choice

    print("Bill to date: ${:.2f}".format(bill))

    def run_drive(taxis, bill):
        distance = int(input("Drive how far?: "))
        taxis[taxi_choice].drive(distance)
        print("Your {} trip will cost you {}".format(taxis[taxi_choice].name, Taxi.get_fare(taxis[taxi_choice])))

        print(taxis[taxi_choice])
        bill += Taxi.get_fare(taxis[taxi_choice])
        bill += 4.5
        print("Bill to date: ${:.2f}".format(bill))

    choose_menu = get_menu()

    while choose_menu != "q":
        if choose_menu == "c":
            taxi_choice = run_taxi_choice(taxis)
            choose_menu = get_menu()
        elif choose_menu == "d":
            drive = run_drive(taxis, bill)
            choose_menu = get_menu()
    print("Total trip cost: $",bill)
    print("Taxis are now: ")
    counter = 0
    for row in taxis:
        print(counter, "-", taxis[counter])
        counter += 1


main()

# def main():
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
# main()
