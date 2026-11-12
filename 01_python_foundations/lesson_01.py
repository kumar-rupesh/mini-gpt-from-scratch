
# ==================================================
# MINI GPT FROM SCRATCH
# Lesson 01: Python Foundations - Scalars, Vectors & Matrices
# ==================================================

# --------------------------------------------------
# 1. Scalar
# --------------------------------------------------
# A scalar is a single numerical value.

number = 10


# --------------------------------------------------
# 2. Vector
# --------------------------------------------------
# A vector is a one-dimensional collection of values.

vector = [10, 20, 30]


# --------------------------------------------------
# 3. Matrix
# --------------------------------------------------
# A matrix is a two-dimensional collection of values
# arranged in rows and columns.

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


# --------------------------------------------------
# 4. Display Scalar, Vector and Matrix
# --------------------------------------------------

print("\n--- Scalar ---")
print("Scalar:", number)


print("\n--- Vector ---")
print("Vector:", vector)
print("Vector Length:", len(vector))


print("\n--- Matrix ---")
print("Matrix:")
print(matrix)


# --------------------------------------------------
# 5. Matrix Indexing
# --------------------------------------------------

print("\n--- Matrix Indexing ---")

# Access the first row
print("First Row:", matrix[0])

# Access the element at row 1, column 2
print("Element at [0][1]:", matrix[0][1])
