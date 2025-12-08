import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (assuming your script is in the 'code' folder and data is in 'data' folder)
data = pd.read_csv('data/Question 1.csv')  # Adjust path for relative directory

# Strip any extra spaces from column names
data.columns = data.columns.str.strip()

# Convert 'Size' and 'Funding' to numeric (in case they aren't already)
data['Funding'] = pd.to_numeric(data['Funding'], errors='coerce')
data['Size'] = pd.to_numeric(data['Size'], errors='coerce')
data['ES'] = pd.to_numeric(data['ES'], errors='coerce')

# Drop rows with missing values
data.dropna(subset=['Funding', 'Size', 'ES'], inplace=True)

# Handle the categorical 'Location' column using One-Hot Encoding
location_encoded = pd.get_dummies(data['Location'], drop_first=True)
data = pd.concat([data, location_encoded], axis=1)

# Create a pairplot to visualize relationships between all predictors and the target
sns.pairplot(data[['Size', 'Funding', 'ES'] + location_encoded.columns.tolist()])
plt.savefig('../picture/Question 1_pairplot.png')  # Save the plot in the picture folder
plt.show()

# Alternatively, use Seaborn's FacetGrid to create subplots for different locations
g = sns.FacetGrid(data, col="Location", col_wrap=4, height=4)
g.map(sns.regplot, "Size", "ES", scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.savefig('../picture/Question 1_FacetGrid.png')  # Save the plot in the picture folder
plt.show()

# You can also use lmplot with a single predictor
sns.lmplot(x="Size", y="ES", data=data, aspect=1.5, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title("Linear Regression: Size vs Endangered Species")
plt.savefig('../picture/Question 1_Size_ES.png')  # Save the plot in the picture folder
plt.show()

sns.lmplot(x="Funding", y="ES", data=data, aspect=1.5, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title("Linear Regression: Funding vs Endangered Species")
plt.savefig('../picture/Question 1_Funding_ES.png')  # Save the plot in the picture folder
plt.show()