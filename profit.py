# -*- coding: utf-8 -*-
"""
Heuristieken: AmstelHaege
Name: profit.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

calculate the current profit or current free space
"""

def calculate_value(house_list):
    '''
    Calculate the total profit from the current vrijstand set in the 
    houseclass.
    
    IMPORTANT: Make sure you have updated the free space in the house class 
    before you call this function.
    '''
    # total value
    value = 0
    
    # calculate per house
    for house in house_list:
        # value of single house
        cost = house.get_cost()
        gain = house.get_gain()
        extra_vrijstand = house.get_extra_vrijstand()
        total_cost_of_house = cost + float(cost)*gain*extra_vrijstand
        
        # add
        value += total_cost_of_house
    return value

def calculate_free_space(house_list):
    '''
    Calculate the total free space from the current free space set in the 
    houseclass.
    
    IMPORTANT: Make sure you have updated the free space in the house class 
    before you call this function.
    '''
    
    total_free_space = 0
    
    # calculate per house
    for house in house_list:
        # free space of house
        manditory_fs = house.get_vrijstand()
        extra_fs = house.get_extra_vrijstand()
        total_house_fs = manditory_fs + extra_fs
        
        # add
        total_free_space += total_house_fs
    return total_free_space