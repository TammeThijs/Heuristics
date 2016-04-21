# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:04:16 2016

@author: Stephan
"""

import houseclass
import random

'''
Place houses random on the matrix
'''
def random_placing(matrix, house, width, height, houseid):
    # get random position
    randy = random.randint(0, height-1)
    randx = random.randint(0, width-1)
    
    # check if house can be placed
    if(can_house_be_placed_here(house, matrix, width, height, randx, randy) 
    == False):
        random_placing(matrix, house, width, height, houseid)
    else:
        matrix = place_house(house, matrix, randx, randy)
    
    return matrix

    
'''
Places a the house on matrix, width xpos and ypos the bottem
left coordinates
'''
def place_house(house, matrix, xpos, ypos):
    for x in range(house.getwidth()):
        for y in range(house.getheigth()):
            matrix[x+xpos][y+ypos] += house.color()
    return matrix
    
'''
Checks if the house can be placed on matrix. 
With xpos and ypos the bottem left coordinates.

returns true if house can be placed
'''
def can_house_be_placed_here(house, matrix, xpos, ypos):

    width = len(matrix)
    heigth = len(matrix[0])

    '''
    Check for outside grid.
    '''
    # right
    if(xpos + house.getwidth() + house.getvrijstand() >= width):
        return False
    # top
    if(ypos + house.getheigth() + house.getvrijstand() >= heigth):
        return False
    # left
    if( xpos - house.getvrijstand() < 0):
        return False
    # bottom
    if( ypos - house.getvrijstand() < 0):
        return False
    
    '''
    Check if a house is already placed.
    
    check by using: 4 spots
    '''
    # bottem left
    if(matrix[xpos][ypos] != 0):
        return False
    # top right
    if(matrix[xpos + house.getwidth()][ypos + house.getheigth()] != 0):
        return False   
    # bottem rigth
    if(matrix[xpos + house.getwidth()][ypos] != 0):
        return False  
    # top left
    if(matrix[xpos][ypos + house.getheigth()] != 0):
        return False  
    
    '''
    Check manditory free space.
    '''
    if(matrix[xpos - house.getvrijstand()][ypos - house.getvrijstand()] != 0):
        return False
    if(matrix[xpos + house.getvrijstand() + house.getwidth()][ypos - house.getvrijstand()] != 0):
        return False
    if(matrix[xpos + int(house.getwidth()/2)][ypos - house.getvrijstand()] != 0):
        return False
    if(matrix[xpos - house.getvrijstand()][ypos + house.getvrijstand() + house.getheigth()] != 0):
        return False
    if(matrix[xpos - house.getvrijstand()][ypos - int(house.getheigth()/2)] != 0):
        return False
    if(matrix[xpos + house.getvrijstand() + house.getwidth()][ypos + house.getvrijstand() + house.getheigth()] != 0):
        return False
    if(matrix[xpos + int(house.getwidth()/2)][ypos + house.getvrijstand() + house.getheigth()] != 0):
        return False
    if(matrix[xpos + house.getvrijstand() + house.getwidth()][ypos + int(house.getheigth()/2)] != 0):
        return False
    
    # passed every test so far
    return True    
    
