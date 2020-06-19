#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read the file statepop.csv.
Create a bar graph of the states and their  population.
Hardcode the file statepop.csv, however you  must first check that it exists.

"""

import os
import csv
import matplotlib.pyplot as plt

def check_file_exist(filename_to_check):
    if not os.path.isfile(filename_to_check):
        print('File ' + filename_to_check + ' does not exist.')


xaxis = []
yaxis = []
with open('statepop.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:
            xaxis.append(row[0])
            yaxis.append(float(row[1]))

        
check_file_exist('statepop.csv')

plt.bar(xaxis, yaxis)
plt.xticks(xaxis, rotation='vertical')
plt.show()