try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")

# 1. When will a ValueError occur?
# When the numerator and/or denominators are not valid numbers,

# 2. When will a ZeroDivisionError occur?
# When a user enters 0 as the dominator.

# 3. Could  you  change  the  code to avoid the  possibility of a ZeroDivisionError?
# Yes, by entering an errorchecker that does not allow a user to enter a 0.
#





# I will not move the goal after the game has started.
# Sincerely, Lindsay