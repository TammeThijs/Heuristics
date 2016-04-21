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
    for i in range(9):
        house = hc.Maison()
        matrix = movement.random_placing(matrix, house, width, height, houseid)
        anim_list.append(matrix)
        houselist.append(house)
        houseid += 1
    for i in range(15):
        house = hc.Bungalow()
        matrix = movement.random_placing(matrix, house, width, height, houseid)
        anim_list.append(matrix)
        houselist.append(house)
        houseid += 1
    for i in range(36):
        house = hc.Eengezinswoning()
        matrix = movement.random_placing(matrix, house, width, height, houseid)
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
    
    # Save on pc
    #plt.savefig("test.png")
    
    print(houselist)
    # Show image
    plt.show()    
    
    
    '''
    def update(i):
        mat.set_data(anim_list[i])
        return mat 
    
    fig, ax = plt.subplots()
    mat = ax.matshow(anim_list[i])
    plt.colorbar(mat)
    ani = animation.FuncAnimation(fig, update, frames = 10, interval=5000)
    plt.show()
    '''
main()
            
            
                    