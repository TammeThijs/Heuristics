# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:55:52 2016

@author: Stephan
"""

import matplotlib.pyplot as plt
import houseclass as hc
import movement
import vrijstand
import calculate_profit
import sys
sys.setrecursionlimit(10**6)              

def main():
    '''
    Plot a figure of the grid    

    '''
    global houselist
    global profit
    
    # height and width 150x160
    width = 300
    height = 320
    
    profit = []
    
    # make a matrix for if pixel is taken.
    matrix = [[0 for i in range(height)] for j in range(width)]
        
    houseid = 0
    houselist = []
    # 20 huizen, 
    for i in range(3):
        house = hc.Maison()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(5):
        house = hc.Bungalow()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(12):
        house = hc.Eengezinswoning()
        matrix, house = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
        
    
    # calculate vrijstand
    houselist = vrijstand.calculate_vrijstand(matrix, houselist) 
    
    # return calculated profit
    return calculate_profit.calculate(houselist)

#  run main any number of times
random = []
for i in range(10000):
    print("*****i*************################", i, i,i)
    random.append(main())
plt.hist(random, bins = 100)