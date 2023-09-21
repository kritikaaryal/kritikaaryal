from stanfordkarel import *

"""
For this problem, Karel starts out
with an infinite number of beepers.
Your goal is to use nested while loops
to fill every space on the board with a
beeper.  Your code should work for any
size board. 

This time around, you should avoid
backtracking. Karel should only
visit every corner once.  
"""
     
    
def main():    
    put_beeper()
    movetowall()
    Turnandgo()
    movetowall()
    Turnandgo()
    movetowall()
    Turnandgo()
    movetowall()
    Turnandgo()
    movetowall()
    
def movetowall():
    while front_is_clear():
        move()
        put_beeper()    
    
def Turnandgo():
    if facing_east():
         turn_left()
         move()
         put_beeper()
         turn_left()
    else:
        turn_right()
        move()
        put_beeper()
        turn_right()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left() 


if __name__ == "__main__":
    run_karel_program("6x5")
    
  
        
        
