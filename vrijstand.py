# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:55:38 2016

@author: Stephan
"""

def calculate_vrijstand(matrix, house_list):
    # 1 check
    house = house_list[0]
    
    
    
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