# ***********************
#  Created by Catherine Ann Celeste Quinlan
# This program takes a user input string and outputs every second word 
# 30 March 2019 
# Problem6
#************************

import re # Import module re to work with strings
user_sentence = input("Please enter your sentence  \n")  # String inputted from user

user_sentence = user_sentence.strip() # Removing training spaces beginning and end.
user_sentence = re.sub(' + ', ' ',user_sentence)
print ("Removing spaces in string ==>:", user_sentence.strip())


large = len(user_sentence.split())
senteced_splitted = user_sentence.split(" ")
words = user_sentence.split("\\")
print ("The number of words in this string is ," , large) 


i = 0

#for i in range(0,len(senteced_splitted)):                        # start of for loop to length
#    if i % 2 != 0:                                             #
#      print("Word in position ",i,"in the string is : ",senteced_splitted[i])                              #print splitted string 

while i <= len(senteced_splitted) :
      if i % 2 != 0:  
        print("Word in position ",i,"in the string is : ",senteced_splitted[i])  
      else :
          print("Word in position ",i)
      
      i += 1
