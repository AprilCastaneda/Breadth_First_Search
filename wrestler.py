#!/usr/bin/env python3
# AUTHOR:       April Castaneda
# DATE:         11.12.2019
# DESCRIPTION:  Suppose there are two types of professional wrestlers: 
#               “Babyfaces” (“good guys”) and “Heels” (“bad guys”). Between any pair of 
#               professional wrestlers, there may or may not be a rivalry. Suppose we have n 
#               wrestlers and we have a list of r pairs of rivalries.
#               Algorithm that determines whether it is possible to designate some of the 
#               wrestlers as Babyfaces and the remainder as Heels such that each rivalry is 
#               between a Babyface and a Heel.

# Import command line parser
import sys
filename = sys.argv[1]

import queue

# First, open file to read.
read_file = open(filename, 'r')

# Read each line in file and store in lines.
lines = []
for line in read_file:
    line = line.rstrip()
    lines.append(line)
read_file.close()

#print(lines)

# Create Wrestler class
class Wrestler:

    def __init__(self, name):
        self.name = name
        self.color = "White"     # White is no type
        self.type = "None"
        self.distance = 0
        self.rivals = []
    
    def add_adj_list(self, vertex):
        if vertex not in self.rivals:
            self.rivals.append(vertex)
            self.rivals.sort()  # Do I need to sort?

# Create Graph Class
class Graph:

    def __init__(self):
        self.vertices = {}
        self.possible = True
        self.source = True
        self.source_name = ""
        self.prior = None

    def add_wrestler(self, a_wrestler):
        if(self.source == True):
            a_wrestler.type = "Babyface"    # Set up Source wrestler
            self.source = False
            self.source_name = a_wrestler.name
        if(a_wrestler.name not in self.vertices):
            self.vertices[a_wrestler.name] = a_wrestler

    def add_rival(self, u, v):
        self.vertices[u].add_adj_list(v)
        self.vertices[v].add_adj_list(u)

    def get_wrestler(self, a_name):
        return vertices[a_name]

    def BFS(self):

        q = queue.Queue()
        first = self.vertices[self.source_name]
        first.color = "Gray"
        q.put(first)   # Put first wrestler in q

        while(q.empty() != True):
            u = q.get()         # Get wrestler out of q
            n = len(u.rivals)   # Go through rivals of u

            for i in range(0, n):
                v_name = u.rivals[i]
                v = self.vertices[v_name]
                if v.color == "White":
                    v.color = "Gray"
                    if u.type == "Babyface":
                        v.type = "Heel"
                    elif u.type == "Heel":
                        v.type = "Babyface"
                    elif u.type == "None":
                        u.type = "Babyface"
                        u.color = "Gray"
                    v.distance = u.distance + 1
                    v.prior = u
                    q.put(v)
                elif v.color == "Gray":
                    if v.type == "Babyface":
                        if u.type != "Heel":
                            self.possible = False
                    elif v.type == "Heel":
                        if u.type != "Babyface":
                            self.possible = False
                    #elif v.type == "Non"
                    #q.put(v)
                u.color = "Black"

            if(q.empty() == True): 
                for name in self.vertices:
                    leftover = self.vertices[name]
                    if leftover.color == "White":
                        #leftover.type = "Babyface"
                        #leftover.color = "Gray"
                        q.put(leftover)


# Store lines info
count = 0       # Counter
g = Graph()     # Create Graph

while count < len(lines):           # Go through all lines
    num_wrestlers = int(lines[count])    # First line - # of wrestlers
    count+=1

    for i in range(0, num_wrestlers):
        name = lines[count]
        some_wrestler = Wrestler(name)  # Create Wrestler with name
        g.add_wrestler(some_wrestler)   # Put wrestler in Graph
        count+=1
    
    num_rivalries = int(lines[count])
    count+=1

    for i in range(0, num_rivalries):
        rivals = lines[count].split()
        u_wrestler = rivals[0]
        v_wrestler = rivals[1]
        g.add_rival(u_wrestler, v_wrestler)
        count+=1

# Output
g.BFS()

# Print if possible
if(g.possible == True):
    print("Yes Possible")
else:
    print("Impossible")

# Get wrestlers
babyfaces = []
heels = []
for wrestlers in g.vertices:
    if g.vertices[wrestlers].type == "Babyface":
        babyfaces.append(g.vertices[wrestlers].name)
    else:
        heels.append(g.vertices[wrestlers].name)

babyfaces.sort()
heels.sort()

bfs = ""
hs = ""

for person in babyfaces:
    bfs = bfs + person + " "
for person in heels:
    hs = hs + person + " "

# Print wrestlers
if(g.possible == True):
    print("Babyfaces:", bfs)
    print("Heels:", hs)