# -*- coding: utf-8 -*-
"""
Heuristieken: AmstelHaege
Name: main.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

This is the main file. Here you can run Random Sampling, Hill Climber 
and simulated annealing.
"""

# import libary
import initialize as init
import free_space as fs
import profit as prof
import saved_state as ss
import sys
import time
import random
import move_objects as move

# make recursion bigger
sys.setrecursionlimit(10**6)

#grid variables in 0.5 meter
WIDTH = 300 
HEIGTH = 320   

def showGaussian(houses_to_place, scope):
    """
    Random Sampling, it will return 2 list, first the list with all values
    and second a list with all free space. 
    ShowGaussian takes 2 parameters. 
    houses_to_place: the amount of houses to place 1 for 20, 2 for 40 and 
    3 for 60.
    scope: the amount of random samples you want to take.
    """
    # save found values
    value_list = []
    free_space_list = []

    # do random sample scope amount of times
    for i in range(scope):
        
        # if a grid could not be placed it will give an error. So surround 
        # with try execpt to catch the error.
        placed = True
        while(placed):
            try:
                # place houses
                matrix, houselist, water = init.initialize_matrix(
                                            houses_to_place, WIDTH, HEIGTH)
                placed = False
            except:
                placed = True
            
        # update free space
        fs.calculate_new_vrijstand_to_class(matrix, houselist)
        
        # calculate profit
        free_space = prof.calculate_vrijstand(houselist)
        value = prof.calculate(houselist)
        
        # update
        if(i % 10 == 0):
            print((i*100)/scope, "%")   

        value_list.append(value)
        free_space_list.append(free_space)

    return value_list, free_space_list 



