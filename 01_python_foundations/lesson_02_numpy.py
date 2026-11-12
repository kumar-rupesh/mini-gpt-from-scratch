
# ============================================
# MINI GPT FROM SCRATCH
# Lesson 02: NumPy Fundamentals
# ============================================

import numpy as np


# ============================================
# 01. NumPy Introduction
# ============================================

# Create a Python List
numbers = [10, 20, 30]

# Create a NumPy Array
numpy_arr = np.array([10, 20, 30])

# Perform multiplication
print("\n--- NumPy Introduction ---")

print("Python List:", numbers * 2)
print("NumPy Array:", numpy_arr * 2)


# ============================================
# 02. Array Dimensions and Shapes
# ============================================

# Create a 1D Array
arr_1d = np.array([10, 20, 30, 40])

# Create a 2D Array
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n--- Array Dimensions and Shapes ---")

print("1D Dimensions:", arr_1d.ndim)
print("1D Shape:", arr_1d.shape)

print("2D Dimensions:", arr_2d.ndim)
print("2D Shape:", arr_2d.shape)


# ============================================
# 03. NumPy Array Properties
# ============================================

properties_arr = np.array([10, 20, 30])

print("\n--- Array Properties ---")

print("Dimensions:", properties_arr.ndim)
print("Shape:", properties_arr.shape)
print("Total Elements:", properties_arr.size)
print("Data Type:", properties_arr.dtype)
print("Item Size (bytes):", properties_arr.itemsize)


# ============================================
# 04. 1D Array Indexing and Slicing
# ============================================

arr_1d = np.array([5, 10, 15, 20, 25, 30])

print("\n--- 1D Indexing and Slicing ---")

# Positive Indexing
print("1D Indexing:", arr_1d[3])

# Negative Indexing
print("Negative Indexing:", arr_1d[-2])

# Slicing
print("1D Slicing:", arr_1d[1:4])


# ============================================
# 05. 2D Array Indexing and Slicing
# ============================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n--- 2D Indexing and Slicing ---")

# 2D Indexing
print("2D Indexing:", matrix[1, 1])

# 2D Slicing
print("2D Slicing:")
print(matrix[1:, 0:])


# ============================================
# 06. Array Reshaping
# ============================================

reshape_arr = np.array([
    1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13, 14, 15, 16
])

# Reshape into 2D Array
reshaped_arr = reshape_arr.reshape(-1, 8)

print("\n--- Array Reshaping ---")

print("Original Shape:", reshape_arr.shape)
print("Reshaped Array:")
print(reshaped_arr)
print("New Shape:", reshaped_arr.shape)


# ============================================
# 07. Assignment (Same Array Reference)
# ============================================

original_arr = np.array([10, 20, 30, 40])

new_arr = original_arr

new_arr[0] = 100

print("\n--- Assignment Example ---")

print("Original:", original_arr)
print("New:", new_arr)

# ============================================
# 08. NumPy Copy
# ============================================

original_arr = np.array([10, 20, 30, 40])

copy_arr = original_arr.copy()

copy_arr[0] = 100

print("\n--- NumPy Copy ---")

print("Original:", original_arr)
print("Copy:", copy_arr)

# ============================================
# 08. NumPy View
# ============================================

original_arr = np.array([15, 20, 25, 30])

view_arr = original_arr.view()

view_arr[0] = 50

print("\n--- NumPy View ---")

print("Original:", original_arr)
print("View:",view_arr)

original_arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

view_arr = original_arr.view()

view_arr = view_arr.reshape(3, 2)

print("Original Shape:", original_arr.shape)
print("View Shape:", view_arr.shape)

# ============================================
# 10. NumPy View: Data Sharing and Shape
# ============================================

original_arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

view_arr = original_arr.view()

# Change View Shape
view_arr = view_arr.reshape(3, 2)

print("\n--- NumPy View: Shape Experiment ---")

print("Original Shape:", original_arr.shape)
print("View Shape:", view_arr.shape)

# Change View Data
view_arr[0, 0] = 999

print("\n--- NumPy View: Data Sharing ---")

print("Original:")
print(original_arr)

print("View:")
print(view_arr)

# ============================================
# 11. NumPy Broadcasting
# ============================================

broadcast_arr = np.array([10, 20, 30])

print("\n--- NumPy Broadcasting ---")

print("Addition:", broadcast_arr + 5)
print("Subtraction:", broadcast_arr - 5)
print("Multiplication:", broadcast_arr * 2)
print("Division:", broadcast_arr / 10)

# Matrix Broadcasting
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

result = matrix + b

print("\n--- Matrix Broadcasting ---")
print(result)

# ============================================
# 12. Mathematical and Statistical Functions
# ============================================

numbers = np.array([10, 20, 30, 40, 50])

print("\n--- Mathematical Functions ---")

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))

# ============================================
# 13. Standard Deviation
# ============================================

a = np.array([10, 10, 10, 10])
b = np.array([5, 10, 15, 10])

print("\n--- Standard Deviation ---")
print("SD of A:", np.std(a))
print("SD of B:", np.std(b))

# ============================================
# 14. Statistical Functions with Axis
# ============================================

matrix = np.array([[10, 20, 30],
                   [40, 50, 60]
                   ])

print("\n--- Statistical Functions with Axis ---")

print("Column Sum:", np.sum(matrix, axis=0))
print("Row Sum:", np.sum(matrix, axis=1))

print("Column Min:", np.min(matrix, axis=0))
print("Row Min:", np.min(matrix, axis=1))

print("Column Max:", np.max(matrix, axis=0))
print("Row Max:", np.max(matrix, axis=1))

print("Column Mean:", np.mean(matrix, axis=0))
print("Row Mean:", np.mean(matrix, axis=1))

print("Column Std:", np.std(matrix, axis=0))
print("Row Std:", np.std(matrix, axis=1))
