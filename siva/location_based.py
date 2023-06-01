import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk

# Read the dataset
df = pd.read_csv("C:/Users/HP/Desktop/siva/overall district data.csv")

# Create a tkinter window
window = tk.Tk()
window.title("Rainfall Prediction")

# Create a label for location
location_label = tk.Label(window, text="Select your location:")
location_label.pack()

# Create a dropdown list for location
locations = ["Thiruchirappalli", "Tanjavur", "Tiruvarur", "Nagapattinam", "Nilgris", "Erode", "Namakkal", "Peramballur", "Ariyalur", "Selam", "Mayiladuthurai", "Cuddalore", "Kallakurichi", "Dharmapuri", "Viluppuram", "Krishnagiri", "Tirupattur", "Tiruvannamalai", "Chengalpattu", "Vellore", "Kanchipuram", "Chennai", "Tiruvallur", "Ranipet", "Tenkasi", "Kanyakumari", "Thirunelveli", "Thoothukudi", "Virudhunagar", "Ramanathapuram", "Theni", "Madurai", "Sivagangai", "Dindigul", "Pudukkottai", "Coimbatore", "Tiruppur", "Karur"]
selected_location = tk.StringVar(window)
selected_location.set(locations[0]) # Set the default value of the dropdown list
location_dropdown = tk.OptionMenu(window, selected_location, *locations)
location_dropdown.pack()

# Create a label for date
date_label = tk.Label(window, text="Enter the date (dd/mm/yyyy):")
date_label.pack()



# Create an entry box for date
date_entry = tk.Entry(window)
date_entry.pack()

# Create a label for the output
output_label = tk.Label(window, text="")
output_label.pack()

# Define a function to predict the rainfall
def predict_rainfall():
    
    # Get the user inputs
    user_location = selected_location.get()
    user_input = date_entry.get()
    if not user_input:
        output_label.config(text="Please enter a date.")
        return
    day, month, year = map(int, user_input.split('/'))

    # Filter the dataset by the input location
    filtered_df = df[df['Location'] == user_location]

    # If there is no data for the input location, display an error message
    if len(filtered_df) == 0:
        output_label.config(text="No data found for the input location.")
        return

    # Filter the dataset by the input date
    mask = (filtered_df['day'] == day) & (filtered_df['month'] == month)
    filtered_df = filtered_df[mask]

    # If there is no data for the input date, display an error message
    if len(filtered_df) == 0:
        output_label.config(text="No data found for the input date.")
        return

    # Create a pandas Series with the rainfall data
    rainfall = pd.Series(filtered_df['Percipitation'])


     # If there is
    if len(rainfall) > 1:
        mean_rainfall = np.mean(rainfall)
        if mean_rainfall >= 0.5:
            output_label.config(text="The predicted rainfall for {} on {} is . Expected rainfall".format(user_location, user_input ))
        else:
            output_label.config(text="The predicted rainfall for {} on {} is . Rainfall not expected".format(user_location, user_input ))
    else:
    # Fit a linear regression model to predict the rainfall
        X = filtered_df[['Latitude', 'Longitude']]
        y = filtered_df['Percipitation']
        model = LinearRegression().fit(X, y)


       

    # Predict the rainfall
        predicted_rainfall = model.predict([[X.iloc[0,0], X.iloc[0,1]]])[0]
        if predicted_rainfall >= 0.5:
            output_label.config(text="The predicted rainfall for {} on {} is . Expected rainfall".format(user_location, user_input))
        else:
            output_label.config(text="The predicted rainfall for {} on {} is . Rainfall not expected".format(user_location, user_input ))


       

    
predict_button = tk.Button(window, text="Predict", command=predict_rainfall)
predict_button.pack()


window.mainloop()



#1/3/2023 - not expected rainfall




