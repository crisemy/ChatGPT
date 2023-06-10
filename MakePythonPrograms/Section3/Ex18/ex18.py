import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("stockholm_updated.csv")

# Convert DATE column to datetime
data["DATE"] = pd.to_datetime(data["DATE"], format="%Y%m%d")

# Aggregate temperatures by year
data["Year"] = data["DATE"].dt.year
aggregated_data = data.groupby("Year")["TG"].mean().reset_index()

# Create bar graph
def create_bar_graph(data, unit):
    # Set up figure and axes
    fig, ax = plt.subplots()

    # Convert temperatures to Fahrenheit if selected
    if unit == "Fahrenheit":
        data["TG"] = (data["TG"] * 1.8) + 32
        ax.set_ylabel("Temperature (°F)")
    else:
        ax.set_ylabel("Temperature (°C)")

    # Plot bar graph
    ax.bar(data["Year"], data["TG"])

    # Customize plot
    ax.set_title("Yearly Temperature Observations")
    ax.set_xlabel("Year")

    # Display plot
    st.pyplot(fig)

# Main Streamlit app
def main():
    # Set title
    st.title("Yearly Temperature Observations")

    # Display the first few rows of the data
    st.subheader("Data Preview")
    st.write(data.head())

    # Create dropdown widget
    unit = st.sidebar.selectbox("Select Unit", ["Celsius", "Fahrenheit"])

    # Generate and display bar graph
    st.subheader("Bar Graph")
    create_bar_graph(aggregated_data, unit)

if __name__ == "__main__":
    main()