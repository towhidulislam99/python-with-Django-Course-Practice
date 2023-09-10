list_2d = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]

for row_index, row in enumerate(list_2d):
    for col_index, value in enumerate(row):
        print(f"Value: {value}, Row: {row_index}, Column: {col_index}")

print(list_2d)