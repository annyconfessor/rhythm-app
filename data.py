import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Data loading
df = pd.read_json("projects.json")

# Filter relevant columns
df_actual_hours = df[["name", "actual_hours"]].copy()
df_actual_hours["actual_hours"] = df_actual_hours["actual_hours"].fillna(0)

# Descending order
df_actual_hours = df_actual_hours.sort_values(by="actual_hours", ascending=False)

# Figure size
plt.figure(figsize=(10, 8))

# Style
sns.set_style("whitegrid")
sns.barplot(x="actual_hours", y="name", data=df_actual_hours, palette="viridis")

# Titles
plt.title("Time invested by Project and Hours", fontsize=16)
plt.xlabel("Hours")
plt.ylabel("Project")

# To show
plt.show()
# st.pyplot(plt)