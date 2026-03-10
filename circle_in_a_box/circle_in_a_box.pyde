#Drew Pickering, 203237@gscs.ca, circle_in_a_box

# all variables used in this code
d = 50
border = 50
border2 = 350
border3 = 75
border5 = 225
border6 = 100


# sets up the border size
def setup():
    size(400, 300)
    noStroke()
    
    #defines the border limits for the circile x axis
def circle_x(x, border, diameter):
    new_q = min(x, border2-circle_radius(diameter))
    return max(border3, new_q)
    
    #defines the border limits on the y axis
def circle_y(y, border, diameter):
    new_t = max(y, border6-circle_radius(diameter))
    return min(border5, new_t)

    

#the circiles radius
def circle_radius(diameter):
    return diameter/2

def draw():
    background(0,0,0)
    fill(0,0,221)
    global border
    rect (0, 0, border, height)
    rect (350, 0, border, height)
    
    rect (0, 250, width, border)
    rect (0, 0, width, border)
    fill (225, 225, 0)
    global d
    ellipse(circle_x(mouseX, border, d) ,circle_y(mouseY, border, d), d, d)
