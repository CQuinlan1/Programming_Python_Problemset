# ******************************
# Created by Catherine Ann celeste Quinlan
# Programming Course
# This program will output today's date and time in format ' Monday , January 10th at 1:15pm
# Problem8 Date line 
# ******************************



from datetime import datetime

now = datetime.now() # current date and time


modified_date_time = now.strftime("%A, %B %d""th " "%Y at ""%I"":%m%p")  # Found using http://strftime.org/
print("date and time:",modified_date_time)


