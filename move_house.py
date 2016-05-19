# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:12:14 2016

@author: Stephan
"""

import movement
import random

def move_house(matrix, house, dx, dy, max_atempts = 100):
    '''
    Moves a house to a new random position (within a range)
    with a random range from -dx,dx and -dy,dy in meters
    '''
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
    
    # get house type
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

def move_bulk(matrix, houselist, dx, dy , bulk, max_attempts = 5000):
    '''
    Move multiple houses at once.
    
    TODO doest work yet
    '''
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

    # remove bulk houses
    houses = random.sample(range(0,len(houselist) -1), bulk)
  #  print("houses to remove " + str(houses))
    for x in houses:
        new_matrix = remove_house(new_matrix, houselist[x])
    
    for x in houses:
        house = houselist[x]
        if(house.get_house_type() == "maison"):
            house_maison = True
        else:
            house_maison = False
        placed, new_matrix = try_to_place(matrix, new_matrix, house, max_attempts, dx, dy, house_maison)
        
        if(placed == False):
            #print("failed")
            return False, matrix
    return True, new_matrix
        
def try_to_place(matrix,new_matrix, house, max_attemps, dx, dy, house_maison):
    '''
    Method for bulk.
    '''
    for i in range(max_attemps):
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

   
def remove_house(matrix, house):
    '''
    Remove the house
    Decrease manditory free space by 1
    '''
    # get house to remove
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
    
def move_water(matrix, water, dx, dy, max_atempts = 1000):
    '''
    This function will move water. It will try max_atempts times, default 1000
    '''
    

    # transfer meters to rigth index namely0.5 meters per bukket
    dx *= 2
    dy *= 2    

    # make copy of matrix for when move is incorrect
    new_matrix = []
    for i in range(len(matrix)):
        temp_list = []
        for j in range(len(matrix[0])):
            temp_list.append(matrix[i][j])
            
        new_matrix.append(temp_list)
    
    # remove water, so we can move it
    new_matrix = remove_water(new_matrix, water)

    xpos = water.get_xpos()
    ypos = water.get_ypos()

    # Try to place water max_atemps times
    for i in range(max_atempts):
        new_xpos = xpos + random.randint(-dx,dx)
        new_ypos = ypos + random.randint(-dy,dy)
        
        print("old"  + str(xpos) +" " +  str(ypos))
        print("new"  + str(new_xpos) +" " +  str(new_ypos))
        
        # check if you can move, if yes move, if no return old matrix
        if(water_placement_check(new_matrix, water, new_xpos, new_ypos)):
            new_matrix = replace_water(new_matrix, water, new_xpos, new_ypos)
            print("TRUEEE" + str(new_xpos) + str(new_ypos))
            return True, new_matrix
            
    # failed to move water max_atemps times            
    return False, matrix
    
def remove_water(matrix, water):
    '''
    Remove water from matrix
    '''
    xpos = water.get_xpos()
    ypos = water.get_ypos()
 
    # remove water          
    for x in range(xpos, xpos + water.get_width()):
        for y in range(ypos, ypos + water.get_heigth()):
            matrix[x][y] -= 5      
    return matrix    
    
    
def water_placement_check(matrix, water, new_xpos, new_ypos):
    '''
    Check if water can be placed here.
    '''
    width = water.get_width()
    heigth = water.get_heigth()
    
    print("CHECKLENGT" + str(width) + " " +str(heigth))

    # check boundry
    if(new_xpos + width >= len(matrix) or new_xpos < 0):
        return False
    if(new_ypos + heigth >= len(matrix[0]) or new_ypos < 0):
        return False
        
    print("Corners")
    # corners
    if(matrix[new_xpos + width][new_ypos] > 4):
        return False
    if(matrix[new_xpos + width][new_ypos + heigth] > 4):
        return False
    if(matrix[new_xpos][new_ypos + heigth] > 4):
        return False
    if(matrix[new_xpos + width][new_ypos] > 4):
        return False        
    
    print("rest")
    for x in range(new_xpos, new_xpos + width, 7):
        for y in range(new_ypos, new_ypos + heigth, 7):
            if(matrix[x][y] > 9):           
                return False
    print("treu")
    return True
                
def replace_water(matrix, water, new_xpos, new_ypos):
    '''
    Places water at the given position.
    '''
    
    water.set_xpos(new_xpos)
    water.set_ypos(new_ypos)
    
    for x in range(new_xpos, new_xpos+water.get_width()):
        for y in range(new_ypos, new_ypos + water.get_heigth()):
            matrix[x][y] += 5
            
    print("newpoa")
    print(new_xpos, new_ypos)            
    return matrix
