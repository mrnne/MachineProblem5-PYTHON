#MACHINE PROBLEM 5 PYTHON

# Python program to graph the values of x(n) and y(n) from 0 to 200.
# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB
# matplotlib is a plotting library for Python and NumPy

# importing the matplotlib.pyplot
import matplotlib.pyplot as plot

# importing the numpy
import numpy as np

#importing the matplotlib.patches
import matplotlib.patches as mpatches

# creating numeric sequence n with 0 values, and size of 200
n = np.linspace(0,200,200)


def x(n):
    e=eval(x1)
    return e

#the input must incorporate the numpy library eg. sin() -> np.sin()
x1 = input("input equation of x: ")

# loop for i in the sequence 0 to 200
for i in range(0,200):
    
    # boolean expression where it tests if i is equal to 0
    a = i == 0
    
    # boolean expression where it tests if i is greater than 0 and less than 198
    b = 0 <i< 198
    
    # boolean expression where it tests if i equal to 199
    c = i == 199
 
    # y is a variable with the index (n) and x(n), changing every iteration
    # the piecewise function is added, while incorporating the boolean expression
    # when the boolean expression is false, the certain function will be disregard because it is multiplied to 0
    # the boolean expression results in true or false so int should be used    
    y1 = int(a)*((-1.5*x(n))+(2*x(n+1))-(0.5*x(n+2)))
    y2 = int(b)*((0.5*x(n+1))-(0.5*x(n-1)))
    y3 = int(c)*((1.5*x(n))-(2*x(n-1))+(0.5*x(n-2)))
   
    y= y1+y2+y3
   
    #plotting the values of x(n) in red using the plot command
    plot.plot(x(n),color='r')
    
    #plotting the values of y(n) in blue using the plot command
    plot.plot(y,color='b')
    
    # putting labels
    plot.xlabel('x')
    plot.ylabel('y(n)')
    
    #putting the legends using mpatches
    red_patch = mpatches.Patch(color='red', label='x(n)')
    blue_patch = mpatches.Patch(color='blue', label='y(n)')
    plot.legend(handles=[red_patch, blue_patch])
    
    # putting title
    plot.title('Machine Problem 5')
    
    #showing the plot
    plot.show