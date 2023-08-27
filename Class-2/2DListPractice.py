matrix =[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]

]
print(matrix)
print(matrix[1])
print(matrix[2][0])

for row in matrix:
    for item in row:
        print(item)

addition = matrix[0][1] + matrix[0][2]
print(addition)

add = matrix[2][1]  + matrix[2][2]
print(add)