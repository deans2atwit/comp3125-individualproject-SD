# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('../data/Question 1.csv')

# Clean the data (ensure we handle missing values or non-numeric entries)
# Convert "Funding" and "Size" columns to numeric values
data['Funding'] = pd.to_numeric(data['Funding'], errors='coerce')
data['Size'] = pd.to_numeric(data['Size'], errors='coerce')

# Drop rows with missing values
data.dropna(subset=['Funding', 'Size'], inplace=True)

# Set up the plot size
plt.figure(figsize=(10, 6))

# Create a Seaborn regression plot
sns.regplot(x='Size', y='Funding', data=data, scatter_kws={'color': 'blue'}, line_kws={'color': 'red', 'linewidth': 2})

# Adding labels and title
plt.xlabel('Size (sq. ft.)')
plt.ylabel('Funding ($)')
plt.title('Linear Regression: Funding vs. Size of Aquarium')

# Save the plot as a PNG image
plt.savefig('../picture/Question 1.png')

# Show the plot
plt.show()