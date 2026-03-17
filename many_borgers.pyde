#Drew Pickering, 203237@gscs.ca, many_borgers


def setup():
    size (200, 300)


x = 0
z = 0
def keyPressed():
    global x
    global z
    if key == "p":
        x = x + 1
    if key == "o":
        x = x - 1
    if key == "b":
        z = z + 1
    if key == "n":
        z = z - 1

    
def draw():
    global x
    global z
    background(0)
    text ( x, 180, 30)
    text ( z, 170, 45)
    q = z * 12
    e = x * 8
    l =
    
    text ("hamburger pattie packages", 20, 30)
    text ("hamburger buns packages", 20, 45)
    text("total hamburgers", 20, 100)
    text(x * 8 , 90, 60)
    text(z * 12, 80, 75)
    text(l, 120, 100)
