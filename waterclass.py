"""
Heuristieken: AmstelHaege
Name: waterclass.py
Autors: Stephan Kok, Stijn Buiteman and Tamme Thijs.
Last modified: 27-05-2016

contains water class
"""
class Water_pool():
    """
    Class for a invidual pool of water.
    
    Has constrictions for the invidual pool.
    """
    def __init__(self, width, heigth, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.heigth = heigth
        self.area = width*heigth
    
    def get_width(self):
        return self.width
    def get_heigth(self):
        return self.heigth
    def get_area(self):
        return self.area
    def get_xpos(self):
        return self.xpos
    def get_ypos(self):
        return self.ypos
    def set_xpos(self, new_xpos):
        self.xpos = new_xpos
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
    
    

class Water():
    """
    Main water class used to contains pools of water.
    
    Contain the restrictions of total water.
    """
    
    def __init__(self):
        self.max_pools = 4
        self.ratio = 4
        self.pools = []
        
    def get_pools(self):
        return self.pools
        
    def get_max_pools(self):
        return self.max_pools   
        
    def get_pool(self, index):
        if(index - 1 > len(self.pools) or index < 0):
            raise 'This pool does not exist'
        return self.pools[index]    
        
    def new_pool(self, newpool):
        if(len(self.pools) >= self.max_pools):
            raise 'Already at max pools'
        self.pools.append(newpool)  
        
    def delete_pool(self, index):
        self.pools.pop(index)
        
    def copy(self):
        '''
        Return a copy of water.
        '''
        # new water
        new_water = Water()
        for pool in self.pools:
            # new pools
            new_water_pool = Water_pool(pool.get_width(), pool.get_heigth(),
                                  pool.get_xpos(), pool.get_ypos())
            new_water.new_pool(new_water_pool)
        return new_water