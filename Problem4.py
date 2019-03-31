# **********************************
# Created by Catherine Ann Celeste Quinlan
# Programming Course
# This program will ask the user to input any positive integer and outputs the successive values of the calculation.
#At each step it will calculate the next value by taking the current value, and if even will divide by 2 . If odd will multiply by 3 and add 1.
# PROBLEM 4
# ***********************************

Selectednumber=input ("Please enter a positive integer number  :  " )
number =int(Selectednumber)

if(number > 0):
    print("User number is positive ", Selectednumber)
    if (number == 1):
        print("Please pick a bigger number than 1 to run program")
    
else: 
    print ("your number is negative")
while (number > 0) and (number!=1):
    if number % 2 == 0 :
        number= number / 2
else:
    number = (number *3) +1

