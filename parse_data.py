# parse_data.py
import pandas as pd
import json

# Load JSON data
data_file = "NIFTY_option_chain.json"
with open(data_file, "r") as file:
    data = json.load(file)

# Extract the latest expiry date from the data
expiry_date = data['records']['expiryDates'][0]  # This assumes the first is the nearest expiry

def extract_option_data(data, option_type="CE"):
    # Extract the list of options based on type: "CE" (Call) or "PE" (Put)
    options = [option for option in data['records']['data'] if option.get(option_type)]
    return pd.DataFrame([{
        'Strike Price': option['strikePrice'],
        'Open Interest': option[option_type]['openInterest'],
        'LTP': option[option_type]['lastPrice'],
        'Change in OI': option[option_type]['changeinOpenInterest'],
        'Volume': option[option_type]['totalTradedVolume']
    } for option in options])

def filter_by_expiry(data, expiry_date, option_type="CE"):
    options = [option for option in data['records']['data'] if option.get(option_type) and option['expiryDate'] == expiry_date]
    return pd.DataFrame([{
        'Strike Price': option['strikePrice'],
        'Open Interest': option[option_type]['openInterest'],
        'LTP': option[option_type]['lastPrice'],
        'Change in OI': option[option_type]['changeinOpenInterest'],
        'Volume': option[option_type]['totalTradedVolume']
    } for option in options])

# Extract Call and Put Data
filtered_call_data = filter_by_expiry(data, expiry_date, option_type="CE")
filtered_put_data = filter_by_expiry(data, expiry_date, option_type="PE")

# Save the filtered data to CSV files
filtered_call_data.to_csv("filtered_call_data.csv", index=False)
filtered_put_data.to_csv("filtered_put_data.csv", index=False)

# Print the first few rows of the filtered data
print("Filtered Call Option Data:\n", filtered_call_data.head())
print("Filtered Put Option Data:\n", filtered_put_data.head())
