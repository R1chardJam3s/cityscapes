class Roof(object):
    
    def __init__(self, x, y, WIDTH, colour):
        type = ceil(random(0,4))
        self.roof = createShape()
        self.roof.beginShape()
        self.roof.fill(colour)
        self.roof.noStroke()
        self.roof.strokeJoin(BEVEL)
        self.roof.vertex(x, y)
        self.roof.vertex(x + WIDTH, y)
        if type == 1:
            self.roof.vertex(x + (WIDTH / 2), y - (WIDTH / 4))
        elif type == 2:
            self.roof.vertex(x + WIDTH, y - (WIDTH / 4))
        elif type == 3:
            self.roof.vertex(x, y - (WIDTH / 4))
        else:
            self.roof.vertex(x + WIDTH, y - (WIDTH / 8))
            self.roof.vertex(x, y - (WIDTH / 8))
        self.roof.endShape(CLOSE)
    
    def display(self):
        shape(self.roof)
