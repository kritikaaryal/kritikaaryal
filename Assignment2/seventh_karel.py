from stanfordkarel import *

"""
Keral is becoming an artist.
She wants to paint the outside 8x8 boarder
of the world DARK_GRAY, an middle 6x6 rignt
LIGHT_GRAY, an inner 4x4 ring PINK
and a central 2x2 square RED. Use
for loops to accomplish this.  Be sure
to define functions to minimize as much
redundancy as possible
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def outer_boarder():
    fill_boarder()
  
def main():
    outer_boarder()
    middle_area()
    inner()
    center()

  
def outer_boarder():
    while front_is_clear():
        paint_corner(DARK_GRAY)
        move()
        paint_corner(DARK_GRAY)
    turn_left()
    while facing_north() and front_is_clear():
        move()
        paint_corner(DARK_GRAY)
    turn_left()
    while front_is_clear():
        paint_corner(DARK_GRAY)
        move()
        paint_corner(DARK_GRAY)
    turn_left()
    paint_cornerD(6)
    turn_left()
def middle_area():
    paint_cornerN(6)
    turn_left()
    paint_cornerN(5)
    turn_left()
    paint_cornerN(5)
    turn_left()
    paint_cornerN(4)
    turn_left()
def inner():
    paint_cornerP(4)
    turn_left()
    paint_cornerP(3)
    turn_left()
    paint_cornerP(3)
    turn_left()
    paint_cornerP(2)
    turn_left()

def center():
    paint_cornerR(2)
    turn_left()
    paint_cornerR(1)
    turn_left()
    paint_corner(RED)
    move()
    paint_corner(RED)
    
    
    
def paint_cornerD(n:int):
    for i in range(n):
        move()
        paint_corner(DARK_GRAY)
def paint_cornerN(n:int):
    for i in range(n):
        move()
        paint_corner(LIGHT_GRAY)
    
    
def paint_cornerP(n:int):
    for i in range(n):
        move()
        paint_corner(PINK)
def paint_cornerP(n:int):
    for i in range(n):
        move()
        paint_corner(PINK)
def paint_cornerR(n:int):
    for i in range(n):
        move()
        paint_corner(RED)
        
    

    
    

    
    
    
    
        
    

    
                     
            
                
    


    
    
    
    
    
     
    
    
    


if __name__ == "__main__":
    run_karel_program("8x8")