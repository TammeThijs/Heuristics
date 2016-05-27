# -*- coding: utf-8 -*-
"""
Heuristieken: AmstelHaege
Name: initialize.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

Initialize the matrix
"""

# import libary
import random
import houseclass as hc
import waterclass as wc
import housecheck as hcheck



def initialize_matrix(houses, width, height):   
    '''
    Create matrix, place water, place all houses one by one. 
    First big then small. Try to place all houses 1000 times.
    
    WARNING: It can be possible that the random placement made it impossible
    to place all houses. When this happens an error is raised. So be sure
    to surron in try, except to catch this.
    '''
    
    # build matrix
    matrix = [[0 for i in range(height)] for j in range(width)] 
    
    # place water
    matrix, water = place_water_rectangle_random(matrix)    
    
    # place all houses    
    houselist = [] 
    # Maison
    for i in range(3*houses):
        house = hc.Maison()
        matrix, house = random_placing(matrix, house, width, height)
        houselist.append(house)
    
    # Bungalow
    for i in range(5*houses):
        house = hc.Bungalow()
        matrix, house = random_placing(matrix, house, width, height)
        houselist.append(house)
    
    # Eengezinswoning
    for i in range(12*houses):
        house = hc.Eengezinswoning()
        matrix, house = random_placing(matrix, house, width, height)
        houselist.append(house)
        
    return matrix, houselist, water



def random_placing(matrix, house, width, height, iteration = 0):
    '''
    Place houses random on the matrix. Randomise a random position inside the 
    matrix. 
    '''
    # Try to place 1000 times, if fails give error
    iteration += 1    
    if (iteration > 1000):
        raise("error iteration")
    
    # get random position
    randy = random.randint(0, height-1)
    randx = random.randint(0, width-1)       
    
    # check if house can be placed
    if(hcheck.placement_check(house, matrix, randx, randy) 
    == False):
        random_placing(matrix, house, width, height, iteration = iteration)
    else:
        matrix, house = hcheck.place_house(house, matrix, randx, randy)
    
    # done return
    return matrix, house
   
def place_water_rectangle_random(matrix):
    """
    Place 4 water pools in rectangalar shape with a ratio of 1:3.75.
    
    This function must be called BEFORE houses are placed. This is because not
    every position is checked. If houses are placed, water will be placed
    on invalid locations.
    """
    # All 4 water pools
    water = wc.Water()
    
    # equal change for direction of water pool
    chance = 0.5
        
    # place all water pools
    for i in range(water.get_max_pools()):
        # determine direction
        if(chance > random.random()):
            water_width = 40
            water_heigth = 150
        else:
            water_width = 150
            water_heigth = 40
        
        # get a valid position
        matrix, xstart, ystart = get_coords_rectangle_random(
                                	matrix, water_width, water_heigth)
        
        # Make the water pool
        water_pool = wc.Water_pool(water_width, water_heigth, xstart, ystart)
       
        # place water pool on matrix     
        for x in range(water_width):
            for y in range(water_heigth):
                matrix[x+xstart][y+ystart] = 5
        
        # add water pool to total water
        water.new_pool(water_pool)     
    
    return matrix, water
    
def get_coords_rectangle_random(matrix, water_width, water_heigth, count = 0):
    """
    Search a valid position. 
    
    Uses recursion to find a valid position. If called over 1000 times it
    will raise an error.
    """
    
    # Destory infinity loops
    count += 1
    if(count > 10**3):
        raise("Can not find valid position for water")
        
    # get random position within grid
    xstart = random.randint(0, len(matrix) - water_width - 1)
    ystart = random.randint(0, len(matrix[0]) - water_heigth - 1)
    
    # Check if already there is already water at edges ifso try again
    if(matrix[xstart][ystart] != 0):
        return get_coords_rectangle_random(
                matrix, water_width, water_heigth, count = count)
    
    if(matrix[xstart][ystart + water_heigth] != 0):
        return get_coords_rectangle_random(
                matrix, water_width, water_heigth, count = count)
                
    if(matrix[xstart + water_width][ystart] != 0):
        return get_coords_rectangle_random(
                matrix, water_width, water_heigth, count = count)
                
    if(matrix[xstart + water_width][ystart + water_heigth] != 0):
        return get_coords_rectangle_random(
                matrix, water_width, water_heigth, count = count)
        
    # check all positions
    for x in range(xstart, xstart + water_width):
        for y in range(ystart, ystart + water_heigth):
            if(matrix[x][y] != 0):
                return get_coords_rectangle_random(
                        matrix, water_width, water_heigth, count = count)
                
    return matrix, xstart, ystart   
