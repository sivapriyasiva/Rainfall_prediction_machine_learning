import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# Read the dataset
df = pd.read_csv("C:/Users/HP/Desktop/siva/surandai_data.csv")
df

# Split the date column into day, month, and year

# Ask user for input date

"""sp= df['date'].str.split('/', expand=True)
df['day'] = sp[1].astype('int')
df['month'] = sp[0].astype('int')
df['year'] = sp[2].astype('int')"""

user_input = input("Enter your date dd/mm/yyyy format : ")
day, month, year = map(int, user_input.split('/'))





# Filter the dataset by the input date
mask = (df['day'] == day) & (df['month'] == month)
filtered_df = df[mask]

# If there is no data for the input date, exit the program
if len(filtered_df) == 0:
  print("No data found for the input date.")
  exit()

# Create a pandas Series with the rainfall data
rainfall = pd.Series(filtered_df['Precipitation'])

# If there is only one data point, exit the program
if len(rainfall) <= 1:
  print("Not enough data to make a prediction.")
  exit()

# Create a numpy array for the input data
X = np.array(range(len(rainfall))).reshape(-1, 1)
#print(X)

# Create a numpy array for the output data
y = np.array(rainfall)
#print(y)

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Predict the output for the next data point
next_input = np.array([[len(rainfall)]])
next_output = model.predict(next_input)


# Check if the predicted output is greater than or equal to 0.5
if next_output >= 0.5:
  final_output = 1
else:
  final_output = 0

# Print the final output
#print(f"The final output of the rainfall is {final_output}.")
if final_output == 1:
  print(user_input,'This date is "expected rainfall" ')
else:
  print(user_input, ' This date "does Not expecting rainfall" ')

# Visualize the data using Matplotlib
import matplotlib.pyplot as plt

plt.bar(user_input,next_output)
print(next_output)
plt.plot(X,y , color='red')

plt.xlabel('user_input')
plt.ylabel('predict rainfall')
plt.show()

import matplotlib.pyplot as plt

# Create a scatter plot of X and y
plt.scatter(X[:, 0], y)

#print(X[:, 0])

# Add a line of best fit to the scatter plot
m, b = np.polyfit(X[:, 0], y, 1) 


""" function from NumPy library is used to calculate the slope and y-intercept 
The 1 argument specifies the degree of the polynomial fit which is a straight line."""

plt.plot(X[:, 0], m*X[:, 0] + b) # m-slope, b-intercept
#print(m*X[:, 0] + b)



# Set the title and labels for the plot
plt.title('Rainfall Data')
plt.xlabel('Time (days)')
plt.ylabel('Rainfall (mm)')

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Plot the data
plt.plot(filtered_df['year'], filtered_df['Precipitation'])

# Set the title and axis labels
plt.title('Year Wise Percipitation')
plt.xlabel('Year')
plt.ylabel('Precipitation')

# Display the plot
plt.show()

