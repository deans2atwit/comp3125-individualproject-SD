import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the data, specifying the custom delimiter (dash with possible spaces around it)
data_path = 'data/Question 2.txt'
data = pd.read_csv(data_path, delimiter=r' - ', names=["Aquarium", "Type"])

# Strip leading/trailing spaces in both columns
data['Aquarium'] = data['Aquarium'].str.strip()
data['Type'] = data['Type'].str.strip()

# Print the first few rows to check the data
print(data.head())

# Check for any NaN values in the 'Type' column
print(f"NaN values in 'Type' column: {data['Type'].isna().sum()}")

# Count the number of For-Profit and Non-Profit
counts = data['Type'].value_counts()

# Print the counts to see the values
print("Counts for each category:\n", counts)

# If the counts look valid, create the pie chart
if not counts.empty:
    labels = counts.index
    sizes = counts.values
    colors = ['#ff9999', '#66b3ff']  # colors for each segment

    # Create an explode array with the same length as the number of segments
    explode = [0.1] * len(labels)  # Explode the first segment (for-profit) slightly, adjust if necessary

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('For-Profit vs Non-Profit Aquariums')
    plt.tight_layout()

    # Ensure the picture directory exists
    if not os.path.exists('picture'):
        os.makedirs('picture')

    # Save and display the figure
    picture_path = 'picture/Question 2.png'
    plt.savefig(picture_path, dpi=300)
    plt.show()

    print(f"Graph successfully saved to: {picture_path}")