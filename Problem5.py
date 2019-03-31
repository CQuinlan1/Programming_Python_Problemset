# *****************************
# Created by Catherine Ann Celeste Quinlan
# This program will take a positive integer and say if it is a prime number
# QUESTION 5
# ***********************


Selectednumber=input ("Please enter a positive integer number  :  " )
number =int(Selectednumber)


# If given number is greater than 1 
if number > 1: 
      
   # Iterate from 2 to number/2  
   for i in range(2, number//2): # Idea from https://www.geeksforgeeks.org/python-program-to-check-prime-number/        
       # If number is divisible by any number between  
       # 2 and number / 2, it is not prime  
       if (number % i) == 0: 
           print(number, "is not a prime number") 
           break
   else: 
       print(number, "is a prime number") 
  
else: 
   print(number, "is not a prime number") 
