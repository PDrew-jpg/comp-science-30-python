#Drew Pickering, 203237@gscs.ca, Cube_of_a_number
def setup():
    size (500, 500)
    background(0, 0) # makes the screen a black background and makes the R key 
    text("R = reset", 450, 10)# the reset buton

#reset the string
number = ""
output = ""
#when a key is pressed it adds that key into the string
def keyPressed():
    global number
    number = number + key
    # a reset button that crashes the program
    if key == "r":
        output = ""
        number = ""
    # when the mouse is clicked it runs the calculation and gives you the awnser
def mouseClicked():
    background (0, 0)
    text("R = reset", 450, 10)
    global number
    global output
        # turns the string to an integer
    output = int(number) ** 3
    

    #keeps the number and output drawn so its always there
def draw():
    global output
    global number
    text(number, 20, 20)
    text(output, 30, 30)

    
