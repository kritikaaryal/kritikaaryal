from graphics import *

def get_nickname() -> str:
    win = GraphWin("GrotonChat 🚫🦁", 500, 500)
    e = Entry(Point(300,250),20)
    e.setFill("maroon")
    e.draw(win)
    t = Text(Point(120,250), "Enter a Nickname:")
    t.setFill("#cf3441")
    t.setSize(20)
    t.draw(win)
    while win.checkKey() != "Return":
        pass
    nickname = e.getText()
    win.close()
    return nickname[0:12]

def run(inbound_messages, outbound_messages):
    win = GraphWin("GrotonChat 🚫🦁", 610, 400)
    e = Entry(Point(390,360),50)
    e.setFill("maroon")
    e.draw(win)
    b = Rectangle(Point(15,10), Point(600, 330))
    b.setFill("maroon")
    b.draw(win)
    t = Text(Point(300, 170), "")
    t.setFill("pink")
    t.setSize(16)
    t.setFace("courier")
    t.draw(win)
    label = Text(Point(110, 360), "Enter your message here:")
    label.setSize(16)
    label.draw(win)
    displayed_messages = []
    while True:
        key = win.checkKey()
        if key == "Return":
            outbound_messages.append(e.getText())
            e.setText("")
        while len(inbound_messages) > 0:
            displayed_messages.append(inbound_messages.pop(0))
            if(len(displayed_messages) > 15):
                displayed_messages.pop(0)
            t.setText("\n".join(displayed_messages))