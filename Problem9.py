# =================================
# created by Celeste Quinlan.
# Course XXXX
# This program reads in a text ﬁle and outputs every second line. 
# The program should take the ﬁlename from an argument on the command line.
# QUESTION 9 
# =================================

import sys

#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , str(sys.argv))


filepath = sys.argv[1] #takes the name of a file 
print ("The file to read is : " ,filepath) # 
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       if cnt % 2 == 0 :   # when ther is no remainder , even number of lines
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
       cnt += 1