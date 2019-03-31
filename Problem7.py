#**************************
# Created by Catherine Ann Celeste Quinlan
# This program will take a FLOATING POINT NUMBER as input and output its square root approximation.
# QUESTION 7
#*************************

import math


Selectednumber = input ("Please enter a positive floating number bigger than 0 : \n " )
try:
    val = float(Selectednumber)
    if(val > 0):
        print("Yes,input string is a float number.")
        root_square = round(math.sqrt(val),2)
        print("The Square root of this number , rounded to two decimal places is :", root_square)
    elif (val == 0):
        print("please enter a float number bigger than 0")
    else:
        print("User number is negative.")
except ValueError:
    print("That is not a floating number!")
