#Drew Pickering, 203237@gscs.ca, weight_scale

# all global variables defined here
coin1x = 315
coin1y = 445
coin2x = 265
coin2y = 440
coin3x = 225
coin3y = 437
kg1 = 1
kg2 = 2
kg3 = 3

# the setup makess the size of the page
def setup():
    size(800, 800)

    #all key presses are defined here
def keyPressed():
    # when key 1 is pressed it changes its X and Y positions to the cursours X and Y position
        if key == "1":
            global coin1x
            global coin1y
            coin1x = mouseX
            coin1y = mouseY
    # when key 2 is pressed it changes its X and Y positions to the cursours X and Y position
        if key =="2":
            global coin2x
            global coin2y
            coin2x = mouseX
            coin2y = mouseY
    # when key 3 is pressed it changes its X and Y positions to the cursours X and Y position
        if key =="3":
            global coin3x
            global coin3y
            coin3x = mouseX
            coin3y = mouseY
    # where everything happens
def draw():
# calls upon the global variables
    global coin2y
    global coin2x
    global coin1x
    global coin1y
    # turns an image file into a variable
    img = loadImage("weight scale.jpeg")
    # makes that image that background
    image(img, 0, 0)
    # drawing all the coins 
    fill(250, 190, 0)
    ellipse(coin1x, coin1y, 20, 10)
    fill(180)
    ellipse(coin2x, coin2y, 20, 20)
    fill(180, 70, 0)
    ellipse(coin3x, coin3y, 20, 30)
        
    # all if statements that include the coin1's X axis position
    #look to see if coin1's X and coin2's X is greater than 400 and coin3's X is less than 400
    if coin1x < 400 and coin2x < 400 and coin3x < 400:
        # if that statement is true then it prints the text below
        text ("weight is unbalanced", 120, 10)
        
    #look to see if coin1's X and coin2's X is less than 400
    if coin1x < 400 and coin2x < 400 and coin3x > 400:
        # if that statement is true then it prints the text below
        text("weight is balanced", 120, 10)
        
    #look to see if coin1's X and coin3's X is greater than 400
    if coin1x > 400 and coin3x > 400:
        # if that statement is true then it prints the text below
        text("weight is unbalanced", 120, 10)
        
    #look to see if coin1's X and coin3's X is less than 400
    if coin1x < 400 and coin3x < 400:
        # if that statement is true then it prints the text below
        text("weight is unbalanced", 120, 10)
        
#look to see if coin1's X and coin3's X is greater than 400  
    if  coin2x > 400 and coin1x > 400:
        # if that statement is true then it prints the text below
        text("weight is balanced", 120, 10)
    
    # the if statements for coin2's X axis and coin3's X axis

    # checks if coinx's X and coin2's X is greater than 400
    if coin2x >400 and coin3x > 400:
        # if that statement is true then it prints the text below
        text("weight is unbalanced", 120, 10)
        
    #checks to see if coin3's X and coin2's X if less than 400
    if coin2x <400 and coin3x < 400:
        # if that statement is true then it prints the text below
        text("weight is unbalanced", 120, 10)

    
