# -*- coding: utf-8 -*-
"""
Spyder Editor

Heuristieken: AmstelHaege

Autors: 
Stephan Kok 10627987, 
Stijn ... ...,
... ... ...


Last modified:
Stephan 04/04 21.13
"""

# import libary
import matplotlib.pyplot as plt
import display
import display_debug
import movement
import free_space
import profit

import saved_state as ss
import numpy as np
import sys
sys.setrecursionlimit(10**6)

#grid variables
WIDTH = 300 
HEIGTH = 320   

def main():

    # 1 for 20, 2 for 40, 3 for 60
    houses_to_place = 3

    showGaussian(houses_to_place, 1000, 2)

    return 

def showGaussian(houses, scope, desiredResult):

    savedResults = []

    for i in range(scope):
        result = 0        
        placed = True
        
        while(placed):
            try:
                matrix, houselist, water = movement.houses_to_place(houses, WIDTH, HEIGTH)
                placed = False
            except:
                placed = True
            
        
        if(desiredResult == 1):
            result = free_space.calculate(matrix, houselist)
            
        else:
            free_space.calculate(matrix, houselist)
            result = profit.calculate(houselist)
            
        if(i % 10 == 0):
            print((i*100)/scope, "%")   

        savedResults.append(result)

    return plt.hist(savedResults, bins = 100)


#main()

def run_with_pygame():
    '''
    First build a grid and then show every step with pygame.
    This will run slowely.
    For debugging purposes.
    '''
    # make sure you keep track of matrix witch will be the latest version
    global matrix
    global state
    
    # place houses
    not_placed = True
    # place 60 houses
    houses = 3

    while(not_placed):
        try:
            matrix, houselist, water = movement.houses_to_place(houses, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True    

    # calculate initial profit
    free_space.calculate_vrijstand(matrix, houselist)
    result = profit.calculate(houselist)
            
    # save findings
    state = ss.Saved_State(result, houselist, water)
    
    display_debug.build_grid(state, matrix)
#run_with_pygame()    

def hill_climber(runs):
    '''
    Run with hill climber
    Finds max profit
    '''
    # imports
    import move_house as mh
    import random
    import free_space as cv
    import profit as cp
    import display_show_end as dse
    import time
    
    
    global INFO
    INFO = "Hill climber. "
    
    # save last to show with pygame
    global matrix
    global state
    global water_or_house
    global found_profit_per_run
    global time_needed
    global start_run
    global end_run
    
    found_profit_per_run = []
    time_needed = []
    water_or_house = 0.9
    
    # place houses
    not_placed = True
    
    # place 60 houses
    houses = 3
    # start placing
    while(not_placed):
        try:
            matrix, houselist, water = movement.houses_to_place(houses, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True
    
    global first_matrix
    
    first_matrix = np.copy(matrix)

    # calculate initial profit
    free_space.calculate_vrijstand(matrix, houselist)
    result = profit.calculate(houselist)
    
    found_profit_per_run.append(result)
            
    # save findings
    state = ss.Saved_State(result, houselist, water)
    
    # do the hillclimber
    start_run = time.time()
    for i in range(runs):
        if( i % (runs / 100) == 0):
            print(i)
        # make a copy of houselist              
        houselist = state.get_houselist()
        water = state.get_water()
        
        if(water_or_house > random.random()):
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = mh.move_house(matrix, houselist[house], 100, 100)
        else:
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = mh.move_water(matrix, water.get_pool(water_pool), 10, 10)
          
        
        if(moved):
            cv.calculate_vrijstand(new_matrix, houselist)
            new_profit = cp.calculate(houselist)
            if(new_profit >= state.get_total_value()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
        found_profit_per_run.append(state.get_total_value())
        time_needed.append(time.time() - start_run)
               
               
    global final_profit
    final_profit = state.get_total_value()
    
    
    end_run = time.time()  
    plt.figure()         
    plt.imshow(first_matrix) 
    plt.figure()
    plt.imshow(matrix)
    dse.build_grid(state, matrix)
    
def hill_climber_vrijstand(runs):
    '''
    Run with hill climber
    Finds max vrijstand
    '''
    # imports
    import move_house as mh
    import random
    import free_space as cv
    import profit as cp
    import display_show_end as dse
    import time
    
    
    global INFO
    INFO = "Hill climber. "
    
    # save last to show with pygame
    global matrix
    global state
    global water_or_house
    global found_profit_per_run
    global time_needed
    global start_run
    global end_run
    
    found_profit_per_run = []
    time_needed = []
    water_or_house = 0.9
    
    # place houses
    not_placed = True
    
    # place 60 houses
    houses = 3
    # start placing
    while(not_placed):
        try:
            matrix, houselist, water = movement.houses_to_place(houses, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True
    
    global first_matrix
    
    first_matrix = np.copy(matrix)

    # calculate initial profit
    free_space.calculate_vrijstand(matrix, houselist)
    result = profit.calculate_vrijstand(houselist)
    
    found_profit_per_run.append(result)
            
    # save findings
    state = ss.Saved_State(result, houselist, water)
    
    # do the hillclimber
    start_run = time.time()
    for i in range(runs):
        if( i % (runs / 100) == 0):
            print(i)
        # make a copy of houselist              
        houselist = state.get_houselist()
        water = state.get_water()
        
        if(water_or_house > random.random()):
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = mh.move_house(matrix, houselist[house], 100, 100)
        else:
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = mh.move_water(matrix, water.get_pool(water_pool), 10, 10)
          
        
        if(moved):
            cv.calculate_vrijstand(new_matrix, houselist)
            new_profit = cp.calculate_vrijstand(houselist)
            if(new_profit >= state.get_total_value()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
        found_profit_per_run.append(state.get_total_value())
        time_needed.append(time.time() - start_run)
               
               
    global final_profit
    final_profit = state.get_total_value()
    
    
    end_run = time.time()  
    plt.figure()         
    plt.imshow(first_matrix) 
    plt.figure()
    plt.imshow(matrix)
    dse.build_grid(state, matrix)
    
hill_climber_vrijstand(30000)

plt.figure()
plt.plot(found_profit_per_run)
plt.title("vrijstand per run. Max: " + str(state.get_total_value()))
plt.xlabel("runs")
plt.ylabel("profit")
plt.show()

plt.figure()
plt.plot(time_needed)
plt.title("Time needed: " + str(end_run - start_run))
plt.xlabel("runs")
plt.ylabel("time")
plt.show()

