# *********************************
# Created by Catherine A. Celeste Quinlan
# For Programming Module Data Analytics 
# This programme asks the user to input a number and totals the numbers up to it and outputs the total

# *********************************

i=input("Please enter your number : ")  # Reading number from keyboard
number= int(i)                          # Converting string to integer and store as new integer value

counter=0                               # Sum value
while number > 0 :                      # Start loop from selected number to > 0

    counter = number + counter          # Adding values to the total
    number -= 1                         # Decreasing my counter by 1 in each go
print("The sum of all to values upto your number is :" ,counter) # Print message and give a result total


















