user_input = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Create an empty list to store modified values
modified_input = []

# Iterate over the rows of user_input
for row in user_input:
    modified_row = []  # Create an empty list for the modified row
    for element in row:
        if element > 9:
            c = element % 10
            modified_row.append(c)
        else:
            modified_row.append(element)
    modified_input.append(modified_row)

# Print the modified_input list and whether each row contains even or odd numbers
for row in modified_input:
    print(row)
    for element in row:
        if element % 2 == 0:
            print("Even")
        else:
            print("Odd")

row_sums =[]
for k in modified_input:
    row_sum = sum(k)
    row_sums.append(row_sum)
print(row_sums)
# for i, row_sum in enumerate(row_sums):
    # print(row_sum)
for k in modified_input:
    row_sum = sum(k)
    row_sums.append(row_sum)
    if row_sum % 2 == 0:
       print("Even")
    else:
       print("Odd")






    
 

       

      
