# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Configure style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Step 2: Load Dataset
df = pd.read_csv("titanic.csv")  # Replace with your actual file path
print("First 5 rows of dataset:")
print(df.head())

# Step 3: Understand Dataset
print("\nDataset Info:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

print("\nDataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())

# Step 4: Handle Missing Values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Fill missing age values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop rows with missing 'Embarked'
df.dropna(subset=['Embarked'], inplace=True)

# Step 5: Ask Meaningful Questions
# Q1. How many passengers survived?
survived_count = df['Survived'].value_counts()
print("\nSurvival Counts:\n", survived_count)

# Q2. Survival by Gender
survival_by_gender = df.groupby('Sex')['Survived'].mean()
print("\nSurvival Rate by Gender:\n", survival_by_gender)

# Q3. Age vs Survival
avg_age_survived = df.groupby('Survived')['Age'].mean()
print("\nAverage Age by Survival:\n", avg_age_survived)

# Step 6: Data Visualization

# 1. Survival Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# 2. Gender-based Survival
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Gender")
plt.show()

# 3. Age Distribution
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# 4. Passenger Class vs Age
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title("Passenger Class vs Age")
plt.show()

# Step 7: Correlation Analysis
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Step 8: Summary of Findings
print("\nSummary of Insights:")
print("- More males than females on board, but females had a much higher survival rate.")
print("- Younger passengers generally had a slightly higher chance of survival.")
print("- Passengers in higher classes (Pclass 1) had better survival outcomes.")
print("- Some columns had missing values which were handled properly.")

# Step 9: Save cleaned data (optional)
df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned data saved as 'titanic_cleaned.csv'")
