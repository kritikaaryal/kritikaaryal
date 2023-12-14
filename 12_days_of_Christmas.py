from graphics import*

verses = ['A partridge in a pear tree.', 'two turtle doves and','three French hens','four calling birds','five golden rings','six geese a-laying','seven swans a-swimming','eight maids a-milking','nine ladies dancing','ten lords a-leaping','eleven pipers piping','twelve drummers drumming']
    
def verse(i, win):
    first_verse = Text(Point(250, 200), verses[i - 1])
    first_verse.draw(win)
    win.getMouse()
    first_verse.undraw()
    first_verse.setSize(15)

    if i != 1:
        return verse(i - 1, win)


def add_christmas_tree(win):
    tree = Polygon(Point(150, 350), Point(250, 50), Point(350, 350))
    tree.setFill('green')
    tree.draw(win)

    trunk = Rectangle(Point(220, 350), Point(280, 400))
    trunk.setFill('brown')
    trunk.draw(win)


def add_star(win):
    star = Polygon(Point(250, 50), Point(230, 100), Point(200, 100), Point(225, 125),
                   Point(210, 170), Point(250, 140), Point(290, 170), Point(275, 125),
                   Point(300, 100), Point(270, 100))
    star.setFill('yellow')
    star.draw(win)
    
def draw_text(win):
    text = Text(Point(100,150), "🎅🤶❄⛄🎄🎁")
    text.setSize(30)
    text.setStyle("bold")
    text.setFill("red")
    text.draw(win)
def draw_2(win):
    text = Text(Point(390,150), "✨🥣🎶👼🦌🛷")
    text.setSize(30)
    text.setStyle("bold")
    text.setFill("red")
    text.draw(win)
    
    


def main():
    win = GraphWin("12 Days of Christmas", 500, 500)
    win.setBackground('red')

    add_christmas_tree(win)
    add_star(win)
    draw_text(win)
    draw_2(win)

    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'tenth', 'eleventh', 'twelfth']
    for i in range(1, 13):
        message = Text(Point(250, 250), "On the " + days[i - 1] + " day of Christmas, \n My true love gave to me...")
        message.setSize(15)  
        message.draw(win)
        win.getMouse()
        message.undraw()
        verse(i, win)

    win.close()


main()