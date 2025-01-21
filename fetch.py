import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st
import os
import chardet

# Function to fetch the latest CSV file
@st.cache_data  # Cache the result to avoid re-fetching on every interaction
def fetch_latest_csv():
    url = "https://tgftp.nws.noaa.gov/logs/shipstats/"
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all CSV files using a regex pattern
        csv_files = [a['href'] for a in soup.find_all('a', href=re.compile(r'^shipstat\.out\.\d{12}\.csv$'))]

        if not csv_files:
            st.error("No CSV files found in the directory.")
            return None

        # Get the latest file (assuming filenames are in YYYYMMDD.csv format)
        latest_file = max(csv_files)

        # Download the latest file
        latest_file_url = url + latest_file
        response = requests.get(latest_file_url)
        response.raise_for_status()

        # Save the file
        with open(latest_file, 'wb') as f:
            f.write(response.content)

        st.success(f"Downloaded: {latest_file}")
        return latest_file

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the page: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to analyze and plot the data
def analyze(latest_file):
    if not os.path.exists(latest_file):
        st.error(f"File not found: {latest_file}")
        return

    # Detect file encoding
    with open(latest_file, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']

    # Read the file with the detected encoding
    df = pd.read_csv(latest_file, encoding=encoding)
    df = df[[' OCEAN', ' QUADRANT', ' LAT', ' LONG']]
    df = df.head(100)

    # Create a Folium map
    st.title("NOAA SHIPSTAT LOG VISUALIZATION")
    map_center = [df[' LAT'].mean(), df[' LONG'].mean()]
    m = folium.Map(location=map_center, zoom_start=2)

    # Add markers for each latitude and longitude
    for index, row in df.iterrows():
        folium.Marker(
            location=[row[' LAT'], row[' LONG']],
            popup=f"Ocean: {row[' OCEAN']}, Quadrant: {row[' QUADRANT']}",
            tooltip=f"Lat: {row[' LAT']}, Long: {row[' LONG']}"
        ).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=2000, height=600)  # Adjust width and height as needed

# Streamlit App
def main():
    st.title("NOAA Shipstat Log Visualizer")

    # Fetch the latest CSV file
    latest_file = fetch_latest_csv()

    if latest_file:
        # Analyze and plot the data
        analyze(latest_file)

# Run the app
if __name__ == "__main__":
    main()