def main():
    incomes = []
    numberOfMonths = int(input("How many number of Months? "))

    for month in range(1, numberOfMonths + 1):
        income = float(input("Enter income for month  {}: ".format(str(month))),)
        incomes.append(income)
        printReport(incomes)

def printReport(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()