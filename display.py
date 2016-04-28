# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:15:31 2016

@author: Stijn
"""

import pygame

def init_pygame():
    
    # set colours for map
    White = (255, 255, 255) # Mandatory free space
    Blue = (72, 118, 255) # Water
    Green = (102, 205, 0) # Grass
    Yellow = (255, 215, 0) # Eengezinswoning
    Orange = (255, 127, 0) # Bungalow
    Red = (205, 38, 38) # Maison
    
    colours = {0 : White,
               1 : Blue,
               2 : Green,
               3 : Yellow,
               4 : Orange,
               5 : Red
               }

    # initialize pygame display
    pygame.init()
    matrix = pygame.display.set_mode((1200, 800))
    Pygame.display.set_caption("Amstelhaege")
    