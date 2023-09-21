from stanfordkarel import *

"""
Karel is now in a maze.  Write
code to keep one hand on the right
hand wall so that Karel can navigate
the maze until she reaches the
red finish square. 
"""
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def keep_moving():
    while front_is_clear():
        move()

def go():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif left_is_clear():
        turn_left()
        move()
    elif front_is_blocked() and right_is_blocked():
        turn_around()


def main():
    while not corner_color_is(RED):
        go()


if __name__ == "__main__":
    run_karel_program("eighth_world")