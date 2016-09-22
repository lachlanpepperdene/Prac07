import random
from Prac08.taxi import UnreliableCar, Taxi


def main():
    bad_car = UnreliableCar("Ford Fiesta", 100)
    if bad_car.does_drive(distance=30):
        print(bad_car)
    else:
        print("failed")

    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)

    print(taxi)
    print("Fare for this trip: ", taxi.get_fare())

    taxi.start_fare()

    taxi.drive(100)
    print(taxi)
    print("Fare for this trip: ", taxi.get_fare())

main()
