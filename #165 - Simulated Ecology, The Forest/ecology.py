import random

class tree:   
    def __init__(self, age, x, y):
        #age in months, 12 months = 1 year
        self.age = age
        self.xPos, self.yPos = x, y
    
    def spawn_sapling(self, forest):
        #saplings cannot spawn other saplings
        if self.age >= 12:
            if self.age >= 120:
                percent = .2
            else:
                percent = .1
            
            if random() =< percent:
            
                #get neighbor cells
                neigbors = forest.neighbor_cells(self.xPos, self.yPos)
                
                #check for empty neighbor cells
                empty_cells = []
                for cell in neighbors:
                    x, y = cell[0], cell[1]
                    #empty cells return false
                    if not forest.map[x][y]:
                        empty_cells.append([x, y])

                #if there are empty neighbors, pick a random empty cell and add a sapling there
                if empty_cells:
                    cell_index = random.randint(0, len(empty_cells) - 1)
                    x_plant, y_plant = empty_cells[index][0], empty_cells[index][1]
                    forest.map[x_plant][y_plant].append(Tree(0, x_plant, y_plant))
                    
class Lumberjack:
    def __init__(self, x, y):
        self.xPos, self.yPos = x, y
        self.lumber = 0
        
    def move(self):
        encountered_tree = False
        
        
        
class Bear:
    def __init__(self, x, y):
        self.xPos, self.yPos = x, y
        
    def move(self):
        encountered_lumberjack = False
        
class Forest:
    def __init__(self, n):
        #coordinates/objects in map: self.map[x][y][objects]
        self.map = [[[]] * n] * n
        self.size = n
    
    #populates self with specified percentages of objects
    def populate(self): 
        #10% of forest is Lumberjacks; place each at a random, unoccupied cell
        for i in range(int(self.size * .1)):
            x, y = random.randint(0, self.size), random.randint(0, self.size)
            
            #re-randomize coordinates if Lumberjack already spawned at position
            while Lumberjack(x, y) in self.map[x][y]:
                x, y = random.randint(0, self.size), random.randint(0, self.size)
            
            #add Lumberjack to map
            self.map[x][y].append(Lumberjack(x, y))
    
        #50% of forest is regular Trees; place each at a random, unoccupied cell
        for i in range(int(self.size * .5)):
            x, y = random.randint(0, self.size), random.randint(0, self.size)
            
            #re-randomize coordinates if Tree already spawned at position
            while Tree(x, y) in self.map[x][y]:
                x, y = random.randint(0, self.size), random.randint(0, self.size)
            
            #add Tree to map
            self.map[x][y].append(Tree(12, x, y))

        
        #2% of forest is Bears; place each at a random, unoccupied cell
        for i in range(int(self.size * .02)):
            x, y = random.randint(0, self.size), random.randint(0, self.size)
            
            #re-randomize coordinates if Bear already spawned at position
            while Bear(x, y) in self.map[x][y]:
                x, y = random.randint(0, self.size), random.randint(0, self.size)
            
            #add Bear to map
            self.map[x][y].append(Bear(12, x, y))
    
    def neighbor_cells(self, x, y):
        potential_vectors = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        cells = []
        
        for vector in potential_vectors:
            if 0 =< x + cell[0] and x + cell[0] < self.maxSize:
                if 0 =< y + cell[1] and y + cell[1] < self.maxSize:
                    cells.append([x + cell[0], y + cell[1]])
        return cells 
    
    # def process_month(self):
        # scan through all elements of forest.map[x][y]
        # move all Lumberjacks, handling collisions with Bears and Trees
        # spawn all saplings
        # move all Bears, handling collisions with Lumberjacks
        # output monthly data
    
    # def process_year(self):
        # hire/fire Lumberjacks
        # add/remove bears
        # output annual data
    
def main():
    size = int(input("Forest size: "))
    time = int(input("Simulation time (months): "))
    f = Forest(size)
    f.populate()
    for month in range(time):
        f.process_month()
 
if __name__ == "__main__":
    main()