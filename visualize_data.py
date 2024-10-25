# visualize_data.py
import matplotlib.pyplot as plt
import pandas as pd

# Load the filtered data
filtered_call_data = pd.read_csv("filtered_call_data.csv")  # assuming you've saved it from parse_data.py
filtered_put_data = pd.read_csv("filtered_put_data.csv")

# Plotting Open Interest vs Strike Price for Call and Put options
plt.figure(figsize=(10, 5))
plt.plot(filtered_call_data['Strike Price'], filtered_call_data['Open Interest'], label="Call OI", color="blue")
plt.plot(filtered_put_data['Strike Price'], filtered_put_data['Open Interest'], label="Put OI", color="red")
plt.xlabel("Strike Price")
plt.ylabel("Open Interest")
plt.title("Open Interest by Strike Price")
plt.legend()
plt.show()
