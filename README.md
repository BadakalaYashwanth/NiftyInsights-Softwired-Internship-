# NiftyInsights

Overview
NiftyInsights is a web application designed for analyzing the NIFTY Option Chain, providing users with valuable insights into market trends through interactive visualizations. 
This tool enables traders and investors to make informed decisions based on Open Interest data for call-and-put options.

# Features

* User-Friendly Interface: Intuitive design allowing easy navigation and interaction.
* Interactive Visualization: Dynamic graphs displaying Open Interest for both call and put options.
* Customizable Strike Price Range: Users can adjust the strike price range using a slider for real-time data representation.
* Data Filtering: Automatically filters options data based on user-selected strike price ranges.

# Technology Stack

* Frontend: Streamlit - A framework for building web applications in Python.
* Backend: Python - A programming language for data processing and fetching.
* Data Visualization: Matplotlib - Library for creating static, animated, and interactive visualizations.
* Data Source: NIFTY Option Chain data is fetched from the NSE India website.

# Installation

# Prerequisites

* Python 3.9 or higher
* pip (Python package installer)



# Steps
* Clone the Repository:
* git clone [https://github.com/yourusername/NiftyInsights.git](https://github.com/BadakalaYashwanth/NiftyInsights-Softwired-Internship-)
* cd NiftyInsights

# Install Dependencies:

* pip install -r requirements.txt

# Run the Application:

* streamlit run app.py

* Access the Application: Open your web browser and go to http://localhost:8501.

# File Structure

# NiftyInsights/
* ├── app.py               # Main application file
* ├── parse_data.py        # Script for fetching and processing option chain data
* ├── requirements.txt      # Python dependencies
* ├── Dockerfile            # Docker configuration file
* ├── filtered_call_data.csv # Filtered call options data
* ├── filtered_put_data.csv  # Filtered put options data
* └── NIFTY_option_chain.json # Raw data fetched from NSE

# How It Works
* 1. Data Fetching: The application retrieves the latest NIFTY option chain data from the NSE using the parse_data.py script.
* 2. Data Parsing: The JSON data is processed to extract relevant information, such as strike prices and open interest values.
* 3. Data Storage: Filtered call and put option data are saved in CSV files for efficient access and analysis.
* 4. User Interaction: Users can select strike price ranges through a slider, and the application updates the visualizations in real-time.

# Contribution
* Contributions are welcome! Please follow these steps:

* Fork the repository.
* Create a new branch (git checkout -b feature/YourFeature).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature/YourFeature).
* Create a pull request.



