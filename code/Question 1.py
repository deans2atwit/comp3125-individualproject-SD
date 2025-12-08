import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/Question 1.csv')

# Strip any extra spaces from column names
data.columns = data.columns.str.strip()

# Convert 'Size' and 'Funding' to numeric
data['Funding'] = pd.to_numeric(data['Funding'], errors='coerce')
data['Size'] = pd.to_numeric(data['Size'], errors='coerce')
data['ES'] = pd.to_numeric(data['ES'], errors='coerce')

# Drop rows with missing values
data.dropna(subset=['Funding', 'Size', 'ES'], inplace=True)

# Handle the categorical 'Location' column using One-Hot Encoding
location_encoded = pd.get_dummies(data['Location'], drop_first=True)
data = pd.concat([data, location_encoded], axis=1)

g = sns.FacetGrid(data, col="Location", col_wrap=4, height=4)
g.map(sns.regplot, "Size", "ES", scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.savefig('picture/Question 1_FacetGrid.png') 
plt.show()

sns.lmplot(x="Size", y="ES", data=data, aspect=1.5, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title("Linear Regression: Size vs Endangered Species")
plt.savefig('picture/Question 1_Size_ES.png') 
plt.show()

sns.lmplot(x="Funding", y="ES", data=data, aspect=1.5, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title("Linear Regression: Funding vs Endangered Species")
plt.savefig('picture/Question 1_Funding_ES.png') 
plt.show()