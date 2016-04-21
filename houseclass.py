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

class House():
    
    def __init__(self):
        self.posx = False
        self.posy = False
        self.houseid = False
    
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
        if(self.houseid == False):
            raise("house id is not set!")
        return self.houseid
    def get_xpos(self):
        if(self.posx == False):
            raise("posx is not set!")
        return self.posx
    def get_ypos(self):
        if(self.posy == False):
            raise("posy is not set!")
        return self.posy
    def get_house_type(self):
        return self.house_type
        
    def change_xpos(self, xpos):
        self.posx = xpos
    def change_ypos(self, ypos):
        self.posy = ypos







class Eengezinswoning(House):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        # house dimensions in 0.5 meters  
        self.house_type = "eengezinswoning"   
        self.width = 16
        self.heigth = 16
        self.vrijstand = 4
        self.cost = 285000
        self.gain = 1.03 # profit margin/m free space
        self.value = 285000 # startwaarde
        self.housecolor = 1
    
class Bungalow(House):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.house_type = "bungalow"
        self.sort = 2
        self.width = 16
        self.heigth = 20
        self.vrijstand = 6
        self.cost = 399000
        self.gain = 1.04
        self.value = 399000
        self.posx = False
        self.posy = False
        self.houseid = False
        self.housecolor = 2
        
class Maison(House):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.house_type = "maison"
        self.sort = 3
        self.width = 22
        self.heigth = 21
        self.vrijstand = 12
        self.cost = 610000
        self.gain = 1.06 # profit margin/m free space
        self.value = 610000
        self.housecolor = 3
       