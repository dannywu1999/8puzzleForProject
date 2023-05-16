import json
q = []  # string store ucs-bfs
d = {}  # <string, int>  distance from begining
p = {}  # <string, string> (son -> father)  Store parent node

#########  A* with the Misplaced Tile heuristic
def heu(state):#The function h(state) calculates the number of misplaced tiles in the current state compared to the goal state.
    # calculate the misplaced tiles heuristic
    misplaced_tiles = 0
    for i in range(9):
        if state[i] != '0' and state[i] != end[i]:
            misplaced_tiles += 1
    return misplaced_tiles

def A_starH(start):
    q.append(start)
    d[start] = 0
    p[start] = 0
    # [left right up down]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        q.sort(key=lambda x: d[x] + heu(x)) # sort the queue based on f = g + h
        t = q.pop(0)
        distance = d[t]
        if t == end:
            return distance
        k = t.find('0')
        x = int(k / 3)
        y = k % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a < 3 and b >= 0 and b < 3:
                father = t
                tlist = list(t)
                tlist[k], tlist[a * 3 + b] = tlist[a * 3 + b], t[k]
                t = ''.join(tlist)
                if not p.__contains__(t):
                    p[t] = father
                if not d.__contains__(t):
                    d[t] = distance + 1
                    q.append(t)
                tlist = list(t)
                tlist[k], tlist[a * 3 + b] = tlist[a * 3 + b], tlist[k]
                t = ''.join(tlist)
    return -1

############  A* with the Misplaced Tile heuristic


##########Uniform Cost Search
def ucs(start):
    q.append(start)
    d[start] = 0
    p[start] = 0
    # [left right up down]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        t = q[0]
        q.pop(0)
        distance = d[t]
        if t == end:# when queue is not empty, calculate the distance from original place using state t
            return distance
        k = t.find('0')
        x = int(k / 3)
        y = k % 3
        
        for i in range(4):# this for loop is the search part. When we play this game, we will try to move a number from a block to 
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a < 3 and b >= 0 and b < 3:
                father = t
                tlist = list(t)
                tlist[k], tlist[a * 3 + b] = tlist[a * 3 + b], t[k]
                t = ''.join(tlist)
                if not p.__contains__(t):
                    p[t] = father
                if not d.__contains__(t):
                    d[t] = distance + 1
                    q.append(t)
                tlist = list(t)
                tlist[k], tlist[a * 3 + b] = tlist[a * 3 + b], tlist[k]
                t = ''.join(tlist)
    return -1
##########Uniform Cost Search


############################A* with the Manhattan Distance heuristic
def h(state):
    # calculate the Manhattan distance heuristic
    md = 0
    for i in range(9):
        if state[i] != '0':
            j = int(state[i]) - 1
            md += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return md

def A_starM(start):
    q.append(start)
    d[start] = 0
    p[start] = 0
    # [left right up down]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        q.sort(key=lambda x: d[x] + h(x)) # sort the queue based on f = g + h
        t = q.pop(0)
        distance = d[t]
        if t == end:
            return distance
        k = t.find('0')
        x = int(k / 3)
        y = k % 3
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a < 3 and b >= 0 and b < 3:
                father = t
                tlist = list(t)
                tlist[k], tlist[a * 3 + b] = tlist[a * 3 + b], t[k]
                t = ''.join(tlist)
                if not p.__contains__(t):
                    p[t] = father
                if not d.__contains__(t):
                    d[t] = distance + 1
                    q.append(t)
                tlist = list(t)
                tlist[k], tlist[a * 3 + b] = tlist[a * 3 + b], tlist[k]
                t = ''.join(tlist)
    return -1
#################################A* with the Manhattan Distance heuristic


# take input for each row of the matrix
input_str1 = input("Enter the first row of the matrix in the format '1 2 3': ")
input_str2 = input("Enter the second row of the matrix in the format '1 2 3': ")
input_str3 = input("Enter the third row of the matrix in the format '1 2 3': ")

# split each input string into a list of numbers
row1 = [int(num) for num in input_str1.split()]
row2 = [int(num) for num in input_str2.split()]
row3 = [int(num) for num in input_str3.split()]

# combine the rows into a single 3x3 matrix
matrix = [row1, row2, row3]
matrix_str = ""
for row in matrix:#transfer a matrix to str
    for elem in row:
        matrix_str += str(elem)
# print the matrix
print("Matrix:",matrix)
count=0
start = matrix_str #input('Please input raw data:')
end = '123456780'### goal, which is our target
Input=0
#Input = input("1 is Uniform Cost Search///2 is A* with the Misplaced Tile heuristic.///3 is A* with the Manhattan Distance heuristic: ")

res=0
    #if(Input==1):
#res = ucs(start) #Uniform Cost Search
    #if(Input==2):
#res = A_starH(start)#A* with the Misplaced Tile heuristic.
    #if(Input==3):
res= A_starM(start)#A* with the Manhattan Distance heuristic

if(res!=-1):    
    print('Shortest Steps:' + str(res))
    print('')
    formal = p[end] #set formal tothe parent of the goal state
    path = [] #Create an empty list to store path
    path.append(end) # Add the final state to the path
    while formal: # if the current state is not at starting stete, do it
        path.append(formal) 
        formal = p[formal]# update

    path.reverse()#Reverse the order of the path, so that it goes from the starting state to the end state.
    
    #output the matrix
    for i in range(res + 1):
        for a in range(3):
            print(path[i][a], end = ' ')
        print('')
        for a in range(3):
            print(path[i][a + 3], end = ' ')
        print('')
        for a in range(3):
            print(path[i][a + 6], end = ' ')
        print('')
        print('')
        
    print('Goal state!')
    print('Number of nodes expanded:',len(p))
else:
    print("It is not solvable !")