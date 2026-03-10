#Drew Pickering, 203237#gscs.ca, Robot_man_Home

#draws the grass and adds the lake
def setup():
    size(400, 400)
    background(0, 128, 0)
    fill( 0, 218, 228)
    ellipse(210, 270,110, 50)
    
# makes tree1    
def tree1():
    fill(190, 100, 90)
    rect(120, 190, 10, 30)
    fill(0, 2222, 0)
    ellipse(125, 180, 30, 30)
    
def tree2():
    fill(190, 100, 90)
    rect(330, 180, 10, 30)
    fill(0, 2222, 0)
    ellipse(335, 170, 30, 30)
    
def tree3():
    fill(190, 100, 90)
    rect(50, 20, 10, 30)
    fill(0, 2222, 0)
    ellipse(55, 10, 30, 30)
    
def tree4():
    fill(190, 100, 90)
    rect(310, 300, 10, 30)
    fill(0, 2222, 0)
    ellipse(315, 290, 30, 30)
    
def tree5():
    fill(190, 100, 90)
    rect(150, 360, 10, 30)
    fill(0, 2222, 0)
    ellipse(155, 350, 30, 30)
    
def tree6():
    fill(190, 100, 90)
    rect(50, 300, 10, 30)
    fill(0, 2222, 0)
    ellipse(55, 290, 30, 30)

#combines all trees into one variable so its cleaner
def trees():
    tree1()
    tree2()
    tree3()
    tree4()
    tree5()
    tree6()
    
#makes the white base of the house
def housebase():
    fill(285, 285, 285)
    rect (190, 120, 70, 50)

#makes the roof of the house
def roof():
    fill(0, 0, 225)
    triangle(191, 120, 225, 90, 259, 120)

#makes the door of the house
def door():
    fill(225, 0, 0)
    rect(215, 140, 20, 30)

#combines all the elements of the house into one
def house():
    housebase()
    roof()
    door()

#draws the house and trees as defined above
def draw():
    trees()
    house()





    
