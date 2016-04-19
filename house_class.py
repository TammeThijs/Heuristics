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
    width = 16
    heigth = 16
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
    width = 16
    heigth = 20
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
    width = 22
    heigth = 21
    vrijstand = 6
    cost = 610000
    posx = False
    posy = False
    houseid = False
    '''
    11x10.5 TODO
    '''
    
    def getwidth(self):
        return self.width
    def getheigth(self):
        return self.heigth
    def getvrijstand(self):
        return self.vrijstand
    
