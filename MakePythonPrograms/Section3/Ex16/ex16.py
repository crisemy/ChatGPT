import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("stockholm_updated.csv")

# Create a histogram using the "TG" column
fig, ax = plt.subplots()
ax.hist(data["TG"], bins=20, edgecolor='black')
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Frequency")
ax.set_title("Temperature Histogram")

# Display the histogram using Streamlit
st.pyplot(fig)
