#Drew Pickering, 203237@gscs.ca, night_to_day_cycle
def setup():
    size(300, 300)
    background(0, 175, 225)
    frameRate(10)

#when a key is not pressed i redraws everything back to its origonal colors
def draw():
    background(0, 175, 225)
    fill(2250, 2250, 0)
    ellipse(150, 20, 50, 50)
    fill (155, 110, 0)
    rect(-15, 270, 390, 70)
    fill (225, 120, 0)
    rect(50, 240, 30, 30)
    fill (225, 0, 200)
    rect( 120, 240, 30, 30)
    fill (0, 225, 0)
    rect ( 200, 240, 30, 30)
    
    
    
#when a key i pressed down it darkens all the colors by 30
def keyPressed():
    background(0, 145, 195)
    fill(2255, 2255, 2255)
    ellipse(150, 20, 50, 50)
    fill (125, 80, 0)
    rect(-15, 270, 390, 70)
    fill (195, 90, 0)
    rect(50, 240, 30, 30)
    fill (195, 0, 170)
    rect( 120, 240, 30, 30)
    fill (0, 195, 0)
    rect ( 200, 240, 30, 30)
