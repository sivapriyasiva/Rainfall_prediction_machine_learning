import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

#Read the dataset
df = pd.read_csv("C:\\Users\\HP\\Desktop\\siva\\surandai_data.csv") 
df

'''sp= df['date'].str.split('/', expand=True) df['day'] = sp[1].astype('int') df['month'] = sp[0].astype('int') df['year'] = sp[2].astype('int')'''


start_date = input("Enter start date (YYYY/MM/DD): ") 
end_date = input("Enter end date (YYYY/MM/DD): ")

#Generate a range of dates between start and end date
date_range = pd.date_range(start=start_date, end=end_date)

#Initialize lists to store dates and predictions
dates = [] 
predictions = []

def prediction(): 
  for date in date_range: 
    day = date.day
    month = date.month 
    year = date.year 
    date_string = f"{day}/{month}/{year}" 
    date_list = date_string.split('/') 
    day, month, year = map(int, date_list)

    #Filter the dataset by the input date
    mask = (df['day'] == day) & (df['month'] == month)
    filtered_df = df[mask]
    #If there is no data for the input date, exit the program
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

    # Print the final output
    #print(f"The final output of the rainfall is {final_output}.")
    if final_output == 1:
      print(date, "Today is rainfall")
    else:
      print(date, "Not expecting rainfall today")

 

    '''if final_output == 1:
      filter_rainfall_dates= (date, next_output)
      print(filter_rainfall_dates)
    else:
      continue
'''

prediction() 

