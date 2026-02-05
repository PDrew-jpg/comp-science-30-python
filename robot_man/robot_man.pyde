#Drew pickering, 203237@gscs.ca, robot_man

size (300,300)

def draw_legs():
    fill (187)
    rect (160, 170, 30, 90)
    fill(0, 65, 78)
    rect( 150, 250, 60, 30)
    fill(187)
    rect (90,170,30,90)
    fill(0, 65, 78)
    rect(70, 250, 60, 30)
    
def draw_torso():
    fill(187)
    rect(85, 100, 110, 90)
    fill(0, 255, 0)
    ellipse(150, 130, 10, 10)
    fill(255, 0, 0)
    ellipse(110, 130, 10, 10)
    fill(0, 0, 255)
    ellipse(180, 130, 10, 10)
    
def draw_head():
    fill(187)
    rect(105, 50, 70, 50)
    ellipse(105, 50, 40, 40)
    ellipse(185, 50, 40, 40)
    fill(219, 215, 0)
    rect(120, 90, 50, 10)
    fill( 219, 215, 0)
    ellipse(115, 70, 30, 30)
    ellipse(160, 70, 30, 30)

def draw_arms():
    fill(187)
    rect(190, 100, 30, 60)
    rect(60, 100, 30, 60)

def draw_robot():
    draw_arms()
    draw_legs()
    draw_head()
    draw_torso()




draw_robot()
