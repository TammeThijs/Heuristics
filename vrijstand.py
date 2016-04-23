# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:55:38 2016

@author: Stephan
"""

def calculate_vrijstand(matrix, house_list):
    # 1 check
    house = house_list[0]


    # house value is minimal 10    
    # 7 meter = 14 steps    
    
    # check 7 meter
    for house in house_list:
        meters = find_vrijstand(matrix, house)
        print("Halve meters: ", meters)
        print("meters: ", int(meters/2))
        house.change_extra_vrijstand(int(meters/2))
    return house_list
    
    
def find_vrijstand(matrix, house, steps = 14, back = False, prev = 0, taken = None, free = 0):
    print("calculate")
    print("steps: ", steps)
    print("taken: ", taken)
    print("free: ", free)
    print("goin back: ", back)
    if(back == False):
        if(check_layer(matrix, house, steps)):
            # free
            newsteps = steps + 14
            return find_vrijstand(matrix, house, steps = newsteps, free = steps)
        else:
            # found house
            newsteps = int(steps - 7)
            return find_vrijstand(matrix, house, steps = newsteps, back = True, taken = steps, free = free)
    else:
        if(taken - free < 2):
            print("DONNNE**********************************************")
            print("answer: ", steps)
            return steps
        else:
            if(check_layer(matrix, house, steps)):
                # free
                newsteps = int(steps + ((taken - steps) / 2))
                return find_vrijstand(matrix, house, steps = newsteps, back = True, free = steps, taken = taken)
            else:
                # found house
                newsteps = int(free + (taken - steps) / 2)
                return find_vrijstand(matrix, house, steps = newsteps, back = True, taken = steps, free = free)
        
def check_layer(matrix, house, layer):
    print("hello")
    xpos = house.get_xpos()
    ypos = house.get_ypos()
    width = house.get_width()
    heigth = house.get_heigth()
    vrij = house.get_vrijstand() + layer

    # first check boundry because else you will get our of range error
    if(xpos - vrij < 0):
        print("out of bound 1")
        return False
    if(ypos - vrij < 0):
        print("out of bound 2")
        return False
    if(xpos + width + vrij >= len(matrix)):
        print("out of bound 3")
        return False
    if(ypos + heigth + vrij >= len(matrix[0])):
        print("out of bound 4")
        return False


    # house value is minimal 10    
    
    # check 7 meter
    y = ypos - vrij
    for x in range(xpos - vrij , xpos + width + vrij, 7):
        if (matrix[x][y] > 9):
            print("found house")
            return False
    
    y = ypos + heigth + vrij
    for x in range(xpos - vrij, xpos + width + vrij, 7):
        if (matrix[x][y] > 9):
            print("found house")
            return False
        
    x = xpos - vrij
    for y in range(ypos - vrij, ypos + heigth + vrij, 7):
        if (matrix[x][y] > 9):
            print("found house")
            return False
        
    x = xpos + width + vrij
    for y in range(ypos - vrij, ypos + heigth + vrij, 7):
        if (matrix[x][y] > 9):
            print("found house")
            return False
        
    print("###############no house")
    return True
    
    
'''
Vrijstand:

je weet het huis, en zijn verplichte vrijstand zijn al vrij.

Dus je gaat kijken vanaf NA de verplichte vrijstand.

Minimaal kan er een huis tegen de verplichtevrijstand zitten met een dikte van 
8 meter (want dat is de minimale breedte)

dus als je om de 7 meter checkt of de vrijstand vrij is, dan kan er geen huis
in zitten!

Vind je geen huis?! prima 7 meter verder, enz

vind je wel een huis dan stop en doe je binairy search:
7 stappen verder dus nu 7/2 = 3; 3 stappen terug. Zoek weer alles af en kijk
of je een huis vind.


# stappen enzo klopt niet, maar je snapt het idee
3 stappen terug:
    vind je wel een huis:
        7-3 / 2 = 2; ga je 2 stappen terug:
            vind je wel een huis:
                geen extra vrijstand meer
            vind je geen huis:
                ga je een stap verder:
                    vind je wel een huis: 
                        geen extra vrijstand
                    vind je geen huis:
                        1 meter extra
    vind je geen huis:
        3 / 2 = 1; dus 1 stap verder:
            wel een huis:
                4 meter vrijstand
            geen huis:
                

'''