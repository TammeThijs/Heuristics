# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:12:11 2016

@author: Stephan
"""
import random

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
        self.max_pools = 4
        self.ratio = 4
        self.area_needed = 4800
        self.area_filled = 0
        self.pools = []
        
    def get_pools(self):
        return self.pools
        
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
    for i in range(4):
        search = True
        while(search):
            search = False
            xstart = random.randint(0, len(matrix) - 71)
            ystart = random.randint(0, len(matrix[0]) - 71)
            
            if(matrix[xstart][ystart] != 0):
                search = True
            if(matrix[xstart][ystart + 70] != 0):
                search = True
            if(matrix[xstart + 70][ystart] != 0):
                search = True
            if(matrix[xstart + 70][ystart + 70] != 0):
                search = True
        
        water_pool = Water_pool(70, 70, xstart, ystart)
        # place water        
        for x in range(70):
            for y in range(70):
                matrix[x+xstart][y+ystart] = 5
        water.new_pool(water_pool)        
    return matrix, water


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
        