# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:12:14 2016

@author: Stephan
"""

import movement

def move_house(matrix, house):
    temp_matrix = matrix
    
    # remove house
    temp_matrix = remove_house(temp_matrix)
    
    # move house
    
    # get pos
    xpos = 0
    ypos = 0
    new_xpos = xpos + 1
    new_ypos = ypos + 1
    
    if(movement.can_house_be_placed_here(house, temp_matrix, new_xpos, new_ypos) == False):
        print("house is moved")
        temp_matrix = movement.place_house(house, temp_matrix, new_xpos, new_ypos)
        return temp_matrix
    else:
        print("house could not be moved")
        return matrix

def remove_house(matrix, house):
    # TODO GET POS OF HOUSE
    xpos = 0
    ypos = 0
    
    for x in range(house.getwidht()):
        for y in range(house.getheigth()):
            matrix[xpos + x][ypos + y] = 0
    
    return matrix