# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:12:11 2016

@author: Stephan
"""
import random
import math

class Water_pool():
    def __init__(self, width, heigth, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.heigth = heigth
        self.area = width*heigth
    
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_area(self):
        return self.area
    def get_xpos(self):
        return self.xpos
    def get_ypos(self):
        return self.ypos
    def set_xpos(self, new_xpos):
        self.xpos = new_xpos
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
    
    def change_size(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.area = width*heigth
    
    

class Water():
    def __init__(self):
        self.max_pools = random.randint(1,4)
        self.ratio = 4
        self.area_needed = 19200
        self.area_filled = 0
        self.pools = []
        
    def get_pools(self):
        return self.pools
    def get_max_pools(self):
        return self.max_pools        
    def get_pool(self, index):
        if(index - 1 > 4):
            raise 'This pool does not exist'
        return self.pools[index]        
    def new_pool(self, newpool):
        if(len(self.pools) >= 4):
            raise 'could not add another pool'
        self.pools.append(newpool)    
    def delete_pool(self, index):
        self.pools.pop(index)
    def get_filled(self):
        return self.area_filled
    def get_needed(self):
        return self.area_needed 
    def set_filled(self, filled):
        self.area_needed = self.area_needed - filled
        self.area_filled = self.area_filled + filled
    def copy(self):
        new_water = Water()
        for pool in self.pools:
            
            new_water_pool = Water_pool(pool.get_width(), pool.get_heigth(),
                                  pool.get_xpos(), pool.get_ypos())
            
            new_water.new_pool(new_water_pool)
        return new_water
'''
place water by finding the larges free space and place it there.
'''        
def place_water(matrix):
    water = Water()
    count = water.get_max_pools()
    
 
    for i in range(count):  
        
        if(i < count-1):
            max_width = math.floor(math.sqrt(water.get_needed()))
            width = random.randint(14, max_width)
            heigth = math.ceil(width/(random.randint(1,4)))
            surface = width*heigth
        else:
            width = math.ceil(math.sqrt(water.get_needed()))
            if(width < 14):
                width = 14
            heigth = width
            surface = water.get_needed()
            
        water.set_filled(surface)                
                
        search = True
        while(search):
            search = False
            xstart = random.randint(0, len(matrix) - (width+1))
            ystart = random.randint(0, len(matrix[0]) - (heigth+1))
            
            if(matrix[xstart][ystart] != 0):
                search = True
            if(matrix[xstart][ystart + heigth] != 0):
                search = True
            if(matrix[xstart + width][ystart] != 0):
                search = True
            if(matrix[xstart + width][ystart + heigth] != 0):
                search = True
                
            y = ystart
            for x in range(xstart, xstart + width,14):
                if(matrix[x][y] > 9):           
                    return False
            y = ystart + heigth
            for x in range(xstart, xstart + width, 14):
                if(matrix[x][y] > 9):           
                    return False        
            x = xstart       
            for y in range(ystart, ystart + heigth, 14):
                if(matrix[x][y] > 9):           
                    return False      
            x = xstart + width      
            for y in range(ystart, ystart + heigth, 14):
                if(matrix[x][y] > 9):           
                    return False  
        
        water_pool = Water_pool(width, heigth, xstart, ystart)
        # place water        
        for x in range(width):
            for y in range(heigth):
                matrix[x+xstart][y+ystart] += 5
        water.new_pool(water_pool)        
    return matrix, water

def place_water_rectangle(matrix):
    water = Water()
    water_width = 40
    water_heigth = 150
    
    for i in range(4):
        search = True
        while(search):
            search = False
            xstart = random.randint(0, len(matrix) - water_width - 1)
            ystart = random.randint(0, len(matrix[0]) - water_heigth - 1)
            
            if(matrix[xstart][ystart] != 0):
                search = True
            if(matrix[xstart][ystart + water_heigth] != 0):
                search = True
            if(matrix[xstart + water_width][ystart] != 0):
                search = True
            if(matrix[xstart + water_width][ystart + water_heigth] != 0):
                search = True
        
        water_pool = Water_pool(water_width, water_heigth, xstart, ystart)
       
        # place water        
        for x in range(water_width):
            for y in range(water_heigth):
                matrix[x+xstart][y+ystart] = 5
        water.new_pool(water_pool)        
    return matrix, water

def place_water_rectangle_random(matrix):
    water = Water()
    chance = 0.5
        
    for i in range(4):
        if(chance > random.random()):
            water_width = 40
            water_heigth = 150
        else:
            water_width = 150
            water_heigth = 40
        
        matrix, xstart, ystart = get_coords_rectangle_random(matrix, water_width, water_heigth)
        
        water_pool = Water_pool(water_width, water_heigth, xstart, ystart)
       
        # place water        
        for x in range(water_width):
            for y in range(water_heigth):
                matrix[x+xstart][y+ystart] = 5
        water.new_pool(water_pool)        
    return matrix, water
    
def get_coords_rectangle_random(matrix, water_width, water_heigth, count = 0):
    print("placing water....   " + str(count))
    count += 1
    if(count > 10**3):
        raise("water placement error")
        
    xstart = random.randint(0, len(matrix) - water_width - 1)
    ystart = random.randint(0, len(matrix[0]) - water_heigth - 1)
    
    # edges
    if(matrix[xstart][ystart] != 0):
        return get_coords_rectangle_random(matrix, water_width, water_heigth, count = count)
    if(matrix[xstart][ystart + water_heigth] != 0):
        return get_coords_rectangle_random(matrix, water_width, water_heigth, count = count)
    if(matrix[xstart + water_width][ystart] != 0):
        return get_coords_rectangle_random(matrix, water_width, water_heigth, count = count)
    if(matrix[xstart + water_width][ystart + water_heigth] != 0):
        return get_coords_rectangle_random(matrix, water_width, water_heigth, count = count)
        
    # whole
    for x in range(xstart, xstart + water_width):
        for y in range(ystart, ystart + water_heigth):
            if(matrix[x][y] != 0):
                return get_coords_rectangle_random(matrix, water_width, water_heigth, count = count)
                
    return matrix, xstart, ystart
'''
place water by finding the larges free space and place it there.
'''        
def place_water_old(matrix):
    xstart = random.randint(0, len(matrix) - 141)
    ystart = random.randint(0, len(matrix[0]) - 141)
    for x in range(140):
        for y in range(140):
            matrix[x+xstart][y+ystart] = 5
    return matrix
        