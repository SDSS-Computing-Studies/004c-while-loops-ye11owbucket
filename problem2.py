#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
You may need to use the:
print( variable , end='') option to print on one line
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
import math

while True:
    num1 = str(input("Enter number: "))
    num2 = num1 * num1
    num3 = num1 * num2
    num4 = num1 * num3
    num5 = num1 * num4
    num6 = num1 * num5
    num7 = num1 * num6
    num8 = num1 * num7
    num9 = num1 * num8
    num10 = num1 * num9
    num11 = num1 * num10
    num12 = num1 * num11
    
    print(num1 , num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12) 
    break
    