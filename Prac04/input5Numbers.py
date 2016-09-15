def main():
    numbers = []
    for i in range(0, 5, 1):
        numbValue = int(input("Enter a numbers: "))
        numbers.append(numbValue)

    print(numbers)
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average number is", (sum(numbers) / len(numbers)))

main()