# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:04:16 2016

@author: Stephan
"""

def calculate(house_list):
    '''
    Calculate the total profit from the current vrijstand set in the 
    houseclass
    '''
    money = 0
    for house in house_list:
        cost = house.get_cost()
        gain = house.get_gain()
        extra_vrijstand = house.get_extra_vrijstand()
        total = cost + float(cost)*gain*extra_vrijstand
        money += total
    return money

def calculate_vrijstand(house_list):
    '''
    Calculate the total vrijstand from the current vrijstand set in the 
    houseclass
    '''
    totale_vrijstand = 0
    for house in house_list:
        vrijstand = house.get_vrijstand()
        extra_vrijstand = house.get_extra_vrijstand()
        total = vrijstand + extra_vrijstand
        totale_vrijstand += total
    return totale_vrijstand