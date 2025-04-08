# Importing the necessary libraries

import pandas as pd                     # For data manipulation and analysis (Pandas)
import numpy as np                      # For numerical operations (NumPy)
import matplotlib.pyplot as plt         # For plotting graphs and visualizations (Matplotlib)
import os                               # For interacting with the operating system (like creating folders)

# Create folder for graphs
if not os.path.exists("visuals"):
    os.makedirs("visuals")

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Check for null values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing values with 'Unknown'
df.fillna("Unknown", inplace=True)

# Display basic info
print("\nData Info:")
print(df.info())

# -------------------------
# Analysis 1: Type Distribution (Movies vs TV Shows)
# -------------------------
type_counts = df['type'].value_counts()
print("\nType Counts:\n", type_counts)

# Pie chart for type distribution
type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Movie vs TV Show Distribution')
plt.ylabel("")
plt.savefig("visuals/type_distribution.png")
plt.show()
plt.clf()

# -------------------------
# Analysis 2: Content Released Per Year
# -------------------------
content_per_year = df['release_year'].value_counts().sort_index()
print("\nContent Released Per Year:\n", content_per_year.tail())

# Bar chart for content per year
content_per_year.plot(kind='bar', figsize=(12, 6), color='skyblue')
plt.title('Content Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig("visuals/content_by_year.png")
plt.show()
plt.clf()

# -------------------------
# Analysis 3: Top 10 Countries with Most Content
# -------------------------
top_countries = df['country'].value_counts().head(10)
print("\nTop 10 Countries:\n", top_countries)

# Horizontal bar chart
top_countries.plot(kind='barh', color='orange')
plt.title('Top 10 Countries with Most Content')
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig("visuals/top_countries.png")
plt.show()
plt.clf()

# -------------------------
# Analysis 4: Average Movie Duration
# -------------------------
# Remove 'min' and convert to integers
movie_durations = df[df['type'] == 'Movie']['duration']
movie_durations = movie_durations.str.replace(' min', '').replace("Unknown", np.nan).dropna().astype(int)

average_duration = np.mean(movie_durations)
print("\nAverage Movie Duration:", round(average_duration, 2), "minutes")

# Histogram of movie durations
plt.hist(movie_durations, bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig("visuals/movie_duration_distribution.png")
plt.show()
plt.clf()