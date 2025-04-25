# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'your_dataset.csv' with the path to your dataset
data = pd.read_csv('name.csv')

# Basic information about the dataset
print("Basic Information:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())

# Checking for null values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualizing missing data (if any)
sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()

# Plotting correlation heatmap
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Distribution plot for a numerical column
# Replace 'numerical_column' with the name of the column you'd like to analyze
sns.histplot(data['numerical_column'], kde=True, color='blue')
plt.title('Distribution of Numerical Column')
plt.show()

# Boxplot to check for outliers
# Replace 'numerical_column' with the name of the column
data = pd.read_csv('import.csv', delimiter=',')  # Change ',' to your actual delimiter
sns.boxplot(data['numerical_column'], color='green')
plt.title('Boxplot of Numerical Column')
plt.show()
