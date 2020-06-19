
"""
Create a line graph.
Create 25 random numbers between 10-100.
Have X,Y Labels and a Title
Make the line color black.

"""

import random
import matplotlib.pyplot as plt

numbers_to_plot = []
for i in range(25):
    numbers_to_plot.append(random.randint(10,100))

plt.plot(numbers_to_plot, color = 'black')

plt.ylabel('No of number')
plt.xlabel('Random numbers')
plt.title('Python HW 9.1')

plt.show()