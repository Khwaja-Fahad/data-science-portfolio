# ================================================
# NumPy - 01: Array Basics
# Author: Muhammad Fahad
# Topic: Creating and understanding NumPy arrays
# ================================================

import numpy as np

# ── 1. Creating Arrays ──────────────────────────

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d) 

# ── 2. Array Attributes ─────────────────────────

print("Shape of 1D Array:", array_1d.shape)
print("Shape of 2D Array:", array_2d.shape)
print("Shape of 3D Array:", array_3d.shape)

print("Data type of 1D Array:", array_1d.dtype)
print("Data type of 2D Array:", array_2d.dtype)
print("Data type of 3D Array:", array_3d.dtype)

print("Number of dimensions in 1D Array:", array_1d.ndim)
print("Number of dimensions in 2D Array:", array_2d.ndim)
print("Number of dimensions in 3D Array:", array_3d.ndim)

#np.zeros, np.ones, np.empty, np.arange, np.linspace

range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print("Range Array:", range_array)

linspace_array = np.linspace(0, 10, 5)  # Start at 0, end at 10, generate 5 points
print("Linspace Array:", linspace_array)    

zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
print("Zeros Array:\n", zeros_array)

ones_array = np.ones((3, 2))  # 3 rows, 2 columns
print("Ones Array:\n", ones_array)  

empty_array = np.empty((2, 2))  # 2 rows, 2 columns (uninitialized)
print("Empty Array:\n", empty_array)