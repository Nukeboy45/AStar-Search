# A* Search Algorithm
# Written by Nathan Weisskopf
# ITCS 3153 - Introduction to Artificial Intelligence
# 2023

import random
import math

# Class for node object. Holds f, g, h, and parent node.

class Node:
    def __init__(self, p = None, coord = None):
        self.parent = p
        self.position = coord

        self.f = 0
        self.g = 0
        self.h = 0

    def __str__(self):
        return("f: ", self.f, "g: ", self.g, "h: ", self.h, "parent node: ", self.parent, "coordinate: ", self.position)

def astar(maze, start, goal):

    # Creating the Start and End Nodes
    startNode = Node(None, start)
    goalNode = Node(None, goal)
    assignValues(startNode, startNode.position, goalNode.position)

    # Open and closed list
    openList = []
    closedList = []

    openList.append(startNode)

    i = 0
    while openList != [] and i < 50:

        i += 1
        currNode = openList[0]
        currIndex = 0

        # Choosing node with lowest f value and replacing current node & index with that node
        for index, item in enumerate(openList):
            if item.f < currNode.f:
                currNode = item
                currIndex = index

        openList.pop(currIndex)
        closedList.append(currNode)

        # If currNode equals goalNode, creates a path by tracing parents from goalNode. Once it reaches startNode,
        # returns the reversed list tracing from startNode to goalNode.
        if currNode.position[0] == goalNode.position[0] and currNode.position[1] == goalNode.position[1]:
            path = []
            pathNode = currNode
            while pathNode != None:
                path.append(pathNode)
                pathNode = pathNode.parent

            path.reverse()
            return path

        # Finding the child nodes of the current node
        childNodes = []
        for move in [(-1,-1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:

            childPosition = (currNode.position[0] + move[0], currNode.position[1] + move[1])

            if (childPosition[0] < 0 or childPosition[0] > len(maze) - 1 or childPosition[1] < 0 or childPosition[1] \
                    > len(maze) - 1):
                continue

            if maze[childPosition[1]][childPosition[0]] == 1:
                continue

            childNode = Node(currNode, childPosition)
            childNodes.append(childNode)

        for childNode in childNodes:
            for node in closedList:
                if node == childNode:
                    continue

            assignValues(childNode, childNode.position, goalNode.position)

            for node in openList:
                if node == childNode and childNode.g > node.g:
                    continue

            openList.append(childNode)

    if i == 50:
        emptylist = []
        print('entered')
        return emptylist

# Function for assinging g, h, and f values
def assignValues(node, nodePosition, goalPosition):
    if node.parent == None:
        node.g = 0
    else:
        node.g = node.parent.g + 1

    node.h = math.sqrt((nodePosition[1] - goalPosition[1]) ** 2 + \
                  (nodePosition[0] - goalPosition[0]) ** 2)
    node.f = node.g + node.h

# Generates a random board given integer size. Randomly fills out 10% of the board with unpathable nodes (1)
def generateMaze(size, density):
    maze = []
    for x in range(size):
        row = []
        for y in range(size):
            if (random.randint(0, 10) < density):
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

# Generates a random coordinate pair
def generateCoord(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return (x, y)

# Used to test pathfinding complexity. Given size and a given start coordinate, generates a goal node coordinate on the
# opposite side of the board
def generateComplexCoord(size, startPos):
    x = 0
    y = 0
    if startPos[0] < size / 2:
        x = random.randint(int(size / 2), size - 1)
    else:
        x = random.randint(0, int(size / 2))

    if startPos[1] < size / 2:
        y = random.randint(int(size / 2), size - 1)
    else:
        y = random.randint(0, int(size / 2))

    return (x, y)


# Utility function that takes a maze variable, start position, and end position, and prints the board
def printMaze(maze, startPos, endPos):

    maze[startPos[1]][startPos[0]] = 2
    maze[endPos[1]][endPos[0]] = 3

    for i in range(len(maze)):
        line = ""
        for y in maze[i]:
            if y == 0:
                line += "- "
            elif y == 1:
                line += "X "
            elif y == 2:
                line += "S "
            elif y == 3:
                line += "G "
            elif y == 4:
                line += "O "
        print(line)

# Driver code
class main():
    size = 15

    # creating a random scenario
    maze = generateMaze(size, 1)
    start = generateCoord(size)
    goal = generateComplexCoord(size, start)

    # prevents duplicate coordinates
    while start == goal:
        goal = generateCoord(size)

    printMaze(maze, start, goal)

    # Runs A-Star Search, to assign path list to path variable
    path = astar(maze, start, goal)
    print(path)
    if path == []:
        print("There is no path to be found!")
    else:
        for node in path:
            maze[node.position[1]][node.position[0]] = 4

    # Prints maze with finished path
    printMaze(maze, start, goal)

