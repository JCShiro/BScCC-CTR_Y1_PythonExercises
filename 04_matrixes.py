# Exercise One
# Create a matrix called `matrix_a` that contains the following values:
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
matrix_a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
# Print the matrix.
print(matrix_a)

# Exercise Two
# Figure out the position of the number 6 in the above matrix
value = matrix_a[1][1]
# TO test you got it right, store it in a variable and print it
print(value)

# Exercise Three
# Print the number of rows and columns in `matrix_a`.
print(len(matrix_a), len(matrix_a[0]))
# Hint: Use what you learnt in the arrays section to figure it out!

# Exercise Four
# Create a matrix called `matrix_b` that contains the following values:
# 4  3  2  1
# 8  7  6  5
# 12 11 10 9
matrix_b = [
    [4,3,2,1],
    [8,7,6,5],
    [12,11,10,9]
]
print(matrix_b)
# Create a new matrix called `matrix_c` that is the result of adding `matrix_a` and `matrix_b` together.
matrix_c = [
    [(matrix_a[0][0])+(matrix_b[0][0]),(matrix_a[0][1])+(matrix_b[0][1]),(matrix_a[0][2])+(matrix_b[0][2]),(matrix_a[0][3])+(matrix_b[0][3])],
    [(matrix_a[1][0])+(matrix_b[1][0]),(matrix_a[1][1])+(matrix_b[1][1]),(matrix_a[1][2])+(matrix_b[1][2]),(matrix_a[1][3])+(matrix_b[1][3])],
    [(matrix_a[2][0])+(matrix_b[2][0]),(matrix_a[2][1])+(matrix_b[2][1]),(matrix_a[2][2])+(matrix_b[2][2]),(matrix_a[2][3])+(matrix_b[2][3])]
]

# matrix_c = [[],[],[]]

# for y in range (3):
#     for x in range(4):
#         matrix_c[y].append(matrix_a[y][x]+matrix_b[y][x])

# i.e., each cell of `matrix_c` should contain the added values in that cell for `matrix_a` and `matrix_b`
# Print `matrix_c` to see the result.
print(matrix_c)
