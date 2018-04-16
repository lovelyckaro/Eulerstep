import matplotlib.pyplot as plt
#Import math if needed for function
#import math

#Derivative of the function you want to plot
def f(x, y):
    return (y + 2 * x)

#Get user input for start and end point, as well as step-size
x0 = input("X-Start: ")
y0 = input("Y-Start: ")
h = input("H: ")
s = input("End: ")

#Init list for x, and y axes
xlist = [x0]
ylist = [y0]

#Approximate y coordinates using Euler's step-function
for i in range(0, int((s - x0) / h)):
    xlist.append(xlist[i] + h)
    #Y coordinate is approximated using dx * y' where y' is the derivative in the point before 
    ylist.append(ylist[i] + h * f(xlist[i], ylist[i]))
    
#Print last point
print("(" + str(xlist[-1]) + ", " + str(ylist[-1]) + ")")

#Plot a graph connecting the points
plt.plot(xlist, ylist)
plt.show()