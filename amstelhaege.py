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

def main():
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

    # create the matrix with first bin width and second bin heigth
    matrix = [[0 for i in range(height)] for j in range(width)]
    
    # Show info
    print("De eerste index is: " + str(len(matrix)))
    print("De tweede index is: " + str(len(matrix[0])))
        
    # All houses will get a unique house id
    houseid = 0
    # keep track of all houses
    houselist = []
    
    # place the houses
    for i in range(3):
        house = hc.Maison()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(5):
        house = hc.Bungalow()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(12):
        house = hc.Eengezinswoning()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    

    print(len(houselist))
    # 20 huizen
    #matrix = simple_algoritme(width, height, 3, 5, 12)
    

    
    '''
    plt.matshow(matrix, 
                origin = 'lower',   # Set 0,0 at bottom
                cmap=plt.cm.ocean)  # Set colors to ocean
    # Show color bar
    plt.colorbar()
    plt.grid()
    '''
    # Save on pc
    #plt.savefig("test.png")
    '''
    print(houselist)

    
    # get all positions to plot
    coordinates = []
    id_list = []
    for house in houselist:
        x = house.get_xpos()
        y = house.get_ypos()
        id_list.append(str(house.get_id()))
        coordinates.append((y, x))
        
    # plot the grid with their position          
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
    
    # caclculte vrijstand
    houselist = vrijstand.calculate_vrijstand(matrix, houselist)
    profit.append(calculate_profit.calculate(houselist))
    print("Initial profit = ", profit[0])
    
    print("LETS MOVE SOME HOUSES*************************************************")
    for j in range(20):
        print("run: ", j)
        for i in range(len(houselist)):
            matrix = move_house.move_house(matrix, houselist[i], 5, 5)
        
        # calculate profit of move
        houselist = vrijstand.calculate_vrijstand(matrix, houselist)
        profit.append(calculate_profit.calculate(houselist))
    

    # make a plot when finished
    coordinates = []
    id_list = []
    for house in houselist:
        x = house.get_xpos()
        y = house.get_ypos()
        id_list.append(str(house.get_id()))
        coordinates.append((y, x))
        
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


    houselist = vrijstand.calculate_vrijstand(matrix, houselist)
    profit.append(calculate_profit.calculate(houselist))
    '''
    
    
    
    display.build_grid(1)

    return calculate_profit.calculate(houselist)    
main()


random = []
for i in range(1):
    print("*****i*************################", i, i,i)
    random.append(main())
            
            
plt.hist(random, bins = 100)
main()