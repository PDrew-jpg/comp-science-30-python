#Drew Pickering, 203237@gscs.ca, circle_mouse

#setup with screen size and sets framerate
def setup():
    size (1000, 1000)
    frameRate(110 )


    #draws the ellipses on the mouses current position
def draw():
    background(210)
    fill(0, 89, 76)
    ellipse(mouseX,mouseY, 100, 100)
    fill(0, 23, 123)
    ellipse(mouseX, mouseY, 50, 50)
    
    


    
    

            
