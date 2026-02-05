#Drew Pickering, 203237@gscs.ca, functions and abstraction
def draw_square():
    line(10, 40, 60, 40)
    line(10, 90, 60, 90)
    line(60, 40, 60, 90)
    line(10, 90, 10, 40)
    
def draw_circle(x, y):
    ellipse(x, y, 80, 80)
    
def draw_concentric_circles(x, y):
    ellipse(x, y, 90, 90)
    ellipse(x, y, 60, 60)
    ellipse(x, y, 30, 30)
    
        



size(300, 300)
draw_square()
draw_circle(150, 80)
draw_concentric_circles(110, 250)
