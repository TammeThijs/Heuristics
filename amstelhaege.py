# -*- coding: utf-8 -*-
"""
Spyder Editor

Heuristieken: AmstelHaege

Autors: 
Stephan Kok 10627987, 
Stijn ... ...,
... ... ...


Last modified:
Stephan 04/04 21.13
"""

# import libary
import matplotlib.pyplot as plt
import pygame
import display
import display_debug
import movement
import free_space
import profit
import saved_state as ss
import numpy as np
import sys
sys.setrecursionlimit(10**6)

#grid variables
width = 300 
height = 320   

def main():

    # 1 for 20, 2 for 40, 3 for 60
    houses_to_place = 3

    showGaussian(houses_to_place, 1000, 2)

    return 

def showGaussian(houses, scope, desiredResult):

    savedResults = []

    for i in range(scope):
        result = 0        
        placed = True
        
        while(placed):
            try:
                matrix, houselist, water = movement.houses_to_place(houses, width, height)
                placed = False
            except:
                placed = True
            
        
        if(desiredResult == 1):
            result = free_space.calculate(matrix, houselist)
            
        else:
            free_space.calculate(matrix, houselist)
            result = profit.calculate(houselist)
            
        if(i % 10 == 0):
            print((i*100)/scope, "%")   

        savedResults.append(result)

    return plt.hist(savedResults, bins = 100)


main()