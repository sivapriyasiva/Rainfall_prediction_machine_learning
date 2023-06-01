import tkinter as tk
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
import datetime 

#Read the dataset
df = pd.read_csv("C:/Users/HP/Desktop/siva/surandai_data.csv") 

# Initialize lists to store dates and predictions
dates = [] 
predictions = []

def prediction(start_date, end_date): 
  #Generate a range of dates between start and end date
  date_range = pd.date_range(start=start_date, end=end_date)

  for date in date_range: 
    day = date.day
    month = date.month 
    year = date.year 
    date_string = f"{day}/{month}/{year}" 
    date_list = date_string.split('/') 
    day, month, year = map(int, date_list)

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

    #  Create a numpy array for the output data
    y = np.array(rainfall)

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

    # Add the predicted rainfall value to a new column in the dataset
    df.loc[date, 'predicted_rainfall'] = next_output[0]

    # Add the date and prediction to the lists
    dates.append(date)
    predictions.append(final_output)

  # Sort the dataset by the predicted rainfall column in descending order
  sorted_df = df.sort_values(by='predicted_rainfall', ascending=False)
  # Get the top 10 rainfall days
  top_10_rainfall = sorted_df[['predicted_rainfall']].head(10)
  print("Top 10 rainfall days:")
  print(top_10_rainfall)
  
  # Display the output in a new window
  display_output(top_10_rainfall)

def display_output(data):
  # Create a new window for the output
  output_window = tk.Toplevel()
  output_window.title("Top 10 rainfall days")
  
  # Create a label for the output
  output_label = tk.Label(output_window, text=data.to_string(index=True))
  output_label.pack()

# Create the GUI
root = tk.Tk()
root.title("Rainfall Prediction")

# Create the start date input
start_label = tk.Label(root, text="Start Date (YYYY/MM/DD):")
start_label.pack()
start_entry = tk.Entry(root)
start_entry.pack()

# Create the end date input
end_label = tk.Label(root, text="End Date (YYYY/MM/DD):")
end_label = tk.Label(root, text="End Date (YYYY/MM/DD):")
end_label.pack()
end_entry = tk.Entry(root)
end_entry.pack()

submit_button = tk.Button(root, text="Submit", command=lambda: prediction(start_entry.get(), end_entry.get()))
submit_button.pack()

root.mainloop()
