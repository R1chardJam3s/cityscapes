from roof import Roof
from window import Window

class Building(object):
    
    def __init__(self, x, y, DIMENSION, WIDTH, MIN_HEIGHT, MAX_HEIGHT, colour, hasWindows):
        
        self.w = WIDTH
        self.h = round(random(MIN_HEIGHT, MAX_HEIGHT))
        
        self.hasWindows = hasWindows
        
        self.building = createShape()
        self.building.beginShape()
        self.building.fill(colour)
        self.building.noStroke()
        self.building.vertex(x, y)
        self.building.vertex(x + (self.w * DIMENSION), y)
        self.building.vertex(x + (self.w * DIMENSION), y - (self.h * DIMENSION))
        self.building.vertex(x, y - (self.h * DIMENSION))
        self.building.endShape(CLOSE)
        
        self.roof = Roof(x, y - (self.h * DIMENSION), self.w * DIMENSION, colour)
        
        if self.hasWindows:
            self.windows = []
            for ww in range(0, self.w):
                for wh in range(0, floor(self.h) + 1):
                    self.windows.append(Window(x + (ww * DIMENSION), y - (wh * DIMENSION), DIMENSION, colour))
        
    def display(self):
        shape(self.building)
        self.roof.display()
        if self.hasWindows:
            for window in self.windows:
                window.display()
        
