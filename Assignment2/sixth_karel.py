from stanfordkarel import *

"""
For this problem, Karel starts out
with an infinite number of beepers.
Your goal is to use nested while loops
to fill every space on the board with a
beeper.  Your code should work for any
size board. 

Note: There is a more efficient way
to solve this problem using a conditional
structure called an if statement. For this
exercise, you should try to only use while
loops. 
"""
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    if front_is_blocked():
        put_beeper()
        turn_around()
    while front_is_clear():
        move()
    turn_right()
        
        
        
def main():
    fill_row()
    while front_is_clear():
        move()
        turn_right()
        fill_row()
    
    
    
    
    
    


if __name__ == "__main__":
    run_karel_program("6x5")
    
