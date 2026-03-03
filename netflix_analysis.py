import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic Cleaning
df.drop_duplicates(inplace=True)
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Not Rated")

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# -------------------------------
# 1. Movies vs TV Shows
# -------------------------------
type_count = df['type'].value_counts()

plt.figure()
type_count.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# -------------------------------
# 2. Content Growth Over Years
# -------------------------------
year_data = df['year_added'].value_counts().sort_index()

plt.figure()
year_data.plot()
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# -------------------------------
# 3. Top 10 Genres
# -------------------------------
genre_data = df['listed_in'].str.split(',').explode()
top_genres = genre_data.value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top 10 Genres")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 4. Top 10 Directors
# -------------------------------
top_directors = df['director'].value_counts().head(10)

plt.figure()
top_directors.plot(kind='bar')
plt.title("Top 10 Directors")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 5. Rating Distribution
# -------------------------------
top_ratings = df['rating'].value_counts().head(10)

plt.figure()
top_ratings.plot(kind='bar')
plt.title("Top Ratings Distribution")
plt.xticks(rotation=45)
plt.show()

print("Advanced Analysis Completed Successfully!")
