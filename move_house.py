# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:12:14 2016

@author: Stephan
"""

import movement
import random

def move_house(matrix, houselist):
    
    house = houselist[0]    
    
    temp_matrix = []
    for i in range(len(matrix)):
        temp_list = []
        for j in range(len(matrix[0])):
            temp_list.append(matrix[i][j])
            
        temp_matrix.append(temp_list)
    
    
    # remove house
    temp_matrix = remove_house(temp_matrix, house)
    
    # move house
    
    # get pos
    xpos = house.get_xpos()
    ypos = house.get_ypos()
    new_xpos = xpos + random.randint(5,10)
    new_ypos = ypos + random.randint(5,10)
    
    if(movement.placement_check(house, temp_matrix, new_xpos, new_ypos) == True):
        print("house is moved")
        print(xpos, new_xpos, ypos, new_ypos)
        temp_matrix = movement.place_house(house, temp_matrix, new_xpos, new_ypos)
        return temp_matrix[0]
    else:
        print("house could not be moved")
        return matrix

def remove_house(matrix, house):
    # TODO GET POS OF HOUSE
    xpos = house.get_xpos()
    ypos = house.get_ypos()
    
    # remove house and take one from manditory free space            
    for x in range((xpos - house.get_vrijstand()), (xpos + house.get_width() + house.get_vrijstand())):
        for y in range((ypos - house.get_vrijstand()), (ypos + house.get_heigth() + house.get_vrijstand())):
            if(x < xpos or x >= xpos + house.get_width() or y < ypos or y >= ypos + house.get_heigth()):
                #print("x,y", x, y)
                matrix[x][y] -= 1
            else:
                matrix[x][y] = 0       
    print("house deleted")
    return matrix
    
    
    