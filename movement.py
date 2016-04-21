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
    if(placement_check(house, matrix, randx, randy) 
    == False):
        random_placing(matrix, house, width, height, houseid)
    else:
        matrix = place_house(house, matrix, randx, randy)
        print("PLACING WAS FOUND")
    
    return matrix

    
'''
Places a the house on matrix, width xpos and ypos the bottem
left coordinates
'''
def place_house(house, matrix, xpos, ypos):
    
    for x in range((xpos - house.get_vrijstand()), (xpos + house.get_width() + house.get_vrijstand())):
        for y in range((ypos - house.get_vrijstand()), (ypos + house.get_heigth() + house.get_vrijstand())):
            if(x < xpos or x >= xpos + house.get_width() or y < ypos or y >= ypos + house.get_heigth()):
                matrix[x][y] = 1
            else:
                matrix[x][y] = house.get_color() + 1
    return matrix 
   
   
'''
Checks if the house can be placed on matrix. 
With xpos and ypos the bottem left coordinates.

returns true if house can be placed
'''
def placement_check(house, matrix, xpos, ypos):

    width = len(matrix)
    heigth = len(matrix[0])
    
    #Checking if inside grid       
    
    # right
    if(xpos + house.get_width() + house.get_vrijstand() >= width):
        return False
    # top
    if(ypos + house.get_heigth() + house.get_vrijstand() >= heigth):
        return False
    # left
    if( xpos - house.get_vrijstand() < 0):
        return False
    # bottom
    if( ypos - house.get_vrijstand() < 0):
        return False
    
    #Validation done for all houses
        
    # bottem left
    if(matrix[xpos-house.get_vrijstand()][ypos-house.get_vrijstand()] != 0):
        return False
    # top right
    if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos + house.get_heigth() + house.get_vrijstand()] != 0):
        return False   
    # bottom right
    if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos-house.get_vrijstand()] != 0):
        return False  
    # top left
    if(matrix[xpos][ypos + house.get_heigth() + house.get_vrijstand()] != 0):
        return False 
    
    
    
    if(house.get_house_type() == "maison" or house.get_house_type() == "bungalow"):
        # Check middle
        if(matrix[xpos + int((house.get_width() + house.get_vrijstand())/2)][ypos + int((house.get_heigth() + house.get_vrijstand())/2)] != 0):
            return False 
        
        # middle bottom
        if(matrix[xpos + int((house.get_width() + house.get_vrijstand())/2)][ypos] != 0):
            return False    
            
        #middle left
        if(matrix[xpos][ypos + int((house.get_heigth() + house.get_vrijstand())/2)] != 0):
            return False 

        #middle right
        if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos + int((house.get_heigth() + house.get_vrijstand())/2)] != 0):
            return False     
            
        #top middle
        if(matrix[xpos + int((house.get_width() + house.get_vrijstand())/2)][ypos + house.get_heigth() + house.get_vrijstand()] != 0):
            return False
        
    
    # passed every test so far
    return True    
    
