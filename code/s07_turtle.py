import turtle

#t = turtle.Turtle()
#t.speed(5)

def draw_square(turtle_obj, size = 100):
    """Draws a square using the Turtle module"""
    for i in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)

def draw_spiral(t):
    """
    Draw one square, turn a angle, then draw another square and so on
    """
    for i in range(36):
        draw_square(t, 50)
        t.left(10)

def main():
    t = turtle.Turtle()
    t.speed(0)
    #draw_square(t)
    #draw_square(t, size=50)
    draw_spiral(t)
    turtle.mainloop()

#turtle.done() #makes sure the turtle graphics window stays open until you close it
turtle.mainloop() #this is the same as turtle.done() but it is more cross-platform compatible