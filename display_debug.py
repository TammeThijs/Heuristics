
# -*- coding: utf-8 -*-
"""
Heuristieken: AmstelHaege
Name: display_debug.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

For debugging purpose
"""

#import libary
import pygame
import move_objects as mh
import random
import free_space as fs
import profit as prof

def get_colours():
    
    # set colours for map
    White = (255, 255, 255) # Mandatory free space 1 
    Overlap1 = (255, 255, 204) # Mandatory free space shared by 2 houses 2
    Overlap2 = (255, 255, 153) # Mandatory free space shared by 3 houses 3
    Blue = (72, 118, 255) # Water
    Green = (102, 205, 0) # Grass 0
    Yellow = (255, 215, 0) # Eengezinswoning 20
    Orange = (255, 127, 0) # Bungalow 15
    Red = (205, 38, 38) # Maison 10
    Black = (0,0,0)
    
    colours = {0 : Green,
               1 : White,
               2 : Overlap1,
               3 : Overlap2,
               4 : Black,
               20 : Yellow,
               15 : Orange,
               10 : Red,
               5 : Blue,
               6 : Blue,
               7 : Blue,
               8 : Blue,
               }
    return colours    

def init_pygame(width, heigth):  
    
    # initialize pygame display
    pygame.init()
    screen = pygame.display.set_mode((width, heigth))
    pygame.display.set_caption("Amstelhaege")
    
    return screen
    
def build_grid(state, matrix):
    
    colours = get_colours()    
    screen = init_pygame(640, 600)
    tilesize = 2 # width and height    
    
    running = True
    
    # Start Temp Simulated Annealing
    temperature = 1.5*10**6
    start_temp = temperature
    count = 0.0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # copy of houselist              
        houselist = state.get_houselist_copy()
        water = state.get_water_copy()
        
        # Move house
        water_or_house = 0.9
        if(water_or_house > random.random()):
            print("move house")
            house = random.randint(0, len(houselist) - 1)
            moved, new_matrix = mh.move_house(matrix, houselist[house], 10, 10)
        else:
            print("move water")
            water_pool = random.randint(0, len(water.get_pools()) - 1)
            moved, new_matrix = mh.move_water(matrix, water.get_pool(water_pool), 20, 20)
            
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
                print("Declined yet accepted")
                state.set_houselist(houselist)
                state.set_total_value(new_profit)
                state.set_water(water)
                matrix =  new_matrix
            
            # decrease temperature
            count += 1
            temperature = start_temp * ((0.999) ** abs(count))
            print("temp:                                            " + str(temperature))
            
        # draw         
        for row in range(300):
            for column in range(320):
                pygame.draw.rect(screen, colours[new_matrix[row][column]], 
                                 (column * tilesize, row * tilesize, 10, 10))
        
        caption = "Amstelhaege. Profit: " + str(state.get_total_value())
        pygame.display.set_caption(caption)
        pygame.display.flip()
               
    
    pygame.display.quit()
    pygame.quit()

    
                    
    
    
    
    
