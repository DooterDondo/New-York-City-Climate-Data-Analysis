# New-York-City-Climate-Data-Analysis
A thorough analysis of the climate of New York City - Data Gathered from Wikipedia
New York City Climate Data Analysis:
This project visualizes climate data for New York City. It includes line graphs, scatter plots, and pie charts to provide insights into temperature trends, rainfall patterns, and grade categories.

Getting Started
Prerequisites
Make sure you have the following libraries installed:

matplotlib

numpy

You can install them using pip:

bash
pip install matplotlib numpy
Importing Libraries
python
import matplotlib.pyplot as plt
import numpy as np
Data
The data for this project was sourced from Wikipedia. It includes:

Months: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

Average High Temperature (°F): [39, 42, 50, 61, 71, 79, 84, 83, 75, 64, 54, 43]

Record High Temperature (°F): [72, 78, 86, 96, 97, 101, 106, 104, 102, 94, 84, 75]

Average Temperature (°F): [33, 36, 43, 54, 64, 72, 77, 76, 69, 57, 48, 37]

Average Rainfall (inches): [3.7, 3.0, 4.0, 3.9, 4.5, 4.4, 4.6, 4.3, 4.3, 3.7, 3.8, 3.8]

Visualizations
Graph 1: Line Graph of Average High and Record High Temperatures
python
plt.figure(figsize=(10, 6))
plt.plot(months, avg_high_temp, label='Average High', marker='o')
plt.plot(months, record_high_temp, label='Record High', marker='s')
plt.title('Average High and Record High Temperatures in New York City from 1991 to 2020 sourced from Wikipedia')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')
plt.legend()
plt.grid(True)
plt.show()
Graph 2: Scatter Plot of Average Temperature vs Average Rainfall
python
plt.figure(figsize=(10, 6))
plt.scatter(avg_temp, avg_rainfall)
plt.title('Average Temperature vs Average Rainfall in New York City from 1991 to 2020 sourced from Wikipedia')
plt.xlabel('Average Temperature (°F)')
plt.ylabel('Average Rainfall (inches)')
# Making sure the month names appear in the Scatter Plot
for i, month in enumerate(months):
    plt.annotate(month, (avg_temp[i], avg_rainfall[i]))
plt.grid(True)
plt.show()
Graph 3: Pie Chart of Grade Categories in INFS-6140B Class
python
categories_of_Grades = ['Exams', 'Homework', 'Quizzes', 'Project']
percentages = [20, 50, 10, 20]
explode = (0, 0, 0, 0.1)  # Explode only the 'Project' slice

plt.figure(figsize=(8, 8))
plt.pie(percentages, explode=explode, labels=categories_of_Grades, autopct='%1.1f%%', startangle=90)
plt.title('Grade Categories in INFS-6140B Class')
plt.axis('equal')  # Ensuring pies appear in circles
plt.show()
Running the Project
To run the project, execute the script and follow the prompts:

python
input('Press ENTER to exit')
