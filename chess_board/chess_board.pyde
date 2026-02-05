#Drew pickering, 203237@gscs.ca, chess_board

size (200, 200)

# all the white squares
def white_squares():
    fill (255)
    rect (0, 0, 50, 50)
    rect (100, 0, 50, 50)
    rect (50, 50, 50, 50)
    rect (150, 50, 50, 50)
    rect (0, 100, 50, 50)
    rect (100, 100, 50, 50)
    rect (50, 150, 50, 50)
    rect (150, 150, 50, 50)
    
# all the black squares
def black_squares():
    fill (0)
    rect (50, 0, 50, 50)
    rect (150, 0, 50, 50)
    rect (0, 50, 50, 50)
    rect (100, 50, 50, 50)
    rect (50, 100, 50, 50)
    rect (150, 100, 50, 50)
    rect (0, 150, 50, 50)
    rect (100, 150, 50, 50)
    
    
#calling the squares so they are painted in
white_squares()
black_squares()
          
