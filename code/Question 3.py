import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "Question 3.txt")
picture_path = os.path.join(script_dir, "..", "picture", "Question 3.png")

# Read and parse file properly
data = []
with open(data_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        country = " ".join(parts[:-1])
        percent = float(parts[-1].replace("%", ""))
        data.append([country, percent])

df = pd.DataFrame(data, columns=["Country", "Percent"])

# Sort descending
df = df.sort_values("Percent", ascending=False)

# Plot horizontal bar chart
plt.figure(figsize=(10, 12))
sns.barplot(data=df, y="Country", x="Percent", palette="viridis")
plt.title("Percentage of Global Marine Conservation Funding by Country")
plt.xlabel("Percent (%)")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(picture_path, dpi=300)
plt.show()

print(f"Graph successfully saved to: {picture_path}")