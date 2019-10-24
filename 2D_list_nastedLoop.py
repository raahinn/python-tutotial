
Number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


print(Number_grid [0][2])

# Using nested loop

# for num in Number_grid:
#    print(f'\n {num}')

for row in Number_grid:
    for columb in row:
        print(columb)