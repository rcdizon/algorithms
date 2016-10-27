# Richard Dizon
# Programming Assignment 4
# CS 4102 - 10/14/16

# Loosely based from StackOverflow searches

import sys

print sys.argv[1]

longest = []
longest = longest.append([])

def find(grid, size):
    max_val = 0
    for i in range(0, size):
        for j in range(0, size):
            current = adj_check(i, j, size, grid)
            if (current > max_val):
                max_val = current
    return max_val

def adj_check(i, j, size, grid):
    global longest
    if (longest[i][j] == 0):
        max_val = 0
        for k in range(-1,2):
            for l in range (-1, 2):
                if i + k >= 0 and i + k < size and j + l >= 0 and j + l < size and grid[i + k][j + l] > grid[i][j] and (not (k == 0 and l == 0)): # Ensures indicies are within bounds
                    current = adj_check(i + k, j + l, size, grid)
                    if (current > max_val):
                        max_val = current
        longest[i][j] = max_val + 1
    return longest[i][j]

f = open(sys.argv[1], 'r') # Opens and reads file
test_cases = int(f.readline())
for i in range(0, test_cases):
    header = f.readline()
    arr = header.split()
    name = arr[0]
    size = int(arr[1])
    grid = []   # Placceholder for grid
    for j in range(0, size):
       line = f.readline().split() # Reads in each line, splits into separate string values
       for num in range(0, size):
            line[num] = int(line[num]) # Converts strings to ints
       grid.append(line) 
    longest = []
    for index in range(0, size): # Initialize 'longest' array
        new = []
        for index2 in range(0, size):
            new.append(0)
        longest.append(new)
    print name+":", find(grid, size)
f.close()
