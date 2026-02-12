import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("📊 Interactive Data Dashboard")
st.markdown("Explore and visualize dataset interactively!")

# Load built-in dataset
df = sns.load_dataset("tips")

# Sidebar controls
st.sidebar.header("🔍 Filter Options")

selected_day = st.sidebar.multiselect(
    "Select Day(s)",
    options=df["day"].unique(),
    default=df["day"].unique()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Scatter Plot", "Histogram"]
)

# Filter data
filtered_df = df[
    (df["day"].isin(selected_day)) &
    (df["sex"].isin(selected_gender))
]

# Display Data
st.subheader("📋 Filtered Data")
st.dataframe(filtered_df)

# Show basic stats
st.subheader("📈 Summary Statistics")
st.write(filtered_df.describe())

# Plotting
st.subheader("📊 Visualization")

fig, ax = plt.subplots()

if chart_type == "Bar Chart":
    sns.barplot(data=filtered_df, x="day", y="total_bill", ax=ax)

elif chart_type == "Scatter Plot":
    sns.scatterplot(data=filtered_df, x="total_bill", y="tip", hue="sex", ax=ax)

elif chart_type == "Histogram":
    sns.histplot(filtered_df["total_bill"], bins=15, ax=ax)

st.pyplot(fig)

st.markdown("---")
st.success("🚀 Your interactive dashboard is running!")
