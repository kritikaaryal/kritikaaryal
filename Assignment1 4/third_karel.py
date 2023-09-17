from stanfordkarel import *

"""
For this problem, the default
world contains a smily face.
However, the face has red eyes,
which makes it look demonic.
Your goal is to paint the face's
eye's blue and then move Karel
back to where it started.
You may use the following
functions:

turn_left()
move()
paint_corner(BLUE)
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def moveN(n:int):
    for i in range(n):
        move()
    

def main():
    move()
    move()
    turn_left()
    moveN(5) 
    paint_corner(BLUE)
    turn_right()
    moveN(3)
    paint_corner(BLUE)
    turn_right()
    moveN(5)
    turn_right()
    moveN(5)
    turn_left()
    turn_left()
    
    
    


if __name__ == "__main__":
    run_karel_program("third_world")