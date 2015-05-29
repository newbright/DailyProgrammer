import random

class tree:
    
    def __init__(self, age, (x, y)):
        #age in months, 12 months = 1 year
        self.age = age
        self.position = (x, y)
    
    def spawn_sapling(self, forest):
        #saplings cannot spawn other saplings
        if self.age >= 12:
            if self.age >= 120:
                percent = 20
            else:
                percent = 10
            
        #check adjacent squares
        

# class Lumberjack:

    # def __init__(self):
        # self.position
        
    # def move

# class Bear:

    # def __init__(self):
        # self.position
        
class Forest:

    def __init__(self, n):
        #coordinates/objects in map: self.map[x][y][objects]
        self.map = [[[]] * n] * n
        self.maxSize = n
    
    def neighboring_cells(self, x, y):
        potential_vectors = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        cells = []
        
        for vector in potential_vectors:
            if 0 =< x + cell[0] and x + cell[0] < self.maxSize:
                if 0 =< y + cell[1] and y + cell[1] < self.maxSize:
                    cells.append((x + cell[0], y + cell[1]))
        return cells
    
    def spawn_object(self, obj, x, y):
        
        
    
    # def process_collision(self, obj1, obj2):
    
    
    # def process_month(self):
    
    
    # def process_year(self):
    
def main():
    f = Forest(10)
    print(f.map)
 
if __name__ == "__main__":
    main()