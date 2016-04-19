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
    width = 16
    heigth = 16
    vrijstand = 4
    cost = 285000
    gain = 1.03 # profit margin/m free space
    value = 285000 # startwaarde
    posx = False
    posy = False
    houseid = False
        
        #todo
    def getwidth(self):
        return self.width
    def getheigth(self):
        return self.heigth
    def getvrijstand(self):
        return self.vrijstand
    def getcost(self):
        return self.cost
    def getgain(self):
        return self.gain
    def getvalue(self):
        return self.value
    
class Bungalow():
    width = 16
    heigth = 20
    vrijstand = 6
    cost = 399000
    gain = 1.04
    value = 399000
    posx = False
    posy = False
    houseid = False

        #todo   
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand
    def getcost(self):
        return self.cost
    def getgain(self):
        return self.gain
    def getvalue(self):
        return self.value
        
class Maison():
    width = 22
    heigth = 21
    vrijstand = 12
    cost = 610000
    gain = 1.06 # profit margin/m free space
    value = 610000
    posx = False
    posy = False
    houseid = False

        #todo    
    def getwidth(self):
        return self.width
    def getheigth(self):
        return self.heigth
    def getvrijstand(self):
        return self.vrijstand
<<<<<<< HEAD
    def getcost(self):
        return self.cost
    def getgain(self):
        return self.gain
    def getvalue(self):
        return self.value
=======
    
>>>>>>> 2a959151197cf702020eb652fa90bed9e246b4db
