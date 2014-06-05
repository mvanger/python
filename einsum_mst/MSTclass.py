# -*- coding: utf-8 -*-
"""
Created on Wed May 28 21:41:15 2014

@author: Alex
"""

class MST:
    def __init__(self, numpyPoints):
        import numpy as np
        import math as m

        """
        generates list of random coordinates
        """
        self.numpyPoints = numpyPoints

        """
        generate list to store node information
        """
        self.nodes = []

        """
        generates node dictionaries from coordinates list and stores them
        """
        for i in range(len(numpyPoints)):
            node = {
                    'name':str(i),
                    'x': numpyPoints[i][0],
                    'y': numpyPoints[i][1],
                    'color':str(i)
                    }
            self.nodes.append(node)

        #print "nodes"
        #for x in self.nodes:
        #    print x
        #print "*****************************************************************"
        """
        generates list to store edge information
        """
        self.edges = []

        """
        generates edges dictionaries and stores them
        """
        for i in range(len(self.numpyPoints-1)):
            for j in range((i+1),len(self.numpyPoints)):
                x2 = (self.numpyPoints[i][0]-self.numpyPoints[j][0])**2
                y2 = (self.numpyPoints[i][1]-self.numpyPoints[j][1])**2
                dist = m.sqrt(x2+y2)
                edge = {
                        'name':str(i)+","+str(j),
                        'length':dist
                        }
                self.edges.append(edge)

        #print "edges"
        #for x in self.edges:
        #    print x

        #print "*****************************************************************"
        """
        generate list of colors - we can use this as stopping criteria
        """
        self.colors = []

        """
        and fill it
        """
        for x in self.nodes:
            self.colors.append(x['name'])

        """
        list to store MST
        """

        self.MST = []

        """
        call function to find minimum weight and discard edges that would cause cycles
        """
    def getColor(self, name):
        for x in self.nodes:
            if (x['name'] == name):
                return x['color']


    def findMinWeight(self):
        bestEdge = ""
        minDist = 0
        #    print "starting edge "+bestEdge['name']+" length "+str(minDist)

        removal = []
        """
        cycle through edges
        """
        for x in self.edges:
            #print x
            """
            get beginning and ending nodes
            """
            name = x['name'].split(",")
            start = name[0]
            stop = name[1]
            """
            get color of beginning and ending nodes
            """
            startColor = self.getColor(start)
            stopColor = self.getColor(stop)
            """
            if colors match, discard edge
            """
            #if(bestEdge != ""):
            #    print "consider "+x['name']+" length "+str(x['length'])+" against "+bestEdge['name']+" length "+str(bestEdge['length'])
            #    print "consider "+x['name']+" start "+ startColor+" stop "+stopColor


            if(startColor==stopColor):
            #    print "remove "+x['name']+" start "+startColor+" stop "+stopColor
                removal.append(x)
            elif(bestEdge == ""):
                bestEdge = x
                minDist = x['length']
            else:
                if (x['length']<minDist):
                    bestEdge = x
                    minDist = x['length']

            #print "bestEdge "+bestEdge['name']+" length "+str(bestEdge['length'])

        for x in removal:
            self.edges.remove(x)

        return bestEdge


        """
        used to look up the color of a given node
        """


        #step = 0

        """
        the loop continues untill all nodes are painted the same color
        """
    def getMST(self):
        while len(self.colors)>1:
            #step += 1

            #print "*****************************************************************"
            #print "step "+str(step)
            #print "*****************************************************************"

            #print self.colors

            #print "edges"
            #print self.edges

            bestEdge = self.findMinWeight()
            """
            get beginning and ending nodes
            """
            name = bestEdge['name'].split(",")
            start = name[0]
            stop = name[1]
            """
            get color of beginning and ending nodes
            """
            startColor = self.getColor(start)
            stopColor = self.getColor(stop)

            """
            find all nodes currently connected to stop node
            """
            connectedToStop = []
            for x in self.nodes:
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
            self.MST.append(bestEdge)

            self.edges.remove(bestEdge)
            """
            remove stop node color from colors list
            """
            self.colors.remove(stopColor)

        tree = []
        length = 0
        print self.MST
        for x in self.MST:
            length += x['length']
            tree.append(x['name'])

        answer =[]
        answer.append(length)
        answer.append(tree)
        return tuple(answer)



























