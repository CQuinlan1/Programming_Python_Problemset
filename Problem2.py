
 # *************************
 # Catherine Ann Celeste Quinlan
# Programming 2019 Data Analytics
# This program asks the user whether or not today is a day that begins with the letter T.
# Question 2
# *************************

import datetime                                                                      # Importing datatime Pythonhttps://stackoverflow.com/questions/34296860/how-do-you-get-the-time-and-date-in-python
now = datetime.datetime.now
weekday = datetime.datetime.today().strftime("%A")                                    # Taken from # Ian McLoughlin, 2018-02-01
# Is it Tuesday?
if datetime.datetime.today().weekday() == 1:
    print ("Yes! It is Tuesday")  
elif datetime.datetime.today() .weekday() == 3:
    print ("Yes! It is Thursday")                                                   # Printing if it is Tuesday 

else:
    print ("Unfortunately today does not start with T.""\n" "Today is :", weekday)   # prints out day that doesnt start with T