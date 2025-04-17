# Simple Olympics Data Analysis
# This script analyzes Olympic medals from 1976-2008

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set plot style
plt.style.use("ggplot")

# Load the dataset with encoding handling
print("Loading dataset...")
try:
    df = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv", encoding="latin1")

# Show basic dataset info
print(f"Dataset shape: {df.shape}")
print(f"First few rows:\n{df.head()}")

# Check for missing values
missing_values = df.isnull().sum().sum()
print(f"Total missing values: {missing_values}")

# ANALYSIS 1: Medal counts by country
print("\n--- Top 10 Countries by Medal Count ---")
country_medals = df["Country"].value_counts().head(10)
print(country_medals)

# Create a bar chart for top countries
plt.figure(figsize=(10, 6))
country_medals.plot(kind="bar")
plt.title("Top 10 Countries by Medal Count")
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_countries.png")

# ANALYSIS 2: Medal distribution by type
print("\n--- Medal Distribution ---")
medal_counts = df["Medal"].value_counts()
print(medal_counts)

# Create a pie chart for medal types
plt.figure(figsize=(8, 8))
plt.pie(medal_counts, labels=medal_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Distribution of Medal Types")
plt.axis("equal")
plt.savefig("medal_types.png")

# ANALYSIS 3: Gender distribution
print("\n--- Gender Distribution ---")
gender_counts = df["Gender"].value_counts()
print(gender_counts)
print(
    f"Percentage of male athletes: {gender_counts['Men']/gender_counts.sum()*100:.1f}%"
)
print(
    f"Percentage of female athletes: {gender_counts['Women']/gender_counts.sum()*100:.1f}%"
)

# Create a pie chart for gender distribution
plt.figure(figsize=(8, 8))
plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    colors=["#3498db", "#e74c3c"],
)
plt.title("Medal Distribution by Gender")
plt.axis("equal")
plt.savefig("gender_distribution.png")

# ANALYSIS 4: Medals by Olympic year
print("\n--- Medals by Olympic Year ---")
year_medals = df["Year"].value_counts().sort_index()
print(year_medals)

# Create a line chart for medals by year
plt.figure(figsize=(10, 6))
year_medals.plot(kind="line", marker="o")
plt.title("Number of Medals Awarded by Olympic Year")
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.grid(True)
plt.savefig("medals_by_year.png")

# ANALYSIS 5: Top sports
print("\n--- Top 5 Sports by Medal Count ---")
sport_medals = df["Sport"].value_counts().head(5)
print(sport_medals)

# Create a horizontal bar chart for top sports
plt.figure(figsize=(10, 6))
sport_medals.plot(kind="barh", color="#2ecc71")
plt.title("Top 5 Sports by Medal Count")
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.tight_layout()
plt.savefig("top_sports.png")

# ANALYSIS 6: Medal breakdown by country
print("\n--- Medal Breakdown for Top Countries ---")

# Create a pivot table to analyze medals by country and type
country_medal_pivot = pd.pivot_table(
    df,
    index="Country",
    columns="Medal",
    values="Athlete",
    aggfunc="count",
    fill_value=0,
)

# Sort by total medals
country_medal_pivot["Total"] = country_medal_pivot.sum(axis=1)
top_countries = country_medal_pivot.sort_values("Total", ascending=False).head(10)

# Display the medal breakdown
print(top_countries[["Gold", "Silver", "Bronze", "Total"]])

# Create a stacked bar chart for medal breakdown
plt.figure(figsize=(12, 8))
top_countries[["Gold", "Silver", "Bronze"]].plot(
    kind="bar", stacked=True, color=["#FFD700", "#C0C0C0", "#CD7F32"]
)
plt.title("Medal Breakdown for Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("medal_breakdown.png")

# ANALYSIS 7: Gender distribution in top sports
print("\n--- Gender Distribution in Top Sports ---")

# Create a cross-tabulation of sport and gender
sport_gender = df.groupby(["Sport", "Gender"]).size().unstack(fill_value=0)

# Select top 5 sports by total medals
top_sports = sport_gender.sum(axis=1).sort_values(ascending=False).head(5).index

# Display the gender distribution
print(sport_gender.loc[top_sports])

# Create a stacked bar chart for gender distribution in sports
plt.figure(figsize=(12, 6))
sport_gender.loc[top_sports].plot(
    kind="barh", stacked=True, color=["#3498db", "#e74c3c"]
)
plt.title("Gender Distribution in Top 5 Sports")
plt.xlabel("Number of Medals")
plt.tight_layout()
plt.savefig("sport_gender.png")

# ANALYSIS 8: Medal prediction model
print("\n--- Predicting Gold Medals ---")

# Create a binary target: 1 for Gold, 0 for Silver/Bronze
df["is_gold"] = df["Medal"].apply(lambda x: 1 if x == "Gold" else 0)

# Select features and create dummy variables
features = ["Country", "Sport", "Gender"]
X = pd.get_dummies(df[features], drop_first=True)
y = df["is_gold"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Get top 5 important features
feature_importance = pd.DataFrame(
    {"Feature": X.columns, "Importance": model.feature_importances_}
)
top_features = feature_importance.sort_values("Importance", ascending=False).head(5)
print("\nTop 5 features for predicting Gold medals:")
print(top_features)

# Create a bar chart for feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x="Importance", y="Feature", data=top_features, palette="viridis")
plt.title("Top 5 Features for Predicting Gold Medals")
plt.tight_layout()
plt.savefig("feature_importance_simple.png")

print("\nAnalysis complete!")
