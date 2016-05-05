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
import houseclass as hc
import movement
import move_house
import vrijstand
import calculate_profit
import sys
sys.setrecursionlimit(10**6)              

def amstelhaege():
    '''
    Run all the code.
    This is the main function.

    '''
    # make global so it will remember when run is completed.
    global houselist
    global profit
    
    #define the heigth and width of the matrix
    width = 300
    height = 320
    
    # create a profit list to remember all profits
    profit = []
    
    # place the houses on the grid.
    placed = True
    # 1 for 20, 2 for 40, 3 for 60
    houses_to_place = 3
    while(placed):
        try:
            matrix, houselist = movement.houses_to_place(houses_to_place, width, height)
            placed = False
        except:
            print('error happend')
    
    
    display.build_grid(matrix, houselist)

    return calculate_profit.calculate(houselist)    
#main()


random = []
for i in range(1):
    print("begin")
    print("*****i*************################", i, i,i)
    random.append(amstelhaege())
            
            
#plt.hist(random, bins = 100)
#main()
            
            
'''
# a plot
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False)
    plt.imshow(matrix, cmap=plt.cm.ocean)
    for i in range(len(coordinates)):    
        ax.annotate(id_list[i], fontsize=20, xy=coordinates[i])
    plt.xlim(0,320)
    plt.ylim(0,300)
    plt.grid()
    plt.show()
    plt.close()
'''