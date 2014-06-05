# -*- coding: utf-8 -*-
"""
Created on Mon Jun 02 16:29:02 2014

@author: Alex
"""

"""
This sample code can be used to demonstrate the functionality of MSTclass
"""
import random as r
import numpy as n

numPoints = 10

"""
This is the nework used in the documentation example
points =    [[25.106436556848255, 33.11583380351523], 
            [62.809627435200156, 10.794141443593396], 
            [5.950316244837273, 91.90195242156311], 
            [17.373888408020342, 84.33391273846263], 
            [23.152762314339824, 81.87994509602639], 
            [35.49682924740668, 3.931852120332835], 
            [11.956289559499055, 32.01778863553745], 
            [74.2324704285982, 6.24233588940486], 
            [91.64620429001262, 67.95363178421961], 
            [14.261614190772764, 60.79800971430378]]
"""

points = []
for i in range (numPoints):
    x = (100-0)*r.random()
    y = (100-0)*r.random()
    coord = [x,y]
    points.append(coord)
    
    
print points
numpyPoints = n.array(points)

print "*************************************************"
print numpyPoints

print "*************************************************"

import MSTclass as m
network=m.MST(numpyPoints)
MST = network.getMST()
print MST