#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
i = True
while i:
    integer = float(input("Enter a number: "))
    integer = integer / 2
    if integer != int(integer):
        print("That is not an even integer: ")
    else:
        i = False

print("That is an even integer")
 