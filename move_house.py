# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:12:14 2016

@author: Stephan
"""

import movement
import random
import free_space
import profit


'''
Moves a house to a new random position (within a range)
with a random range from -dx,dx and -dy,dy in meters
'''
def move_house(matrix, house, dx, dy, max_atempts = 100):
    # transfer meters to rigth index namly0.5 meters per bukket
    dx *= 2
    dy *= 2    
    
    # make copy of matrix for when move is incorrect
    new_matrix = []
    for i in range(len(matrix)):
        temp_list = []
        for j in range(len(matrix[0])):
            temp_list.append(matrix[i][j])
            
        new_matrix.append(temp_list)
    
    # remove house, so we can move it
    new_matrix = remove_house(new_matrix, house)
    
    if(house.get_house_type() == "maison"):
        house_maison = True
    else:
        house_maison = False
            
    for i in range(max_atempts):
        # get pos new position
        xpos = house.get_xpos()
        ypos = house.get_ypos()
        new_xpos = xpos + random.randint(-dx,dx)
        new_ypos = ypos + random.randint(-dy,dy)
        
        # check if you can move, if yes move, if no return old matrix
        if(movement.placement_check(house, new_matrix, new_xpos, new_ypos, move = True, maison = house_maison) == True):
            #print("house is moved")
            new_matrix = movement.place_house(house, new_matrix, new_xpos, new_ypos)
            return True, new_matrix[0]
#        else:
#            #print("house could not be moved")
    return False, matrix

'''
Remove the house
Decrease manditory free space by 1
'''
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
    return matrix
    
    
    