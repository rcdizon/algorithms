# Richard Dizon
# rcd6ab
# CS4102 - Programming HW3

import sys
import math

f = open(sys.argv[1],"r")
data = f.readline()
points_list = []
arr = []

def get_file_data():
    line = data
    while line:
        points_list.append(line.rstrip())
        line = f.readline()
    for x in range(1, int(points_list[0])+1):
        entry = points_list[x].split()
        arr.append([float(entry[0]), float(entry[1])])

def calc_dist(index1, index2, arr):
    lenx = arr[index1][0] - arr[index2][0]
    leny = arr[index1][1] - arr[index2][1]
    return math.sqrt((lenx**2)+(leny**2))

# Used this while testing to compare easy to
# find solution with more efficient algorithm
# and also used on each half
def brute_force(size, arr):
    min = calc_dist(0,1, arr)
    for i in range(0, size-1):
        for j in range(i, size):
            if i==j:
                continue
            if (calc_dist(i, j, arr) < min):
                min = calc_dist(i, j, arr)
    return min

# Implemented by mergesort, O(nlogn) run time, source Skiena
def horiz_sort(old_list):
    if len(old_list)>1:
        mid = len(old_list) // 2
        left_half = old_list[:mid]
        right_half = old_list[mid:]

        horiz_sort(left_half)
        horiz_sort(right_half)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                old_list[k]=left_half[i]
                i=i+1
            else:
                old_list[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            old_list[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            old_list[k]=right_half[j]
            j=j+1
            k=k+1
    return old_list

#### MAIN SCRIPT STARTS HERE ####
if data == "0" or data == "" or data == None:
    sys.exit()
elif data == "1":
    print "0"
    sys.exit()

get_file_data()
size = int(points_list[0])

horiz_sort(arr)

mid = 0
mid = size // 2
left_half = arr[:mid]
right_half = arr[mid:]
left_short = 0.0
right_short = 0.0
min_dist = 0.0

if len(left_half) > 1 and len(right_half) > 1:
    left_short = brute_force(len(left_half), left_half)
    right_short = brute_force(len(right_half), right_half)
    min_dist = min(left_short,right_short)
elif len(arr) == 3:
    min_dist = min(min(calc_dist(0, 1, arr), calc_dist(1, 2, arr)), calc_dist(1, 2, arr))
else:
    min_dist = calc_dist(0, 1, arr)
    

mid_point = arr[size // 2]

middle_section = []

for point in range(0, size):
    if (arr[point][0] >= mid_point[0]-min_dist and arr[point][0] <= mid_point[0]+min_dist):
        middle_section.append(arr[point])

mid_short = brute_force(len(middle_section), middle_section)

min_dist = min(min_dist, mid_short)
if min_dist <= 10000:
    print min_dist
else:
    print "infinity"

f.close()
