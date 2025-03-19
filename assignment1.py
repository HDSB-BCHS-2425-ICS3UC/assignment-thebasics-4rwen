#Author: Arwen Murphy
#Date Modified: March 19th, 2025
#Description: 

import math

#The following are different types of variables.

integer=1
print("An example of a integer is: ",integer)
#An integer (int) is a whole number, that can be positive or negative, up to two billion.

floats=2.57
print("An example of a float is: ",floats)
#A float is any number with a decimal. 
#Doubles are similar to floats, but can only have one character after the decimal. (ex. 2.5)

char="A"
print("An example of a char is: ",char)
#A char is a single character. It can be a letter (ex. A), number (ex. 1), or symbol (ex. !).

booleans=True
print("An example of boolean is: ",booleans)
#Booleans can have two possible values, usually shown as "true" or "false".

str="Hello world!"
print("An example of a string is: ",str)
#A string (str) is multiple characters put together within quotation marks.

#The following are different types of math operations.

sum_add=2+2
print("An example of addition is 2 + 2 =",sum_add)
#addition

difference=10-5
print("An example of subtraction is 10 - 5 =",difference)
#subtraction

prod=3*3
print("An example of multiplication is 3 * 3 =",prod)
#multiplication

quot=8/2
print("An example of division is 8 / 2 =",quot)
#division (whole numbers)

quot_float=24.5/2
print("An example of division (with floats) is 24.5 / 2 =",quot_float)
#division (with decimals) 

nth_power=3**4
print("An example of an exponent is 3 ** 4 =",nth_power)
#power of...

square=math.sqrt(16)
print("An example of square root is 16sqrt =",square)
#square root

rem=24%5
print("An example of modulus is 24 % 5 =",rem)
#modulus

#The following finds the discriminant

a=int(input("Enter a then press enter:"))
b=int(input("Enter b then press enter:"))
c=int(input("Enter c then press enter:"))

print("The discriminant of",a,",",b,", and",c,"is",b**2-4*a*c)

#Find the volume of a cube

A=int(input("Enter the length of one edge: "))
print("The area of the cube is",A**3,".")
