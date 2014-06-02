# -*- coding: utf-8 -*-
"""
Created on Wed May 28 21:41:15 2014

@author: Alex
"""
import numpy as np
import random as r
import math as m

"""
generates list of random coordinates
"""

numPoints = 10
points = []
for i in range (numPoints):
    x = (100-0)*r.random()
    y = (100-0)*r.random()
    coord = [x,y]
    points.append(coord)


"""
generate list to store node information
"""
nodes = []

"""
generates node dictionaries from coordinates list and stores them
"""
for i in range (numPoints):
    node = {
            'name':str(i),
            'x': points[i][0],
            'y': points[i][1],
            'color':str(i)
            }
    nodes.append(node)

print "nodes"
for x in nodes:
    print x
print "*****************************************************************"
"""
generates list to store edge information
"""
edges = []

"""
generates edges dictionaries and stores them
"""
for i in range(numPoints-1):
    for j in range((i+1),numPoints):
        x2 = (points[i][0]-points[j][0])**2
        y2 = (points[i][1]-points[j][1])**2
        dist = m.sqrt(x2+y2)
        edge = {
                'name':str(i)+","+str(j),
                'length':dist
                }
        edges.append(edge)

print "edges"
for x in edges:
    print x

print "*****************************************************************"
"""
generate list of colors - we can use this as stopping criteria
"""
colors = []

"""
and fill it
"""
for x in nodes:
    colors.append(x['name'])

"""
list to store MST
"""

MST = []

"""
call function to find minimum weight and discard edges that would cause cycles
"""
def findMinWeight():
    bestEdge = ""
    minDist = 0
    # print "starting edge "+bestEdge['name']+" length "+str(minDist)

    removal = []

    """
    cycle through edges
    """
    for x in edges:
        """
        get beginning and ending nodes
        """
        name = x['name'].split(",")
        start = name[0]
        stop = name[1]
        """
        get color of beginning and ending nodes
        """
        startColor = getColor(start)
        stopColor = getColor(stop)
        """
        if colors match, discard edge
        """
        if(startColor==stopColor):
            print "remove "+x['name']
            removal.append(x)
        elif(bestEdge == ""):
            bestEdge = x
            minDist = x['length']
        else:
            print "consider "+x['name']+" length "+str(x['length'])+" against "+bestEdge['name']+" length "+str(bestEdge['length'])
            if (x['length']<minDist):
                bestEdge = x
                minDist = x['length']

    print "bestEdge "+bestEdge['name']+" length "+str(bestEdge['length'])

    for x in removal:
        edges.remove(x)

    return bestEdge


"""
used to look up the color of a given node
"""
def getColor(name):
    for x in nodes:
        if (x['name'] == name):
            return x['color']

step = 0

"""
the loop continues untill all nodes are painted the same color
"""
while len(colors)>1:
    step += 1

    print "step "+str(step)
    print "*****************************************************************"

    bestEdge = findMinWeight()
    """
    get beginning and ending nodes
    """
    name = bestEdge['name'].split(",")
    start = name[0]
    stop = name[1]
    """
    get color of beginning and ending nodes
    """
    startColor = getColor(start)
    stopColor = getColor(stop)

    """
    find all nodes currently connected to stop node
    """
    connectedToStop = []
    for x in nodes:
        if (x['color']==stopColor):
            connectedToStop.append(x)
    """
    paint start node color on stop node and all nodes connected to it
    """
    for x in connectedToStop:
        x['color']=startColor

    """
    add edge to MST list and remove it from edges list
    """
    MST.append(bestEdge)
#    print "MST"
#    print MST

    edges.remove(bestEdge)
#    print "edges"
#    print edges
    """
    remove stop node color from colors list
    """
    colors.remove(stopColor)

length = 0
for x in MST:
    length += x['length']

print MST
print length
