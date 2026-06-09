# ================================
# 01 - Python Fundamentals
# Author: Muhammad Fahad
# ================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy
numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)
print("Mean:", np.mean(numbers))

# Pandas
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": [85, 92, 78, 96]
}
df = pd.DataFrame(data)
print(df)

# Matplotlib
plt.bar(df["Name"], df["Score"], color="steelblue")
plt.title("Student Scores")
plt.savefig("student_scores.png")
plt.show()
print("Done!")