# Richard Dizon
# rcd6ab
# CS4102 - Programming HW5

import sys
import math
from pprint import pprint

f = open(sys.argv[1],"r")
data = f.readline()
graph = {}
index_dict = {}
student_reg = []
course_list = []
n = 0
s = 0
t = 0

def get_file_data():
    global n
    line = data
    first_line = line.rstrip().split()

    r = int(first_line[0])
    c = int(first_line[1])
    n = int(first_line[2])

    if r == 0 and c == 0 and n == 0:
        sys.exit()

    line = f.readline()

    # Enumerate student_reg
    for i in range(0, r):
        entry = line.rstrip().split(" ", 1)
        student_reg.append(entry)
        line = f.readline()

    # Enumerate course_list
    for i in range(0, c):
        entry = line.rstrip().split(" ")
        course = entry[0] + " " + entry[1]
        course_list.append([ course, int(entry[2]) ])
        line = f.readline()

def construct_graph():
    for entry in student_reg:
        try:
            graph[entry[0]].append(entry[1])
        except:
            graph[entry[0]] = [entry[1]]

def construct_adj_matrix(students, courses):
    global graph, student_reg, course_list, index_dict, n, t

    # Initializing matrix, include two nodes for source + sink
    num_nodes = len(courses) + len(students) + 2
    matrix = [[0 for i in range(num_nodes)] for j in range(num_nodes)]
    t = num_nodes - 1

    # Make it easier to assign values in the matrix using dict
    index = 1
    for student in students:
        index_dict[student] = index
        index += 1
    for course in courses:
        index_dict[course] = index
        index += 1
    
    # Assigning true values for adjacency matrix
    for student in students:
        matrix[0][index_dict[student]] = n
    for student in student_reg:
        matrix[index_dict[student[0]]][index_dict[student[1]]] = 1 
    for course in course_list:
        matrix[index_dict[course[0]]][num_nodes - 1] = course[1]

    return matrix

def do_dfs(s, t):
    for i in range(t+1):
        if matrix[0][i]:
            return True
    return False

def dfs(s, t):
    global matrix
    visited = [False for i in range(t + 1)]
 
    stack = []
    path = []

    visited[s] = True

    stack.append(s)

    if (s==t):
        return minn

    min_val = sys.maxint

    while(stack != []):
        row = stack.pop()
        path.append(row)

        # Process
        if row == t:
            for i in range(len(path)-1):
                min_val = min(min_val, matrix[path[i]][path[i+1]])
            for i in range(len(path)-1):
                matrix[path[i]][path[i+1]] -= min_val
                matrix[path[i+1]][path[i]] += min_val
            return True
        
        # Add neighbors
        for i in range(0, t + 1):
            if matrix[row][i] != 0 and visited[i] == False:
                stack.append(i)                 
    return False


get_file_data()
construct_graph()

students = graph.keys()

courses = []
for course in course_list:
    courses.append(course[0])

matrix = construct_adj_matrix(students, courses)

# Test-case for students that register for too few classes
for student in students:
    count = 0
    for reg in student_reg:
        if reg[0] == student:
            count += 1
    if count < n:
        print "No"
        sys.exit()

while(do_dfs(s, t)):
    try:
        if not dfs(s, t):
            sys.exit()
    except:
        print "No"
        sys.exit()

max_flow = 0

for i in range(t + 1):
    max_flow += matrix[i][0]

if len(students)*n == max_flow:
    print "Yes"
else:
    print "No"

# Anything popped off the stack should be put onto a closed list
# Once 't' has been popped from the stack, we can trace-back
# and add 1 to the back-flow edges the do DFS again from this
# newly edited graph. Once 's' is empty, you've found max-flow.
# Sum the 's' column to get that max-flow value.
