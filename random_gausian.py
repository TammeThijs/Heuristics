# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:55:52 2016

@author: Stephan
"""

import matplotlib.pyplot as plt
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
        
    houselist = []
    
   # 20 huizen,  
    placed = True
    while(placed):
        try:
            matrix, houselist = movement.houses_to_place(3, width, height)
            placed = False
        except:
            print('error happend')
        
    
    
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


#  run main any number of times
random = []
for i in range(100):
    print("*****i*************################", i, i,i)
    random.append(main())
plt.hist(random, bins = 100)