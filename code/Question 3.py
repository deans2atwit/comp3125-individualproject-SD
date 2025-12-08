import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
print(os.path.exists("../data/Question 3.txt"))

# Read the dataset
df = pd.read_csv(
    "../data/Question 3.txt",
    sep="\t",
    header=None,
    names=["Country", "Percent"],
    dtype=str
)

# Clean percent column
df["Percent"] = df["Percent"].str.replace("%", "", regex=False).astype(float)

# Sort for nicer plotting
df = df.sort_values("Percent", ascending=False)

# Create the bar plot
plt.figure(figsize=(10, 12))
sns.barplot(data=df, y="Country", x="Percent", palette="viridis")
plt.title("Percentage of Global Marine Conservation Funding by Country")
plt.xlabel("Percent (%)")
plt.ylabel("Country")
plt.tight_layout()

# Save the figure to Picture folder
output_path = "../Picture/marine_conservation_by_country.png"
plt.savefig(output_path, dpi=300)  # High-resolution
plt.show()

# Confirm the file was saved
if os.path.exists(output_path):
    print(f"Graph successfully saved to: {output_path}")
else:
    print("Failed to save the graph.")