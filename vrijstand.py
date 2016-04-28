# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:55:38 2016

@author: Stephan
"""


'''
Calculate vrijstand for every house in house_list and add it to the class
'''
def calculate_vrijstand(matrix, house_list):
    
    # for every house calculate vrijstand
    for house in house_list:
        # find its vrijstand
        meters = find_vrijstand(matrix, house)
        
        # vrijstand to class
        house.change_extra_vrijstand(int(meters/2))
        
    # return the list
    return house_list
    
    
'''
Calculate the vrijstand of an house.
You start at the minimum reqruired vrijstand. The smallest house is 8 meters,
so you can search in a radius of 7 meters (14 steps) to check if there is a 
house it is impossible for within those 7 meters to be a house. So you can 
check the next 7 meters. 
If there is a house you binary search till you found it.
'''    
def find_vrijstand(matrix, house, steps = 14, back = False, prev = 0, taken = None, free = 0):
    
    # When a house have been found do binary search
    if(back == False):
        if(check_layer(matrix, house, steps)):
            # no house found. Increase steps
            newsteps = steps + 14
            return find_vrijstand(matrix, house, steps = newsteps, free = steps)
        else:
            # found a house, do binary search
            newsteps = int(steps - 7)
            return find_vrijstand(matrix, house, steps = newsteps, back = True, taken = steps, free = free)
    else:
        # binary search
        if(taken - free < 2):
            # found it
            return steps
        else:
            if(check_layer(matrix, house, steps)):
                # no house
                newsteps = int(steps + ((taken - steps) / 2))
                return find_vrijstand(matrix, house, steps = newsteps, back = True, free = steps, taken = taken)
            else:
                # found a house
                newsteps = int(free + (taken - steps) / 2)
                return find_vrijstand(matrix, house, steps = newsteps, back = True, taken = steps, free = free)
    
'''
Check the layer of a house

you have too check every 7 meters and every corner.

'''
def check_layer(matrix, house, layer):
    # intialize
    xpos = house.get_xpos()
    ypos = house.get_ypos()
    width = house.get_width()
    heigth = house.get_heigth()
    vrij = house.get_vrijstand() + layer

    # first check boundry because else you will get our of range error
    if(xpos - vrij < 0):
        return False
    if(ypos - vrij < 0):
        return False
    if(xpos + width + vrij >= len(matrix)):
        return False
    if(ypos + heigth + vrij >= len(matrix[0])):
        return False


    # house value is minimal 10 you wont want to find a house on vrijstand
    # because vrijstand can overlap
    # check every 7 meter

    # start left bottem go to right
    y = ypos - vrij
    for x in range(xpos - vrij , xpos + width + vrij, 7):
        if (matrix[x][y] > 9):
            return False
    
    # start right top go to left
    y = ypos + heigth + vrij
    for x in range(xpos + width + vrij, xpos - vrij, -7):
        if (matrix[x][y] > 9):
            return False
        
    # start left top go down
    x = xpos - vrij
    for y in range(ypos + heigth + vrij, ypos - vrij, -7):
        if (matrix[x][y] > 9):
            return False
    
    # start botem right go up
    x = xpos + width + vrij
    for y in range(ypos - vrij, ypos + heigth + vrij, 7):
        if (matrix[x][y] > 9):
            return False
        
    return True