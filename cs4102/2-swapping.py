# Richard Dizon
# rcd6ab
# CS4102 - HW2

import sys
f = open(sys.argv[1],"r")
data = f.readline()
orig_list = []
orig_total = 0
new_total = 0
arr = []
trailer = 0
min_trailer = 0

# Given valid input, O(n) to assemble data
def get_file_data():
    global orig_total, new_total, min_trailer
    line = data
    while line:
        # print line
        orig_list.append(line.rstrip())
        line = f.readline()
    for x in range(1, int(orig_list[0])+1):
        entry = orig_list[x].split()
        arr.append([int(entry[0]), int(entry[1])])
        orig_total += int(entry[0])
        new_total += int(entry[1])

# Implementation of bubblesort, average case O(n^2)
# Sort by change in room size, adapted from Skiena
def bubbleSort(arr):
    global min_trailer
    for num in range(len(arr)-1,0,-1):
        for i in range(num):
            if (arr[i][1] - arr[i][0]) > (arr[i+1][1] - arr[i+1][0]): # Basic swap
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            if (arr[i][1] - arr[i][0]) == (arr[i+1][1] - arr[i+1][0]):
                min_trailer = min(arr[i][0], arr[i+1][0])

def max(arr):
    nMax = arr[0][0]
    for i in range(0, len(arr)):
        if arr[i][0] > nMax:
            nMax = arr[i][0]
    return nMax


#### MAIN SCRIPT STARTS HERE ####

get_file_data()
size = orig_list[0]

# Test edge cases first
if orig_total > new_total:
    trailer = orig_total - new_total
elif orig_total == new_total:
    trailer = max(arr)

# Do sort
else:
    bubbleSort(arr)
    trailer = arr[len(arr)-1][0]
    # Apply greedy rule
    max_diff = arr[len(arr)-1][1] - arr[len(arr)-1][0]
    if max_diff == (arr[len(arr)-2][1] - arr[len(arr)-2][0]):
        trailer = min_trailer
    for i in range(0, len(arr)):
        if (arr[i][0] > max_diff) and (arr[i][0] > trailer):
            print "hit it"
            trailer = arr[i][0]

print trailer
f.close()
