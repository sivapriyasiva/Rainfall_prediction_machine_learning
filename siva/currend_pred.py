

import pandas as pd
from sklearn.naive_bayes import GaussianNB
import tkinter as tk
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("C:/Users/HP/Desktop/siva/anndataset.csv")
inputs = data.drop('rainfall', axis='columns')
target = data['rainfall']

# Create classifier
classifier = GaussianNB()
classifier.fit(inputs, target)

# Define function to get prediction and show alert message
def predict_rainfall():
    temp = float(temp_entry.get())
    humidity = float(humidity_entry.get())
    wind_speed = float(wind_speed_entry.get())

    test_data = [[temp, humidity, wind_speed]]
    prediction = classifier.predict(test_data)[0]
    
    if prediction == 1:
        result_label.config(text="The probability of rainfall is 'yes'")
        alert_label.config(text='"Rainfall expected today". Please carry an umbrella.')
    else:
        result_label.config(text="The probability of rainfall is 'no'")
        alert_label.config(text="NO Rainfall expected today")

    # Calculate accuracy
    acc = classifier.score(inputs, target)
    accuracy_label.config(text=f"Accuracy: {acc:.2f}")
        
# Create GUI
window = tk.Tk()
window.title("Rainfall Prediction")
window.geometry("400x250")

# Create input fields and labels
temp_label = tk.Label(window, text="Temperature:")
temp_label.grid(row=0, column=0)
temp_entry = tk.Entry(window)
temp_entry.grid(row=0, column=1)

humidity_label = tk.Label(window, text="Humidity:")
humidity_label.grid(row=1, column=0)
humidity_entry = tk.Entry(window)
humidity_entry.grid(row=1, column=1)

wind_speed_label = tk.Label(window, text="Wind Speed:")
wind_speed_label.grid(row=2, column=0)
wind_speed_entry = tk.Entry(window)
wind_speed_entry.grid(row=2, column=1)

# Create button to predict rainfall
predict_button = tk.Button(window, text="Predict", command=predict_rainfall)
predict_button.grid(row=3, column=0)

# Create label to show result of prediction
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=1)

# Create label to show alert message
alert_label = tk.Label(window, text="")
alert_label.grid(row=4, column=0, columnspan=2)

# Create label to show accuracy score
accuracy_label = tk.Label(window, text="")
accuracy_label.grid(row=5, column=0, columnspan=2)

window.mainloop()


