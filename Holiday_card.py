from graphics import *

win = GraphWin("My Holiday Card", 500, 500)

def main():
    
    
    
    width = 500
    height = 500
    draw_text()
    draw_snowman()
    

def draw_text():
    text = Text(Point(100,150), "Happy Holidays!")
    text.setSize(24)
    text.setStyle("bold")
    text.setFill("red")
    text.draw(win)
    

def draw_snowman():

    win.setBackground("Pink")  


    bottom = Circle(Point(250, 400), 100)  
    middle = Circle(Point(250, 275), 70)   
    top = Circle(Point(250, 180), 50)     
    bottom.setFill("white")
    middle.setFill("white")
    top.setFill("white")

   
    left_eye = Circle(Point(235, 170), 5)
    right_eye = left_eye.clone()  
    right_eye.move(30, 0)  
    left_eye.setFill("black")
    right_eye.setFill("black")


    button1 = Circle(Point(250, 235), 7)
    button2 = button1.clone() 
    button3 = button1.clone()
    button1.move(0, 26)
    button2.move(0, 65)
    button3.move(0, -35)
    button1.setFill("black")
    button2.setFill("black")
    button3.setFill("orange")

   
    left_arm = Line(Point(175, 275), Point(100, 250))
    right_arm = Line(Point(325, 275), Point(400, 250))

   
    hat_base = Rectangle(Point(200, 130), Point(300, 160))
    hat_top = Rectangle(Point(220, 100), Point(280, 130))
    hat_base.setFill("black")
    hat_top.setFill("black")

    bottom.draw(win)
    middle.draw(win)
    top.draw(win)
    left_eye.draw(win)
    right_eye.draw(win)
    button1.draw(win)
    button2.draw(win)
    button3.draw(win)
    left_arm.draw(win)
    right_arm.draw(win)
    hat_base.draw(win)
    hat_top.draw(win)

  
    win.getMouse()
    win.close()




if __name__ == "__main__":
    main()

