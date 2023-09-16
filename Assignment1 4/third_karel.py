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

def main():
    move()
    move()
    turn_left()
    move()
    move()
    move()
    move()
    move()
    paint_corner(BLUE)
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    move()
    paint_corner(BLUE)
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    move()
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    move()
    move()
    move()
    turn_left()
    turn_left()
    
    
    


if __name__ == "__main__":
    run_karel_program("third_world")