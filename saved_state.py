# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:31:10 2016

@author: Stijn
"""

class Saved_State():
    
    def __init__(self, matrix, value, freespace):
        self.matrix = matrix
        self.total_value = value
        self.total_freespace = freespace
        
    def get_matrix(self):
        return self.matrix
    def get_total_value(self):
        return self.total_value
    def get_total_freespace(self):
        return self.total_freespace


def main():
    
    global houselist
    global profit
    global state
    
    # set runs
    cycles = 5
    matrix = init()
    
    nr = 0
    nr2 = 0
    

    
    for i in range(cycles):
        
        house = random.randint(0, (len(houselist) - 1))
        temp_matrix = state.get_matrix()
        #print(temp_matrix)
        #display.build_grid(temp_matrix)
        matrix = mh.move_house(matrix, houselist[house], 2, 2)
                
        #free_space = cv.calculate_vrijstand(matrix, houselist)
        profit = cp.calculate(houselist)
        nr2 = nr2 + 1
        print("cycles" , nr2, "profit", profit)             

        
        if profit > state.get_total_value():
            ss.Saved_State(matrix, profit, 0)
            nr = nr + 1
            print("update" , nr, "profit2", profit)
            
            
            
            
            
    display.build_grid(matrix)
            

    
    
    
        
    
    return            

def init():
    '''
    TODO

    '''
    
    #global houselist

    
    #define the heigth and width of the matrix
    width = 300
    height = 320
    
    # place the houses on the grid.
    placed = True
    
    # 1 for 20, 2 for 40, 3 for 60
    houses_to_place = 1
    while(placed):
        try:
            matrix, houselist = movement.houses_to_place(houses_to_place, width, height)
            placed = False
        except:
            print('error happend')
            

    profit = cp.calculate(houselist)
    free_space = cv.calculate_vrijstand(matrix, houselist)    
    
    ss.Saved_State(matrix, profit, free_space)
    
    return matrix




        
        
        

            
            
#plt.hist(random, bins = 100)
main()