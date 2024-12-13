import random
import matplotlib.pyplot as plt
import pandas as pd

# Generate random numbers for a 5x5 grid (1 to 25)
numbers = random.sample(range(1, 26), 25)
grid = [numbers[i:i+5] for i in range(0, 25, 5)]

# Add BINGO headers
columns = ['B', 'I', 'N', 'G', 'O']
df = pd.DataFrame(grid, columns=columns)

# Plot the BINGO grid
fig, ax = plt.subplots(figsize=(8, 8))  # Adjust figure size for square cells
ax.axis('off')

# Draw table
table = plt.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1]  # Full table size within the figure
)

# Adjust table appearance
table.auto_set_font_size(False)
table.set_fontsize(14)

# Fix the width and height of cells to ensure squares
n_rows, n_cols = len(df), len(df.columns)
for i in range(n_rows + 1):  # Rows + 1 for header
    for j in range(n_cols):
        cell = table[(i, j)]
        cell.set_height(1 / n_rows)
        cell.set_width(1 / n_cols)
        cell.set_edgecolor('black')
        cell.set_linewidth(2)

        # Change color of header row (BINGO) to red
        if i == 0:  # Header row
            cell.set_text_props(color='red')
            cell.set_facecolor('white')

# Save the image
plt.savefig('bingo.png', dpi=300, bbox_inches='tight')
plt.close()

print("BINGO grid image saved as 'bingo.png' with red headers.")
