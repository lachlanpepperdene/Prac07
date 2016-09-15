def get_number(number):
    if number > 10 and < 50:
        true
get_number()

def main():
    value = (input("Enter character: "))
    print("The ASCII code for", value, "is", ord(value), )

    number = int(input("Enter number between 10 and 50: "))
    while get_number():
        print("The character for", number, "is", chr(number))
    else:
        print("Invalid Number")
main()


# Enter  a  character:g
# The  ASCII  code  for  g  is  103
# Enter  a  number  between  33  and  127: 100
# The  character  for  100  is  d

