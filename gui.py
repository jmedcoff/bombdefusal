from appJar import gui
from logicizer import logicizer

# Setup
app = gui()
logic = logicizer()
app.setFont(16, font = "Courier")
app.setBg("Gray")
app.addLabel("title", logic.get_output())


# Logic
def bool2str(b):
    if b:
        return '1'
    else:
        return '0'


def btnpress(button):
    string = ['0']
    for j in b2 + b1:
        boolean = app.getCheckBox(j)
        string.append(bool2str(boolean))
    logic.evaluate(''.join(string))
    app.setLabel("title", labeltext(logic.get_output()))


def labeltext(n):
    if n == 0:
        return "Don't Cut!"
    if n == 1:
        return "Cut!"

# Part 1 Boxes
app.startLabelFrame("Preliminaries")
app.setSticky("ew")
b1 = ["Serial# last Digit Even", "Par. Port", "2+ Batteries"]
for i in b1:
    app.addCheckBox(i)
app.stopLabelFrame()

# Part 2 Boxes
app.startLabelFrame("Variables")
app.setSticky("ew")
b2 = ["Red", "Blue", "Star", "LED"]
for i in b2:
    app.addCheckBox(i)
app.stopLabelFrame()

app.addButton("Solve",btnpress)



app.go()
