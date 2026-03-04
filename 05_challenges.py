# Challenge One: Transpose
# Create a matrix with name `matrix` of the form:
# 1 2 3 4
# 5 6 7 8
matrix = [
    [1,2,3,4],
    [5,6,7,8]
]
# Create a new empty matrix called `m_transpose`.
m_transpose = []
# Using a for loop, populate `m_transpose` so that it is the transpose of `matrix`.
for i in range (len(matrix[0])):
    m_transpose.append([])
    for j in range(len(matrix)):
        m_transpose[i].append(matrix[j][i])
# Print `m_transpose` to see the changes.
    print(m_transpose[i])
print(matrix)
# Challenge Two: Matrix Multiplication
# Create a matrix called `multiplied` that is the result of multiplying `matrix` and `m_transpose`.
multiplied = []
# To do so, you may follow the steps:
# Step One: Identify resulting matrix rows & columns
# -- these two numbers will be the same and will equal to the rows of the first matrix and the columns of the second matrix
for i in range (len(matrix)):
    
# Step Two: Create a new `multiplied` empty matrix
# Step Three: Using for loops, populate the `multiplied` matrix