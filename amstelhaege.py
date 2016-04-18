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

import matplotlib.pyplot as plt

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
    
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_vrijstand(self):
        return self.vrijstand

                        


def main():
    '''
    Plot a figure of the grid    

    '''
    
    # height and width 150x160
    width = 150
    height = 160
    
    # make a matrix for if pixel is taken.
    # every pixel right now stands for 1 meter. So not very precise...
    matrix = [[0 for i in range(width)] for j in range(height)]
    
    # Show info
    #print(matrix)
    print("De eerste index is: " + str(len(matrix)))
    print("De tweede index is: " + str(len(matrix[0])))
        
  
    # Place some houses
    matrix[0][0] = 1
    matrix[0][1] = 1   
    matrix[1][1] = 1
    matrix[1][0] = 1
    
    # 20 huizen
    #matrix = simple_algoritme(width, height, 3, 5, 12)
    
    plt.matshow(matrix, 
                origin = 'lower',   # Set 0,0 at bottom
                cmap=plt.cm.ocean)  # Set colors to ocean
    # Show color bar
    plt.colorbar()
    
    # Save on pc
    plt.savefig("test.png")
    
    # Show image
    plt.show()

main()
            
            
'''   
Simpel algoritme:
Eerst groote huizen (naast elkaar) met minimale vrijstand
Dan minder grote huizen met minimale vrijstand
dan alle kleinste huizen met minimale vrijstand
De rest vullen met water.

def simple_algoritme(width, height, maison, bungalow, eengezinswoning):
    
    # matrix
    matrix = [[0 for i in range(width)] for j in range(height)]
    houses_placed = 1
    
    
    # first place maisons
    for placed in range(maison):
        print("Placing house: ", placed + 1)
        huis = Maison()
    
        print("check if free")
        # start at bottom and check for room
        i_heigth = 0
        i_width = 0
        free = False
        while(free):
            free = True
            if (heigth - i_heigth - huis.get_heigth() - huis.get_vrijstand() 
            < 0):
                print("Error no space!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
            
            elif ((width - i_width - huis.get_width() + huis.get_vrijstand())
            < 0):
                free = False
                i_width = 0
                i_heigth += 1
                break
            
            else:
                for y in range(huis.get_heigth):
                    for x in range(huis.get_width):
                        if matrix[y + i_heigth][x + i_width] != 0:
                            free = False
                            i_width += x
                            break
        
        
        

    houses_placed += 1       
    # first place bungalow
    for i in range(bungalow):
        place_maison = Bungalow()
        for index_heigth in range(height):
            index_width = width - 1 - place_maison.get_width()
            # MAKE SURE THERE is space at this level
            if(matrix[index_heigth][index_width] == 0):
                
                # check where the first position is empty
                index_width = 0
                while matrix[index_heigth][index_width] != 0:
                    index_width += 1
                    
                # add maison
                for x in range(place_maison.get_width()):
                    for j in range(place_maison.get_heigth()):
                        matrix[j+index_heigth][x+ index_width] = houses_placed
                    #print(x + index_width ,j + index_heigth)
                #houses_placed += 1
                print("PLaced %i bungalow" % i)
                break
                    
            else:
                index_heigth += 1
                
    
    houses_placed += 1        
    # first place eengezinswoning
    for i in range(eengezinswoning):
        place_maison = Eengezinswoning()
        for index_heigth in range(height):
            index_width = width - 1 - place_maison.get_width()
            # MAKE SURE THERE is space at this level
            if(matrix[index_heigth][index_width] == 0):
                
                # check where the first position is empty
                index_width = 0
                while matrix[index_heigth][index_width] != 0:
                    index_width += 1
                    
                # add maison
                for x in range(place_maison.get_width()):
                    for j in range(place_maison.get_heigth()):
                        matrix[j+index_heigth][x+ index_width] = houses_placed
                   # print(x + index_width ,j + index_heigth)
                #houses_placed += 1
                print("PLaced %i eengezinswoning" % i)
                break
                    
            else:
                index_heigth += 1
            
    

            
    # plt matrix
    return matrix
'''
                    