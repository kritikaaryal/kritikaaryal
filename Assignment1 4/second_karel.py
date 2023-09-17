from stanfordkarel import *

"""
For this problem, your goal is to
move the beeper to the designated
red square. You may use the following
commands:

turn_left()
move()
pick_beeper()
put_beeper()
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def main():
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()
    put_beeper()


if __name__ == "__main__":
    run_karel_program("second_world")
    
