import turtle


# command
# beginfill, black
# circle, 20, 1, black
# endfill
# penup
# goto, 120, 0, 1, black
# pendown
# beginfill, black
# circle, 20, 1, black
# endfill
# penup
# goto, 150, 40, 1, black
# pendown
# beginfill, yellow
# goto, -30, 40, 1, black
# goto, -30, 70, 1, black
# goto, 60, 70, 1, black
# goto, 60, 100, 1, black
# goto, 90, 100, 1, black
# goto, 115, 70, 1, black
# goto, 150, 70, 1, black
# goto, 150, 40, 1, black
# endfill

# def main():
#     filename = input("Please enter drawing filename: ")
#     t = turtle.Turtle()
#     screen = t.getscreen()
#     file = open(filename, "r")
#     #============================================================#
#     # for line in file:
#     #     text = line.strip()
#     #     commandlist = text.split(",")
#     #     # print(commandlist)
#     #     command = commandlist[0]
#     #     # print(command)
#     #
#     #     if command == "goto":
#     #         x = float(commandlist[1])
#     #         y = float(commandlist[2])
#     #         width = float(commandlist[3])
#     #         color = commandlist[4].strip()
#     #         t.width(width)
#     #         t.pencolor(color)
#     #         t.goto(x, y)
#     #
#     #     elif command == "circle":
#     #         radius = float(commandlist[1])
#     #         width = float(commandlist[2])
#     #         color = commandlist[3].strip()
#     #         t.width(width)
#     #         t.pencolor(color)
#     #         t.circle(radius)
#     #
#     #     elif command == "beginfill":
#     #         color = commandlist[1].strip()
#     #         t.fillcolor(color)
#     #         t.begin_fill()
#     #
#     #     elif command == "endfill":
#     #         t.end_fill()
#     #
#     #     elif command == "penup":
#     #         t.penup()
#     #
#     #     elif command == "pendown":
#     #         t.pendown()
#     #
#     #     else:
#     #         print("Unknow command found in file:", command)
#     #============================================================#
#     # half a loop
#     #============================================================#
#     command = file.readline().strip()
#     while command != "":
#         if command == "goto":
#             x = float(file.readline())
#             y = float(file.readline())
#             width = float(file.readline())
#             color = file.readline().strip()
#             t.width(width)
#             t.pencolor(color)
#             t.goto(x, y)
#
#         elif command == "circle":
#             radius = float(file.readline())
#             width = float(file.readline())
#             color = file.readline().strip()
#             t.width(width)
#             t.pencolor(color)
#             t.circle(radius)
#
#         elif command == "beginfill":
#             color = file.readline().strip()
#             t.fillcolor(color)
#             t.begin_fill()
#
#         elif command == "endfill":
#             t.end_fill()
#
#         elif command == "penup":
#             t.penup()
#
#         elif command == "pendown":
#             t.pendown()
#
#         else:
#             print("Unknow command found in file:", command)
#         command = file.readline().strip()
#
#     file.close()
#
#     t.ht()
#     screen.exitonclick()
#     print("Program Execution Completed.")

# ===============================================#
# Graphic Command Classes
# ===============================================#
class GoToCommand(object):
    def __init__(self, x, y, width=1.0, color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return '<Command x="'+str(self.x)+'"  \
                         y="'+str(self.y)+'" \
                         width="'+str(self.width)+'" \
                         color="'+self.color+'">GoTo</Command>'


class CircleCommand(object):
    def __init__(self, radius, width=1.0, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)


class BeginFillCommand(object):
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()


class EndFillCommand(object):
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()


class PenUpCommand(object):
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()


class PenDownCommand(object):
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()


class PyList(object):
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c


# def main():
#     filename = input("Please enter the drawing filename: ")
#     t = turtle.Turtle()
#     screen = t.getscreen()
#     file = open(filename, "r")
#
#     graphicsCommands = PyList()
#
#
#     command = file.readline().strip()
#     while command != "":
#         if command == "goto":
#             x = float(file.readline())
#             y = float(file.readline())
#             width = float(file.readline())
#             color = file.readline().strip()
#             cmd = GoToCommand(x, y, width, color)
#             graphicsCommands.append(cmd)
#
#         elif command == "circle":
#             radius = float(file.readline())
#             width = float(file.readline())
#             color = file.readline().strip()
#             cmd = CircleCommand(radius, width, color)
#             graphicsCommands.append(cmd)
#
#         elif command == "beginfill":
#             color = file.readline().strip()
#             cmd = BeginFillCommand(color)
#             graphicsCommands.append(cmd)
#
#         elif command == "endfill":
#             cmd = EndFillCommand()
#             graphicsCommands.append(cmd)
#
#         elif command == "penup":
#             cmd = PenUpCommand()
#             graphicsCommands.append(cmd)
#
#         elif command == "pendown":
#             cmd = PenDownCommand()
#             graphicsCommands.append(cmd)
#
#         else:
#             print("Unknow command found in file:", command)
#
#         command = file.readline().strip()
#     for cmd in graphicsCommands:
#         cmd.draw(t)
#
#     file.close()
#     t.ht()
#     screen.exitonclick()
#     print("Program Execution Completed.")

def main():
    filename = "Command.XML"
    file = open(filename, "w")
    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    file.write('<GraphicsCommands>\n')
    graphicsCommands = PyList()
    graphicsCommands.append(GoToCommand(20, 21, 1.0, "black"))
    for cmd in graphicsCommands:
        file.write('  '+str(cmd)+"\n")
    file.write('</GraphicsCommands>\n')
    file.close()

if __name__ == "__main__":
    main()
