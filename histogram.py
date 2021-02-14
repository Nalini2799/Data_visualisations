# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:02:36 2021

@author: ASUS
"""

# Import the pyplot
import matplotlib.pyplot as plt

# Open and read the file
f = open('agedata.csv','r')
agefile = f.readlines()
# integer list
age_list = []
# Append the list with the age data
for records in agefile:
    age_list.append(int(records))
# Create bins list for histogram
bins = [0,10,20,30,40,50,60,70,80,90,100]
# Change the chart labels
plt.title("Age histogram")
plt.xlabel("Group")
plt.ylabel("Age")
# Create the plot
plt.hist(age_list, bins, histtype='bar', rwidth=0.9)

# Show the Plot
plt.show()

