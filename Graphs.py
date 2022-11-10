# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:46:16 2022

@author: HP
"""

# importing pandas library
import matplotlib.pyplot as plt
# import matplotlib library
import pandas as pd
# reading data from csv file for plotting bar graph and pie chart
details = pd.read_csv("C:/Users/HP/Documents/Assignment/poultry-inspection-assistant-february-2020 -trimmed.csv")
# choosing first 10 rows  for bar graph
top_10 = details[0:9]
# choosing random 4 rows  for pie chart
data = details[2:6]
# reading data from csv file for plotting line graph
details2 = pd.read_csv("C:/Users/HP/Documents/Assignment/active-library-users-by-age.csv")
# choosing firts 10 rows  for line graph
lb = details2[:9]


def bar():
    """This function is used to plot a bar graph of poultry Inspection Assistant Data,where the y axis is showing Number of PIAs"""
    
    plt.figure(figsize=(8,6))
    plt.bar(top_10["Abattoir Name"], top_10["NumberOfPIA"],color='g')
    plt.xticks(rotation = 90)
    plt.xlabel("Abattoir Name")
    plt.ylabel("NumberOfPIA")
    plt.title("Poultry Inspection Assistant Data")
    plt.savefig("bargraph.png")
    plt.legend()
    plt.show()
bar()


def pie():
    """This function is used to plot a pie chart of poultry Inspection Assistant Data."""
    
    
    plt.pie(data["NumberOfPIA"],labels=data["Abattoir Name"],autopct='%1.1f%%',startangle=140)
    plt.title("Number of Poultry Inspection Assistant Information")
    plt.legend(bbox_to_anchor = (1,1))
    plt.savefig("piechart.png")
    plt.show()
    
pie()


def line():
   """This function is used to plot a line graph of Library users in different age groups.The y axis is showing the number of users in that particular age group"""
   
   plt.figure(figsize=(8,6))
   plt.plot(lb['Name'], lb['Age0-4'], label="Age0-4")
   plt.plot(lb['Name'], lb['Age5-11'], label="Age5-11")
   plt.plot(lb['Name'], lb['Age12-17'], label="Age12-17")
   plt.title("Active library users by age")
   plt.xlabel("Library Name")
   plt.xticks(rotation = 90)
   plt.ylabel("Range")
   plt.legend(fontsize=10)
   plt.savefig("linegraph.png")
   plt.show()
line()