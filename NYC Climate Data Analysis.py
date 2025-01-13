# Importing matplotlib and numby Libraries
import matplotlib.pyplot as plt
import numpy as np

# Data for New York City (source: Wikipedia)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_high_temp = [39, 42, 50, 61, 71, 79, 84, 83, 75, 64, 54, 43]
record_high_temp = [72, 78, 86, 96, 97, 101, 106, 104, 102, 94, 84, 75]
avg_temp = [33, 36, 43, 54, 64, 72, 77, 76, 69, 57, 48, 37]
avg_rainfall = [3.7, 3.0, 4.0, 3.9, 4.5, 4.4, 4.6, 4.3, 4.3, 3.7, 3.8, 3.8]

# Graph 1: Line graph of average high and record high temperatures for New York City
plt.figure(figsize=(10, 6))
plt.plot(months, avg_high_temp, label='Average High', marker='o')
plt.plot(months, record_high_temp, label='Record High', marker='s')
plt.title('Average High and Record High Temperatures in New York City from 1991 to 2020 sourced from Wikipedia')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')
plt.legend()
plt.grid(True)
plt.show()

# Graph 2: Scatter plot of average temperature vs average rainfall
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

# Graph 3: Pie chart of grade categories
categories_of_Grades = ['Exams', 'Homework', 'Quizzes', 'Project']
percentages = [20, 50, 10, 20]
explode = (0, 0, 0, 0.1)  # Explode only the 'Project' slice

plt.figure(figsize=(8, 8))
plt.pie(percentages, explode=explode, labels=categories_of_Grades, autopct='%1.1f%%', startangle=90)
plt.title('Grade Categories in INFS-6140B Class')
plt.axis('equal')  # Ensuring pies appear in circles
plt.show()

input('Press ENTER to exit')