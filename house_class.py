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
    heigth = 10.5
    vrijstand = 6
    cost = 610000
    posx = False
    posy = False
    houseid = False
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
    
