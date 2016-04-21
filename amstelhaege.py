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

import matplotlib.pyplot as plt
import houseclass as hc
import movement
import matplotlib.animation as animation
import move_house

import sys
sys.setrecursionlimit(10**6)              

def main():
    '''
    Plot a figure of the grid    

    '''
    
    # height and width 150x160
    width = 300
    height = 320
    
    # make a matrix for if pixel is taken.
    # every pixel right now stands for 1 meter. So not very precise...
    matrix = [[0 for i in range(height)] for j in range(width)]
    
    # Show info
    #print(matrix)
    print("De eerste index is: " + str(len(matrix)))
    print("De tweede index is: " + str(len(matrix[0])))
        
    houseid = 0
    houselist = []
    anim_list = [matrix]
    # 20 huizen, 
    for i in range(1):
        house = hc.Maison()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        anim_list.append(matrix)
        houselist.append(house)
        houseid += 1
    for i in range(0):
        house = hc.Bungalow()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        anim_list.append(matrix)
        houselist.append(house)
        houseid += 1
    for i in range(20):
        house = hc.Eengezinswoning()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        anim_list.append(matrix)
        houselist.append(house)
        houseid += 1
    
    print(len(houselist))
    # 20 huizen
    #matrix = simple_algoritme(width, height, 3, 5, 12)
    
    
    plt.matshow(matrix, 
                origin = 'lower',   # Set 0,0 at bottom
                cmap=plt.cm.ocean)  # Set colors to ocean
    # Show color bar
    plt.colorbar()
    plt.grid()
    
    # Save on pc
    #plt.savefig("test.png")
    
    print(houselist)
    
     
    
    
    print("LETS MOVE SOME HOUSES*************************************************")
    move_house.move_house(matrix, houselist)
    move_house.move_house(matrix, houselist)
    move_house.move_house(matrix, houselist)
    
    plt.matshow(matrix, 
                origin = 'lower',   # Set 0,0 at bottom
                cmap=plt.cm.ocean)  # Set colors to ocean
    # Show color bar
    plt.colorbar()
    plt.grid()
    # Show image
    plt.show()       
    
    
main()
            
            
                    