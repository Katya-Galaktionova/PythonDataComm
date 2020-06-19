#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a pie chart of car theft data.
Only use data that has a theft rate of over 2.5%
Use the file cartheft.csv, hard code the file, but  check that the file exists.

"""

import os
import csv
import matplotlib.pyplot as plt

def check_file_exist(filename_to_check):
    if not os.path.isfile(filename_to_check):
        print('File ' + filename_to_check + ' does not exist.')

check_file_exist('cartheft.csv')

car = []
model = []
theft = []
with open('cartheft.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if float(row[4]) > 2.5:
            car.append(row[0])
            model.append(row[1])
            theft.append(row[4])
car_model = list(zip(car, model))
        

plt.pie(theft, labels = car_model, shadow = True, startangle = 90)

plt.axis('equal')
plt.show()
