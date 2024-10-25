import requests
import json
import time

def fetch_option_chain(symbol):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            # Save data to a JSON file
            with open(f"{symbol}_option_chain.json", "w") as file:
                json.dump(data, file)
            print(f"Data for {symbol} saved successfully.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON for {symbol}. Response text: {response.text}")
    else:
        print(f"Failed to fetch data for {symbol}. Status Code: {response.status_code}")

# Fetch data for both NIFTY and HDFCBANK
fetch_option_chain("NIFTY")
fetch_option_chain("HDFCBANK")
