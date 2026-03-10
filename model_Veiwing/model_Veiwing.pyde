#Drew Pickering, 203237@gscs.ca, Model_Viewing

# thanks ms cheston for the help

# all global variables being stated at the start
x = -100
y = -100
o = 225
z = 255
def setup():
    size (300, 300)
    return

# all key binds for increasing and decreaseing the colors
# by a value of 50
def keyPressed():
    global o
    global z
    if key == "b":
        o = o + 50
        fill(0, 0, o)
    if key =="n":
        o = o - 50
        fill(0, 0, o)
    if key =="r":
        z = z + 50
    if key =="d":
        z = z - 50
    
    
       
# keeping the background the same color and making the circle go where the mouse is
# at 60 fps
def draw():
    global z
    global x
    global y 
    background(z, 0, 0)
    ellipse(x, y, 30, 30)

# when the mouse is clicked the circle moves to where the mouse is
# without changing its shade or hue of its color 
def mouseClicked():
    global x
    global y
    x = mouseX
    y = mouseY
    
