from building import Building

class BuildingSet(object):
    
    def __init__(self, y, DIMENSION, MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT, colour, windows=False):
        
        self.total = width / DIMENSION
        self.widths = [] 
        
        assigned = 0
        cur = MIN_WIDTH
        while assigned < self.total:
            if self.total - assigned < MIN_WIDTH:
                break
            if random(0,1) < 0.5:
                if cur == MAX_WIDTH:
                    assigned += cur
                    self.widths.append(cur)
                    cur = MIN_WIDTH
                else:
                    cur += 1
            else:
                assigned += cur
                self.widths.append(cur)
                cur = MIN_WIDTH
        
        self.buildings = []
        _x = 0
        for w in self.widths:
            self.buildings.append(Building(_x, y, DIMENSION, w, MIN_HEIGHT, MAX_HEIGHT, colour, windows))
            _x += DIMENSION * w        
                
    def display(self):
        for building in self.buildings:
            building.display()
        
