from Prac07.car import Car


def main():
    bus = Car(180,"Bus")
    bus.drive(30)

    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(150, "Limo")
    limo.drive(50)
    limo.add_fuel(20)
    print(limo)

main()