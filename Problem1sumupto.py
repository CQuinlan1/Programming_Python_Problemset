# *********************************
# Created by Catherine A. Celeste Quinlan
# For Programming Module 
# This programme asks the user to input a number and totals the numbers up to it and outputs the totals

# *********************************

i=input("Please enter your number : ")
number= int(i)
counter=0
while number > 0 :
    counter = number + counter
    number -= 1
print("The sum of all to values upto your number is :" ,counter)


















