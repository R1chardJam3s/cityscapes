from building_set import BuildingSet

# make sure w / DIMENSION is a whole number
w, h = 1000, 600

# background gradient colours
T_COLOURS = [color(153, 213, 247), color(222, 144, 55), color(235, 113, 141)]
B_COLOURS = [color(242, 172, 229), color(235, 231, 42), color(67, 247, 241)]

# BuildingSet(y, DIMENSION, MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT, colour) - recommended keeping MIN_WIDTH to 1
def setup():
    global b_ground, m_ground, f_ground
    size(w, h)
    b_ground = BuildingSet(h - 100, 5, 1, 2, 30, 35, color(150, 130))
    m_ground = BuildingSet(h - 60, 10, 1, 3, 14, 18, color(80, 220))
    f_ground = BuildingSet(h, 25, 1, 4, 4, 8, color(20, 255), True)
    noLoop()
    
def draw():
    setGradient()
    b_ground.display()
    m_ground.display()
    f_ground.display()
    
    save("Examples/out.png")
    
def setGradient():
    noFill()
    tc = T_COLOURS[ceil(random(-1,2))]
    bc = B_COLOURS[ceil(random(-1,2))]
    
    for i in range(0, h + 1):
        inter = map(i, 0, h, 0, 1)
        c = lerpColor(tc, bc, inter)
        stroke(c)
        line(0, i, w, i)