def hill_climber_value(steps, houses_to_place):
    '''
    Finds max profit using Hill Climber. Returns a dictionary with saved data.
    Takes 2 arguments.
    Steps: the amount of steps a hill climber has to make. A steps is defined 
    as a succesful move of a house or water.
    Houses_to_place: 1 for 20 houses, 2 for 40, 3 for 60.
    '''
    
    print("Starting hill climber max value")
    
    # save profit and time
    found_profit_per_run = []
    time_needed = []
    
    # 90% change to move house, 10% change to move water
    water_or_house = 0.9
    
    # place houses
    not_placed = True
    
    # start placing
    while(not_placed):
        print("Initialize")
        init.initialize_matrix(houses_to_place, WIDTH, HEIGTH)
        try:
            matrix, houselist, water = init.initialize_matrix(
                                            houses_to_place, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True

    # calculate initial profit
    fs.calculate_new_vrijstand_to_class(matrix, houselist)
    result = prof.calculate_value(houselist)
    
    found_profit_per_run.append(result)
            
    # save findings
    state = ss.saved_state(result, houselist, water)
    
    # do the hillclimber
    start_run = time.time()
    runtimes = 0
    while (runtimes < steps):
        
        # update
        if( runtimes % (steps / 100) == 0):
            print(runtimes)

        # make a copy of houselist and water           
        houselist = state.get_houselist_copy()
        water = state.get_water_copy()
        
        # random move water or house
        if(water_or_house > random.random()):
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = move.move_house(
                                    matrix, houselist[house], 100, 100)
        else:
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = move.move_water(
                                    matrix, water.get_pool(water_pool), 10, 10)
          
        # if a house or water has succesfully been moved.
        if(moved):
            # calculate new profit
            fs.calculate_new_vrijstand_to_class(new_matrix, houselist)
            new_profit = prof.calculate_value(houselist)
            
            # if profit is more, accept it
            if(new_profit >= state.get_total_value()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            
            # save found data
            found_profit_per_run.append(state.get_total_value())
            time_needed.append(time.time() - start_run)
            
            # One step is completed
            runtimes += 1

    # save final profit
    final_profit = state.get_total_value()
    
    # done
    end_run = time.time() 
    
    # make dictionary to return data
    return_values = {"matrix": matrix, "profit_per_run":found_profit_per_run, 
                     "time_needed":time_needed, "start_time":start_run, 
                     "end_time":end_run, "final_profit":final_profit}
    return return_values
    

def hill_climber_vrijstand(steps, houses_to_place):
    '''
    Finds max vrijstand using Hill Climber. Returns a dictionary with saved data.
    Takes 2 arguments.
    Steps: the amount of steps a hill climber has to make. A steps is defined 
    as a succesful move of a house or water.
    Houses_to_place: 1 for 20 houses, 2 for 40, 3 for 60.
    '''
    
    print("Starting hill climber max value")
    
    # save profit and time
    found_profit_per_run = []
    time_needed = []
    
    # 90% change to move house, 10% change to move water
    water_or_house = 0.9
    
    # place houses
    not_placed = True
    
    # start placing
    while(not_placed):
        try:
            matrix, houselist, water = init.initialize_matrix(
                                            houses_to_place, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True

    # calculate initial profit
    fs.calculate_new_vrijstand_to_class(matrix, houselist)
    result = prof.calculate_free_space(houselist)
    
    found_profit_per_run.append(result)
            
    # save findings
    state = ss.saved_state(result, houselist, water)
    
    # do the hillclimber
    start_run = time.time()
    runtimes = 0
    while (runtimes < steps):
        
        # update
        if( runtimes % (steps / 100) == 0):
            print(runtimes)

        # make a copy of houselist and water           
        houselist = state.get_houselist_copy()
        water = state.get_water_copy()
        
        # random move water or house
        if(water_or_house > random.random()):
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = move.move_house(matrix, houselist[house], 100, 100)
        else:
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = move.move_water(matrix, water.get_pool(water_pool), 10, 10)
          
        # if a house or water has succesfully been moved.
        if(moved):
            # calculate new profit
            fs.calculate_new_vrijstand_to_class(new_matrix, houselist)
            new_profit = prof.calculate_free_space(houselist)
            
            # if profit is more, accept it
            if(new_profit >= state.get_total_value()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            
            # save found data
            found_profit_per_run.append(state.get_total_value())
            time_needed.append(time.time() - start_run)
            
            # One step is completed
            runtimes += 1

    # save final profit
    final_profit = state.get_total_value()
    
    # done
    end_run = time.time() 
    
    # make dictionary to return data
    return_values = {"matrix": matrix, "profit_per_run":found_profit_per_run, 
                     "time_needed":time_needed, "start_time":start_run, 
                     "end_time":end_run, "final_profit":final_profit}
    return return_values
    
   
    
def simulated_annealing_value(houses_to_place):
    '''
    Finds max value using Simulated annealing. Returns a dictionary with saved data.
    Takes 2 arguments.
    Houses_to_place: 1 for 20 houses, 2 for 40, 3 for 60.
    '''
    
    print("simulated annealing")
    
    # save profit and time
    found_profit_per_run = []
    time_needed = []
    
    # 90% change to move house, 10% change to move water
    water_or_house = 0.9
    
    # place houses
    not_placed = True
    
    # start placing
    while(not_placed):
        try:
            matrix, houselist, water = init.initialize_matrix(
                                            houses_to_place, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True

    # calculate initial profit
    fs.calculate_new_vrijstand_to_class(matrix, houselist)
    result = prof.calculate_value(houselist)
    
    found_profit_per_run.append(result)
            
    # save findings
    state = ss.saved_state(result, houselist, water)
    
    # Start Temp Simulated Annealing
    temperature = 1.5*10**6
    start_temp = temperature
    count = 0.0
    
    # do the simulated annealing
    start_run = time.time()
    while(temperature > 1.0):
        
        # update
        if(count % 100 == 0):
            print(count, temperature)
            
        # make a copy of houselist              
        houselist = state.get_houselist_copy()
        water = state.get_water_copy()
        
         # random move water or house
        if(water_or_house > random.random()):
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = move.move_house(matrix, houselist[house], 100, 100)
        else:
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = move.move_water(matrix, water.get_pool(water_pool), 10, 10)
          
        
        # if a house or water has succesfully been moved.
        if(moved):
            # calculate new profit
            fs.calculate_new_vrijstand_to_class(new_matrix, houselist)
            new_profit = prof.calculate_value(houselist)
            
            # if more accepts
            if(new_profit >= state.get_total_value()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            # else random accept depending on temperature
            elif((state.get_total_value() - new_profit) / temperature  < random.random()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            
            # decrease temperature
            count += 1
            temperature = start_temp * ((0.999) ** abs(count))
            
            # save findings
            found_profit_per_run.append(state.get_total_value())
            time_needed.append(time.time() - start_run)
   

    # final profit
    final_profit = state.get_total_value()
    
    # done
    end_run = time.time()
    
    return_values = {"matrix": matrix, "profit_per_run":found_profit_per_run, 
                     "time_needed":time_needed, "start_time":start_run, 
                     "end_time":end_run, "final_profit":final_profit}
    return return_values

def simulated_annealing_vrijstand(houses_to_place):
    '''
    Finds max vrijstand using Simulated annealing. Returns a dictionary with saved data.
    Takes 2 arguments.
    Houses_to_place: 1 for 20 houses, 2 for 40, 3 for 60.
    '''
    
    print("simulated annealing")
    
    # save profit and time
    found_profit_per_run = []
    time_needed = []
    
    # 90% change to move house, 10% change to move water
    water_or_house = 0.9
    
    # place houses
    not_placed = True
    
    # start placing
    while(not_placed):
        try:
            matrix, houselist, water = init.initialize_matrix(
                                            houses_to_place, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True

    # calculate initial profit
    fs.calculate_new_vrijstand_to_class(matrix, houselist)
    result = prof.calculate_free_space(houselist)
    
    found_profit_per_run.append(result)
            
    # save findings
    state = ss.saved_state(result, houselist, water)
    
    # Start Temp Simulated Annealing
    temperature = 50
    start_temp = temperature
    count = 0.0
    
    # do the simulated annealing
    start_run = time.time()
    while(temperature > 0.08):
        
        # update
        if(count % 100 == 0):
            print(count, temperature)
            
        # make a copy of houselist              
        houselist = state.get_houselist_copy()
        water = state.get_water_copy()
        
         # random move water or house
        if(water_or_house > random.random()):
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = move.move_house(matrix, houselist[house], 100, 100)
        else:
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = move.move_water(matrix, water.get_pool(water_pool), 10, 10)
          
        
        # if a house or water has succesfully been moved.
        if(moved):
            # calculate new profit
            fs.calculate_new_vrijstand_to_class(new_matrix, houselist)
            new_profit = prof.calculate_free_space(houselist)
            
            # if more accepts
            if(new_profit >= state.get_total_value()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            # else random accept depending on temperature
            elif((state.get_total_value() - new_profit) / temperature  < random.random()):
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            
            # decrease temperature
            count += 1
            temperature = start_temp * ((0.999) ** abs(count))
            
            # save findings
            found_profit_per_run.append(state.get_total_value())
            time_needed.append(time.time() - start_run)
   

    # final profit
    final_profit = state.get_total_value()
    
    # done
    end_run = time.time()
    
    return_values = {"matrix": matrix, "profit_per_run":found_profit_per_run, 
                     "time_needed":time_needed, "start_time":start_run, 
                     "end_time":end_run, "final_profit":final_profit}
    return return_values  
    
def run_with_pygame():
    '''
    FOR DEBUGGING PURPOSE ONLY.
    First build a grid and then show every step with pygame.
    This will run slowely.
    For debugging purposes.
    '''
    import display_debug
    
    # place houses
    not_placed = True
    # place 60 houses
    houses_to_place = 3

    while(not_placed):
        try:
            matrix, houselist, water = init.initialize_matrix(
                                            houses_to_place, WIDTH, HEIGTH)
            not_placed = False
        except:
            not_placed = True    

    # calculate initial profit
    fs.calculate_new_vrijstand_to_class(matrix, houselist)
    result = prof.calculate_value(houselist)
            
    # save findings
    state = ss.saved_state(result, houselist, water)
    
    display_debug.build_grid(state, matrix)
