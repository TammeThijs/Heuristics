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
    
    # house dimensions in 0.5 meters  
    type = "eengezinswoning"   
    width = 16
    heigth = 16
    vrijstand = 4
    cost = 285000
    gain = 1.03 # profit margin/m free space
    value = 285000 # startwaarde
    posx = False
    posy = False
    houseid = False
    housecolor = 1
       
    def get_type(self):
        return self.type
    def get_color(self):
        return self.housecolor
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand
    def get_cost(self):
        return self.cost
    def get_gain(self):
        return self.gain
    def get_value(self):
        return self.value
    def get_id(self):
        return self.value
    
class Bungalow():
    
    type = "bungalow"
    sort = 2
    width = 16
    heigth = 20
    vrijstand = 6
    cost = 399000
    gain = 1.04
    value = 399000
    posx = False
    posy = False
    houseid = False
    housecolor = 2


    def get_type(self):
        return self.type
    def get_color(self):
        return self.housecolor
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand
    def get_cost(self):
        return self.cost
    def get_gain(self):
        return self.gain
    def get_value(self):
        return self.value
    def get_id(self):
        return self.value
        
class Maison():
    
    type = "maison"
    sort = 3
    width = 22
    heigth = 21
    vrijstand = 12
    cost = 610000
    gain = 1.06 # profit margin/m free space
    value = 610000
    posx = False
    posy = False
    houseid = False
    housecolor = 3
    
    #getters
    def get_type(self):
        return self.type
    def get_color(self):
        return self.housecolor
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand
    def get_cost(self):
        return self.cost
    def get_gain(self):
        return self.gain
    def get_value(self):
        return self.value
    def get_id(self):
        return self.value
