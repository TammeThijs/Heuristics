# -*- coding: utf-8 -*-
"""
Heuristieken: AmstelHaege
Name: housecheck.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

Check if houses can be placed
"""

def place_house(house, matrix, xpos, ypos):
    '''
    Places a the house on matrix, width xpos and ypos the bottom
    left coordinates
    '''
    
    # add their position
    house.change_xpos(xpos)
    house.change_ypos(ypos)
    
    # place house and house manditory free space
    for x in range((xpos - house.get_vrijstand()), (xpos + house.get_width() + house.get_vrijstand())):
        for y in range((ypos - house.get_vrijstand()), (ypos + house.get_heigth() + house.get_vrijstand())):
            if(x < xpos or x >= xpos + house.get_width() or y < ypos or y >= ypos + house.get_heigth()):
                matrix[x][y] += 1
            else:
                matrix[x][y] = house.get_color()
                
    return matrix, house
   

def placement_check(house, matrix, xpos, ypos, move = False, maison = True):
    '''
    Checks if the house can be placed on matrix. 
    With xpos and ypos the bottem left coordinates.
    
    returns true if house can be placed
    '''
    
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
    
    # Check the boundry of the house
    # bottem left
    if(matrix[xpos][ypos] != 0):
        return False
    if(matrix[xpos + house.get_width()][ypos] != 0):
        return False
    if(matrix[xpos][ypos + house.get_heigth()] != 0):
        return False
    if(matrix[xpos+ house.get_width()][ypos + house.get_heigth()] != 0):
        return False
    
    # if this is a move of a house and not a random placing
    if(move):
        # check for manditory vrijstand inside other house
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

        # if it is a maison you will need extra checks since it is longer
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
            
    # passed every test
    return True