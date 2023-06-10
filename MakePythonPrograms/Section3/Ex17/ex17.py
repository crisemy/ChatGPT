import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("stockholm_updated.csv")

# Convert the "DATE" column to a datetime format
data["DATE"] = pd.to_datetime(data["DATE"], format="%Y%m%d")

# Extract the year from the "DATE" column
data["Year"] = data["DATE"].dt.year

# Group the data by year and calculate the average temperature for each year
yearly_temperatures = data.groupby("Year")["TG"].mean().reset_index()

# Create a bar graph for the yearly temperatures
fig, ax = plt.subplots()
ax.bar(yearly_temperatures["Year"], yearly_temperatures["TG"])
ax.set_xlabel("Year")
ax.set_ylabel("Average Temperature (°C)")
ax.set_title("Yearly Average Temperatures")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the bar graph using Streamlit
st.pyplot(fig)
