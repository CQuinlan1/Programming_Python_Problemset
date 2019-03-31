#*************************
#Created by Catherine Ann Celeste Quinlan.
# This program display a plot of the functions x x squared and 2 to the power of x in the range [0,4]
# Problem10
# ***********************


from matplotlib import pyplot as plt
# x-axis values 
x = [0,1,2,3,4]   # Domain for x function
  
# Y-axis values 
y = [0,1,2,3,4]   # Range for x function
  
# Function to plot 
plt.plot(x,y) 
  
# function to show the plot 
plt.show() 


# x-axis values 
x = [0,1,2,3,4]  # Domain for x  squared
  
# Y-axis values 
y = [0,1,4,9,16]   # Range  for x  squared
  
# Function to plot 
plt.plot(x,y) 
  
# function to show the plot 
plt.show() 

# x-axis values 
x = [0,1,2,3,4]  # Domain for 2 to the power of x 
  
# Y-axis values 
y = [1,2,8,16] # Range  for 2 to the power of x 
  
# Function to plot 
plt.plot(x,y) 
  
# function to show the plot 
plt.show() 
