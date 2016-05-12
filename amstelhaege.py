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
WIDTH = 300 
HEIGTH = 320   

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
                matrix, houselist, water = movement.houses_to_place(houses, WIDTH, HEIGTH)
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


#main()

def run_with_pygame():
    '''
    First build a grid and then show every step with pygame.
    This will run slowely.
    For debugging purposes.
    '''
    # make sure you keep track of matrix witch will be the latest version
    global matrix
    
    # place houses
    not_placed = True
    # place 60 houses
    houses = 3

    while(not_placed):
        try:
            matrix, houselist, water = movement.houses_to_place(houses, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True    

    # calculate initial profit
    free_space.calculate(matrix, houselist)
    result = profit.calculate()
            
    # save findings
    state = ss.Saved_State(result, houselist, water)
    
    display_debug.build_grid(state, matrix)
run_with_pygame()    