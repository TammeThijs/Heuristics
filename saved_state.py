# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:31:10 2016

@author: Stijn
"""

class Saved_State():
    
    def __init__(self, profit, houselist, water):
        self.total_value = profit
        self.houselist = houselist
        self.water = water
        
    def get_total_value(self):
        return self.total_value
    def get_houselist(self):
        new_list=[]
        for house in self.houselist:
            new_list.append(house.copy())
        return new_list
    def get_water(self):
        return self.water.copy()
    
    def set_total_value(self, profit):
        self.total_value = profit
    def set_houselist(self, houselist):
        self.houselist = houselist
    def set_water(self, water):
        self.water = water
        '''
    def get_matrix(self):
        return self.matrix
    def get_houselist(self):
        return self.houselist
    def get_total_value(self):
        return self.total_value
    def get_total_freespace(self):
        return self.total_freespace
        '''

