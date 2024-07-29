import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("householdtask3.csv")
data.head(10)

#Scatter plot with year against own
plt.scatter(data['year'],data['own'])

# Adding Title to the Plot
plt.title ("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the Chart
plt.show()


#Line Chart
plt.plot(data["year"])
plt.plot(data["own"])

# Adding Title to the Plot
plt.title ("Line Plot")

# Setting the X and Y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the Chart
plt.show()


#barchart or bar plot
plt.bar(data['year'],data['own'])

# Adding Title to the Plot
plt.title ("Bar Plot")

# Setting the X and Y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the Chart
plt.show()


#Histogram
plt.hist(data['income'])

# Adding Title to the Plot
plt.title ("Histagram Plot")

#Showing the Chart
plt.show()