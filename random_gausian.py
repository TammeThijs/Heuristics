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
sys.setrecursionlimit(10**4)              

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
        
    houselist = []
    
   # 20 huizen,  
    placed = True
    while(placed):
        try:
            matrix, houselist = houses_to_place(3, width, height)
            placed = False
        except:
            print("ging nie hea")
            placed = True
        
    
    
    # calculate vrijstand
    houselist = vrijstand.calculate_vrijstand(matrix, houselist) 
    
    # return calculated profit
    return calculate_profit.calculate(houselist)

'''
place houses 
1 for 20
2 for 40
3 for 60
'''
def houses_to_place(houses, width, height):
    # make a matrix for if pixel is taken.
    matrix = [[0 for i in range(height)] for j in range(width)]    
    
    houselist = []
    
    houseid = 0
    for i in range(3*houses):
        house = hc.Maison()
        matrix, house, correct = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(5*houses):
        house = hc.Bungalow()
        matrix, house, correct = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    for i in range(12*houses):
        house = hc.Eengezinswoning()
        matrix, house, correct = movement.random_placing(matrix, house, width, height, houseid)
        houselist.append(house)
        houseid += 1
    return matrix, houselist

#  run main any number of times
random = []
for i in range(100):
    print("*****i*************################", i, i,i)
    random.append(main())
plt.hist(random, bins = 100)