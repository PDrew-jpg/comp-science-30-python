#Drew Pickering, 203237@gscs.ca, pin_the_tail_on_the_donkey

def setup():
    size (500, 500)
    background(195)

    
  # draws the donkeys legs  
def draw_legs():
    fill(225, 110, 0)
    rect( 120, 170, 30, 100)
    rect( 140, 170, 30, 100)
    
    rect( 250, 170, 30, 100)
    rect( 270, 170, 30, 100)
    
# draws the donkey's body neck ,and head
def draw_body():
    ellipse(210, 150, 210, 90)
    ellipse(120, 110, 50, 115)
    ellipse(90, 70, 90, 40)
    ellipse(120, 50, 20, 50)
    ellipse(130, 50, 20, 50)

#for when you click the mouse it adds a tail on your mouses position
def mouseClicked():
    fill(225, 150, 0)
    rect( mouseX, mouseY, 20, 50)
    fill(225, 0, 0)
    ellipse (mouseX, mouseY, 10,10) 

#romoves alltails on screen when a key is pressed
def keyPressed():
    background(195) 

# constitaly draws the donkey.
def draw():
    draw_legs()
    draw_body()
