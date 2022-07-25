class Window(object):
    
    COLOURS = [color(209, 219, 134), color(116, 155, 161)]
    
    def __init__(self, x, y, DIMENSION, colour):
        
        self.rand = random(0, 1)
        self.colours = Window.COLOURS + [colour]
        self.c = self.colours[floor(random(len(self.colours)))]
        self.step = DIMENSION / 5
        self.window = createShape()
        self.window.beginShape(QUADS)
        self.window.fill(self.c, random(0, 255))
        self.window.noStroke()
        
        if self.rand < 0.25: #open
            self.window.vertex(x + self.step, y + self.step)
            self.window.vertex(x + (self.step * 4), y + self.step)
            self.window.vertex(x + (self.step * 4), y + (self.step * 4))
            self.window.vertex(x + self.step, y + (self.step * 4))
        if self.rand < 0.5: # hor
            self.window.vertex(x + self.step, y + self.step)
            self.window.vertex(x + (self.step * 4), y + self.step)
            self.window.vertex(x + (self.step * 4), y + (self.step * 2))
            self.window.vertex(x + self.step, y + (self.step * 2))
            
            self.window.vertex(x + self.step, y + (self.step * 3))
            self.window.vertex(x + (self.step * 4), y + (self.step * 3))
            self.window.vertex(x + (self.step * 4), y + (self.step * 4))
            self.window.vertex(x + self.step, y + (self.step * 4))
        elif self.rand < 0.75: # ver
            self.window.vertex(x + self.step, y + self.step)
            self.window.vertex(x + (self.step * 2), y + self.step)
            self.window.vertex(x + (self.step * 2), y + (self.step * 4))
            self.window.vertex(x + self.step, y + (self.step * 4))
            
            self.window.vertex(x + (self.step * 3), y + self.step)
            self.window.vertex(x + (self.step * 4), y + self.step)
            self.window.vertex(x + (self.step * 4), y + (self.step * 4))
            self.window.vertex(x + (self.step * 3), y + (self.step * 4))
        else: # cross
            self.window.vertex(x + self.step, y + self.step)
            self.window.vertex(x + (self.step * 2), y + self.step)
            self.window.vertex(x + (self.step * 2), y + (self.step * 2))
            self.window.vertex(x + self.step, y + (self.step * 2))
            
            self.window.vertex(x + (self.step * 3), y + self.step)
            self.window.vertex(x + (self.step * 4), y + self.step)
            self.window.vertex(x + (self.step * 4), y + (self.step * 2))
            self.window.vertex(x + (self.step * 3), y + (self.step * 2))
            
            self.window.vertex(x + self.step, y + (self.step * 3))
            self.window.vertex(x + (self.step * 2), y + (self.step * 3))
            self.window.vertex(x + (self.step * 2), y + (self.step * 4))
            self.window.vertex(x + self.step, y + (self.step * 4))
            
            self.window.vertex(x + (self.step * 3), y + (self.step * 3))
            self.window.vertex(x + (self.step * 4), y + (self.step * 3))
            self.window.vertex(x + (self.step * 4), y + (self.step * 4))
            self.window.vertex(x + (self.step * 3), y + (self.step * 4))
            
        self.window.endShape()
        
    def display(self):
        shape(self.window)
