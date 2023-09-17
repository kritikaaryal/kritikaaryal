from stanfordkarel import *

"""
For this problem, there
are 8 colored squares
and 8 beepers on the map.
Your job is to move the
beepers so that there is one
beeper on each colored square.
Try to do this with as few
lines of code as possible.
You may use any of the following
functions:

turn_left()
move()
pick_beeper()
put_beeper()
"""
def moveN(n:int):
    for i in range(n):
        move()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    turn_left()
    moveN(8)
    turn_right()
    moveN(2)
    pick_beeper()
    pick_beeper()
    moveN(2)
    turn_right()
    move()
    pick_beeper()
    pick_beeper()
    turn_left()
    moveN(2)
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    moveN(2)
    turn_left()
    moveN(6)
    pick_beeper()
    pick_beeper()
    pick_beeper()
    turn_left()
    moveN(3)
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    moveN(2)
    pick_beeper()
    turn_left()
    move()
    turn_left()
    moveN(2)
    put_beeper()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


if __name__ == "__main__":
    run_karel_program("fourth_world")
