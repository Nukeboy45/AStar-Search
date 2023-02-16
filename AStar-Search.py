# A* Search Algorithm
# Written by Nathan Weisskopf
# ITCS 3153 - Introduction to Artificial Intelligence
# 2023

import random

# Class for node object. Holds f, g, h, and parent node.

class Node:
    def __init__(self, p = None, coord = None):
        self.parent = p
        self.position = coord

        self.f = 0
        self.g = 0
        self.h = 0

    def __str__(self):
        return "f: ", self.f, "g: ", self.g, "h: ", self.h, "parent node: ", self.parent, "coordinate: ", self.coord

def astar(maze, start, goal):

    # Creating the Start and End Nodes
    startNode = Node(None, start)
    goalNode = Node(None, goal)

    # Open and closed list
    openList = []
    closedList = []

    openList.append(startNode)

    while len(openList) > 0:

        currNode = openList[0]
        currIndex = 0

        # Code for finding lowest F node in list
        for index, item in enumerate(openList):
            if item.f < currNode.f:
                currNode = item
                currIndex = index

        # Removing the current lowest F node from the openList, adding it to closedList
        openList.pop(currIndex)
        closedList.append(currNode)

        if currNode == goalNode:
            pathList = []

            pathNode = currNode
            while pathNode is not None:
                pathList.append(pathNode.position)
                pathNode = pathNode.parent

            return pathList[::-1]


def generateMaze(size):
    maze = []
    for x in range(size):
        row = []
        for y in range(size):
            if (random.randint(0, 10) == 0):
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

def generateCoord(size):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    return [x, y]


# Driver code
class main():
    size = 8

    # creating a random scenario
    maze = generateMaze(size)
    start = generateCoord(size)
    goal = generateCoord(size)

    maze[start[0]][start[1]] = 2
    maze[goal[0]][goal[1]] = 3
    for i in maze:
        print(i)

