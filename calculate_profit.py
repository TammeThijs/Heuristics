# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:04:16 2016

@author: Stephan
"""

def calculate(house_list):
    money = 0
    for house in house_list:
        cost = house.get_cost()
        gain = house.get_gain()
        extra_vrijstand = house.get_extra_vrijstand()
        total = cost + float(cost)*gain*extra_vrijstand
        money += total
        #print("opbrengst van: ", house.get_id(), " is: ", total)
        
    print("total: ", money)
    return money
