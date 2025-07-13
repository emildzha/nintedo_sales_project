import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"E:\GitHub\nintedo_sales_project\data\raw\vgsales.csv", dtype={"Year": str}
)

# Top 10 games by Global Sales
top_games = df.nlargest(10, "Global_Sales")[["Name", "Global_Sales"]]

print("Top 10 games by Global Sales:")
print(top_games)

# Platforms with the highest sales
highest_sales_platforms = (
    df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
)

print("Platforms with the highest sales (top 10):")
print(highest_sales_platforms.head(10))

# Sales evolution over the years (chart)
df1 = df[pd.notna(df["Year"])]
df1 = df1[~df1["Year"].isin(["2017", "2020"])]

years = df1["Year"].unique().astype(int)
years.sort()


sales_by_year = df1.groupby("Year")["Global_Sales"].sum()

plt.figure(figsize=(12, 6))
plt.plot(years, sales_by_year)
plt.xlabel("Year")
plt.ylabel("Global Sales")
plt.title("Sales Evolution Over the Years")
plt.show()

# Most popular genres
most_popular_genres = (
    df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
)

print("Most Popular Genres (top 10):")
print(most_popular_genres.head(10))
