from stanfordkarel import *

"""
This is an example program
that picks up several beepers
and moves them all to the same
location
"""

def main():
    """Karel code goes here!"""
    move()
    pick_beeper()
    turn_left()
    move()
    pick_beeper()
    turn_left()
    move()
    pick_beeper()
    move()
    pick_beeper()
    turn_left()
    move()
    pick_beeper()
    move()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    turn_left()
    move()


if __name__ == "__main__":
    run_karel_program("example_world")