value = (input("Enter character: "))
print("The ASCII code for",value, "is",ord(value),)

number = int(input("Enter number between 33 and 127: "))
while number > 32 and number < 128:
    print("The character for", number, "is", chr(number))
else:
    print("Invalid Number")


# Enter  a  character:g
# The  ASCII  code  for  g  is  103
# Enter  a  number  between  33  and  127: 100
# The  character  for  100  is  d

