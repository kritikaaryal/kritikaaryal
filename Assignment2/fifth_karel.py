from stanfordkarel import *

"""
For this problem, a set of
beepers have been arranged in
the world to form a pyramid.
Your goal is to pick them all up
and then pile them into a single
stack in the bottom right corer of
the board.  Make use of for and while
loops to make your code as concise as
possible.  
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def moveN(n:int):
    for i in range(n):
        move()
def rotate():
    turn_left()
    turn_left()
def pick_beeperN(n:int):
    for i in range(n):
        move()
        pick_beeper()
def put_beeperN(n:int):
    for i in range(n):
        put_beeper()
    
    
def main():
    pick_beeperN(7)
    while facing_east():
        turn_left()
    move()
    turn_left()
    pick_beeperN(5)
    while facing_west():
        turn_right()
        move()
        turn_right()
    pick_beeperN(3)
    while facing_east():
        turn_left()
        move()
        turn_left()
        move()
        pick_beeper()
    while facing_west():
        turn_left()
        turn_left()
        moveN(4)
        turn_right()
        moveN(3)
        turn_left()
        put_beeperN(16)
      
        
        
        
        
        
        
        
    
    
    
    
        
        
        
    
    
    
  
       
   


if __name__ == "__main__":
    run_karel_program("fifth_world")
    
