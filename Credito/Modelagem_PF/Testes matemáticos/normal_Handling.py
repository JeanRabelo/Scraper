import simpy
from scipy.stats import norm as normDist
# importing the required module
import matplotlib.pyplot as plt

# x axis values
y = range(-100,100,)
print(y)

# print(value="aaa",)

# print()
# z = scipy.stats.norm()
z = normDist.pdf(y,0,40)
print(z)
# corresponding y axis values
# y = range(4,7)
x = z


# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')
plt.show()

# function to show the plot
