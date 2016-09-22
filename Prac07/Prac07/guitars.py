from Prac07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    jtv = Guitar("Line 6 JTV-59", 2010, 1512.9)
    guitars = [gibson, jtv]

    print("These are my guitars:")
    i = 0
    for guitar in guitars:
        i += 1
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print("Guitar {}: {:>18} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
main()