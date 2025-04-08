import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create folder for graphs
if not os.path.exists("visuals"):
    os.makedirs("visuals")

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Check for null values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing values for simplicity
df.fillna("Unknown", inplace=True)

# Check basic stats
print("\nData Info:")
print(df.info())

# Count movies vs TV shows
type_counts = df['type'].value_counts()
print("\nType Counts:\n", type_counts)

# Content released per year
content_per_year = df['release_year'].value_counts().sort_index()

# Most frequent countries
top_countries = df['country'].value_counts().head(10)

# Average duration of Movies
movie_durations = df[df['type'] == 'Movie']['duration'].str.replace(' min', '').replace("Unknown", np.nan).dropna().astype(int)
print("\nAverage Movie Duration:", np.mean(movie_durations), "minutes")

# Plot: Type Distribution
type_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Movie vs TV Show Distribution')
plt.ylabel("")
plt.savefig("visuals/type_distribution.png")
plt.show()
plt.clf()

# Plot: Content Released per Year
content_per_year.plot(kind='bar', figsize=(12, 6), color='skyblue')
plt.title('Content Released per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.savefig("visuals/content_by_year.png")
plt.show()
plt.clf()

# Plot: Top 10 Countries
top_countries.plot(kind='barh', color='orange')
plt.title('Top 10 Countries with Most Content')
plt.xlabel('Count')
plt.savefig("visuals/top_countries.png")
plt.show()
plt.clf()