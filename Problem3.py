# Problem 3########
# Catherine A Celeste Quinlan ######
# This program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.
# 16/03/19
print('start here')                     # initial number used
initialnumber = 1000                    # initial number used
finalnumber = 10000                     # final number used
counter = initialnumber


print("Initial Number :", initialnumber)         # Asking for values for Front end value

print ("Final Number :", finalnumber)             # Asking for values for end values
print("Counter :",counter)
while counter <= finalnumber :                   # Start loop from Intial to Final
    if counter%6 == 0 and counter%12 != 0:     # Checking for values divisable by 6 Not divisable by 12
        print (counter)
    counter += 1                                # Incrementing counter with each loop
    