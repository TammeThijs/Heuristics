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


class Eengezinswoning():
    width = 8
    heigth = 8
    vrijstand = 1
    '''
    8x8 TODO
    '''
    def __init__(self):
        self.heigth = 8
        #todo
    def get_width(self):
        return self.width
        
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand
    
class Bungalow():
    width = 8
    heigth = 10
    vrijstand = 1
    '''
    10x7.5 TODO
    '''
    def __init__(self):
        self.width = 8
        #todo
    
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand
        
class Maison():
    width = 11
    heigth = 11
    vrijstand = 1
    '''
    11x10.5 TODO
    '''
    def __init__(self):
        self.width = 11
        #todo
    
    def getwidth(self):
        return self.width
    def getheigth(self):
        return self.heigth
    def getvrijstand(self):
        return self.vrijstand
        
    '''
    Places a the house on matrix, width xpos and ypos the bottem
    left coordinates
    '''
    def placehouse(self, matrix, xpos, ypos):
        for x in range(self.width*2):
            for y in range(self.heigth*2):
                matrix[x+xpos][y+ypos] += 1
        return matrix
    
    '''
    Checks if the house can be placed on matrix. 
    With xpos and ypos the bottem left coordinates.
    '''
    def checkplace(self, matrix, width, heigth, xpos, ypos):
        print("checking...")
        # check if fits on grid
        if (xpos + self.width*2 > width):
            return True
        elif (ypos + self.heigth*2 > heigth):
            return True
    
        print("passed")
        return False
        # check if not already a house
            #TODO
        # check if not in mandiotry freeplace
            #TODO