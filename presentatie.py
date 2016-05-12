
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:15:31 2016
@author: Stijn
"""

import pygame
import random_gausian as rg
import move_house as mh
import random
import vrijstand as cv
import movement
import houseclass as hc
import calculate_profit as cp

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
               -1 : Black,
               19 : Black,
               14 : Black,
               21 : Black
               }
    return colours    

def init_pygame(width, heigth):  
    
    # initialize pygame display
    pygame.init()
    screen = pygame.display.set_mode((width, heigth))
    pygame.display.set_caption("Amstelhaege")
    
    return screen
    
def build_grid(matrix):
    
    colours = get_colours()    
    screen = init_pygame(640, 600)
    tilesize = 2 # width and height    
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        for row in range(300):
            for column in range(320):
                pygame.draw.rect(screen, colours[matrix[row][column]], 
                                 (column * tilesize, row * tilesize, 10, 10))
        
        pygame.display.set_caption("Amstelhaege")
        pygame.display.flip()
               
    
    pygame.display.quit()
    pygame.quit()

    
                    
matrix = [[0 for i in range(0, 320)] for j in range(0, 300)]
house = hc.Eengezinswoning()
matrix, house = movement.random_placing(matrix, house, 320, 300, 1)
house = hc.Maison()
matrix, house = movement.random_placing(matrix, house, 320, 300, 1)
house = hc.Bungalow()
matrix, house = movement.random_placing(matrix, house, 320, 300, 1)  
build_grid(matrix)
    
    
