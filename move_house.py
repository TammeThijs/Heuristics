# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:12:14 2016

@author: Stephan
"""

import movement
import numpy as np

def move_house(matrix, houselist):
    
    temp_matrix = np.copy(matrix)
    house = houselist[0]
    
    # remove house
    temp_matrix = remove_house(temp_matrix, house)
    
    # move house
    
    # get pos
    xpos = house.get_xpos()
    ypos = house.get_ypos()
    new_xpos = xpos + 10
    new_ypos = ypos + 10
    
    if(movement.placement_check(house, temp_matrix, new_xpos, new_ypos) == True):
        print("house is moved")
        print(new_xpos)
        print(new_ypos)
        temp_matrix = movement.place_house(house, temp_matrix, new_xpos, new_ypos)
        return temp_matrix
    else:
        print("house could not be moved")
        return matrix

def remove_house(matrix, house):
    # TODO GET POS OF HOUSE
    xpos = house.get_xpos()
    ypos = house.get_ypos()
    
    for x in range(house.get_width()):
        for y in range(house.get_heigth()):
            matrix[xpos + x][ypos + y] = 0
    
    return matrix