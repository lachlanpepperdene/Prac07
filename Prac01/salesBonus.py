sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        sales = sales * 1.1
    else:
        sales = sales * 1.15
    print("Result: {:.2f}".format(sales))
    sales = float(input("Enter sales: $"))
