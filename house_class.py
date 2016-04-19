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
        
    '''
    Places a the house on matrix, width xpos and ypos the bottem
    left coordinates
    '''
    def placehouse(self, matrix, xpos, ypos, houseid):
        self.houseid = houseid
        self.posx = xpos
        self.posy = ypos
        for x in range(int(self.width*2)):
            for y in range(int(self.heigth*2)):
                matrix[x+xpos][y+ypos] += 1
        return matrix
    
    '''
    Checks if the house can be placed on matrix. 
    With xpos and ypos the bottem left coordinates.
    '''
    def checkplace(self, matrix, width, heigth, xpos, ypos):
        #print("checking...")
        
        # check if fits on grid
        # right
        if (xpos + int((self.width + self.vrijstand)*2) >= width):
            return True
        #top
        elif (ypos + int((self.heigth + self.vrijstand )*2) >= heigth):
            return True
        #left
        elif( xpos - int(self.vrijstand*2) < 0):
            return True
        #bottem
        elif( ypos - int(self.vrijstand*2) < 0):
            return True
        
        # check if not already a house
            #TODO
        # bottem left
        elif(matrix[xpos][ypos] != 0):
            return True
        # top right
        elif(matrix[xpos+self.width*2][ypos+int(self.heigth*2)] != 0):
            return True   
        # bottem rigth
        elif(matrix[xpos+self.width*2][ypos] != 0):
            return True  
        #top left
        elif(matrix[xpos][ypos+int(self.heigth*2)] != 0):
            return True  
        # middle
        elif(matrix[xpos+int(self.width)][ypos+int(self.heigth)] != 0):
            return True  
            
        # check if not in mandiotry freeplace
            #TODO
        
        '''
        elif(matrix[xpos - self.vrijstand*2][ypos - self.vrijstand*2] != 0):
            return True
        elif(matrix[xpos + (self.vrijstand + self.width)*2][ypos + int((self.vrijstand + self.heigth)*2)] != 0):
            return True
        elif(matrix[xpos - self.vrijstand*2][ypos + int((self.vrijstand + self.heigth)*2)] != 0):
            return True
        elif(matrix[xpos + (self.vrijstand + self.width)*2][ypos - self.vrijstand*2] != 0):
            return True
        '''
        
        '''
        # todo ~correct dit is niet goed
        elif(matrix[xpos + (self.vrijstand + self.width)][ypos + int((self.vrijstand + self.heigth)*2)] != 0):
            return True
        elif(matrix[xpos + (self.vrijstand + self.width)*2][ypos + int((self.vrijstand + self.heigth))] != 0):
            return True
        elif(matrix[xpos + (self.vrijstand + self.width)][ypos - self.vrijstand*2] != 0):
            return True
        '''
        
        #print("passed")
        return False