# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:15:31 2016

@author: Stijn
"""

import pygame

def get_colours():
    
    # set colours for map
    White = (255, 255, 255) # Mandatory free space 1 ,2 ,3 
    Blue = (72, 118, 255) # Water
    Green = (102, 205, 0) # Grass 0
    Yellow = (255, 215, 0) # Eengezinswoning 20
    Orange = (255, 127, 0) # Bungalow 15
    Red = (205, 38, 38) # Maison 10
    
    colours = {0 : White,
               1 : Blue,
               0 : Green,
               20 : Yellow,
               15 : Orange,
               10 : Red
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
    screen = init_pygame(800, 800)
    tilesize = 2.5 # width and height    
    
    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            # draw display
            for row in range(320):
                for column in range(300):                    
                  pygame.draw.rect(screen, colours[matrix[row, column]], )
                
        
        pygame.quit()
    except SystemExit():
        running = False
        pygame.quit()
        
    
                    
    
    
    
    
    