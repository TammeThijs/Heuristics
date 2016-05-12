# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:04:16 2016

@author: Stephan
"""

import random
import houseclass as hc
import waterclass as wc
import numpy as np



'''
Call functions to place houses
'''
def houses_to_place(houses, width, height):
    # make a matrix for if pixel is taken.
    matrix = [[0 for i in range(height)] for j in range(width)] 
    
    matrix, water = wc.place_water(matrix)    
    
    houselist = []
    
    houseid = 0
    for i in range(3*houses):
        house = hc.Maison()
        house.change_id(houseid)
        matrix, house = random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(5*houses):
        house = hc.Bungalow()
        house.change_id(houseid)
        matrix, house = random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(12*houses):
        house = hc.Eengezinswoning()
        house.change_id(houseid)
        matrix, house = random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    return matrix, houselist, water

'''
Place houses random on the matrix
'''
def random_placing(matrix, house, width, height, houseid, iteration = 0):
#    
#    iteration += 1    
#    if (iteration > 1000):
#        #print("More then ", iteration, " iteration. Try again")
#        raise("error iteration")
    
    # get random position
    randy = random.randint(0, height-1)
    randx = random.randint(0, width-1)       
    
    # check if house can be placed
    if(placement_check(house, matrix, randx, randy) 
    == False):
        random_placing(matrix, house, width, height, houseid, iteration = iteration)
    else:
        matrix, house = place_house(house, matrix, randx, randy)
    
    return matrix, house

    
'''
Places a the house on matrix, width xpos and ypos the bottem
left coordinates
'''
def place_house(house, matrix, xpos, ypos):
    
    house.change_xpos(xpos)
    house.change_ypos(ypos)
    
    for x in range((xpos - house.get_vrijstand()), (xpos + house.get_width() + house.get_vrijstand())):
        for y in range((ypos - house.get_vrijstand()), (ypos + house.get_heigth() + house.get_vrijstand())):
            if(x < xpos or x >= xpos + house.get_width() or y < ypos or y >= ypos + house.get_heigth()):
                matrix[x][y] += 1
            else:
                matrix[x][y] = house.get_color()
    return matrix, house
   
   
'''
Checks if the house can be placed on matrix. 
With xpos and ypos the bottem left coordinates.

returns true if house can be placed
'''
def placement_check(house, matrix, xpos, ypos, move = False, maison = True):

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
    
    # Check if the house can be placed. 
    # bottem left
    if(matrix[xpos][ypos] != 0):
        return False
    if(matrix[xpos + house.get_width()][ypos] != 0):
        return False
    if(matrix[xpos][ypos + house.get_heigth()] != 0):
        return False
    if(matrix[xpos+ house.get_width()][ypos + house.get_heigth()] != 0):
        return False
    
    if(move):
        # check for vrijstand
        # bot left
        if(matrix[xpos - house.get_vrijstand()][ypos - house.get_vrijstand()] > 9):
            return False
        #bot right
        if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos - house.get_vrijstand()] > 9):
            return False
        # top left
        if(matrix[xpos - house.get_vrijstand()][ypos + house.get_heigth() + house.get_vrijstand()] > 9):
            return False    
        # top rigth
        if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos + house.get_heigth() + house.get_vrijstand()] > 9):
            return False

        if(maison):
            # middle between
            # bot
            if(matrix[xpos +  4][ypos - house.get_vrijstand()] > 9):
                return False
            # right
            if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos + 4] > 9):
                return False
            # top
            if(matrix[xpos + 4][ypos + house.get_heigth() + house.get_vrijstand()] > 9):
                return False    
            # left
            if(matrix[xpos - house.get_vrijstand()][ypos + 4] > 9):
                return False
            # bot
            if(matrix[xpos + 18][ypos - house.get_vrijstand()] > 9):
                return False
            # right
            if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos + 18] > 9):
                return False
            # top
            if(matrix[xpos + 18][ypos + house.get_heigth() + house.get_vrijstand()] > 9):
                return False    
            # left
            if(matrix[xpos - house.get_vrijstand()][ypos + 18] > 9):
                return False                
                
        else:
            # bot
            if(matrix[xpos +  int(house.get_width()/2)][ypos - house.get_vrijstand()] > 9):
                return False
            # right
            if(matrix[xpos + house.get_width() + house.get_vrijstand()][ypos + int(house.get_heigth()/2)] > 9):
                return False
            # top
            if(matrix[xpos + int(house.get_width()/2)][ypos + house.get_heigth() + house.get_vrijstand()] > 9):
                return False    
            # left
            if(matrix[xpos - house.get_vrijstand()][ypos + int(house.get_heigth()/2)] > 9):
                return False
            
    
        
    # passed every test so far
    return True    
    
