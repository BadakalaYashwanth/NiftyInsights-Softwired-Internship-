# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("NIFTY Option Chain Analysis")

# Define file names
call_data_file = "filtered_call_data.csv"
put_data_file = "filtered_put_data.csv"

# Check if the files exist
if os.path.exists(call_data_file) and os.path.exists(put_data_file):
    # Load data
    filtered_call_data = pd.read_csv(call_data_file)
    filtered_put_data = pd.read_csv(put_data_file)

    # User input for strike price range
    strike_min, strike_max = st.slider(
        "Select Strike Price Range", 
        int(filtered_call_data['Strike Price'].min()), 
        int(filtered_call_data['Strike Price'].max()), 
        (int(filtered_call_data['Strike Price'].min()), 
         int(filtered_call_data['Strike Price'].max()))
    )

    # Filter data based on strike price range
    filtered_call_data = filtered_call_data[
        (filtered_call_data['Strike Price'] >= strike_min) & 
        (filtered_call_data['Strike Price'] <= strike_max)
    ]
    filtered_put_data = filtered_put_data[
        (filtered_put_data['Strike Price'] >= strike_min) & 
        (filtered_put_data['Strike Price'] <= strike_max)
    ]

    # Plot Open Interest by Strike Price
    fig, ax = plt.subplots()
    ax.plot(filtered_call_data['Strike Price'], filtered_call_data['Open Interest'], label="Call OI", color="blue")
    ax.plot(filtered_put_data['Strike Price'], filtered_put_data['Open Interest'], label="Put OI", color="red")
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Open Interest")
    ax.set_title("Open Interest by Strike Price")
    ax.legend()
    st.pyplot(fig)
else:
    st.error("One or both of the CSV files do not exist. Please run parse_data.py first.")
