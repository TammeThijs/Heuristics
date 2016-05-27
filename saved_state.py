# -*- coding: utf-8 -*-
"""
Heuristieken: AmstelHaege
Name: saved_state.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

contains saved state to keep track of the best state
"""

class saved_state():
    '''
    Used to save the the best state of the matrix.
    '''
    
    def __init__(self, profit, houselist, water):
        self.total_value = profit
        self.houselist = houselist
        self.water = water
        
    def get_total_value(self):
        return self.total_value

    def set_total_value(self, profit):
        self.total_value = profit
        
    def set_houselist(self, houselist):
        self.houselist = houselist
        
    def set_water(self, water):
        self.water = water
        
    def get_houselist_copy(self):
        new_list=[]
        for house in self.houselist:
            new_list.append(house.copy())
        return new_list
        
    def get_water_copy(self):
        return self.water.copy()
            