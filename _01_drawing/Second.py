import turtle


nathanael = turtle.Turtle()
nathanael.shape("turtle")
nathanael.color("green")
nathanael.speed(0)

def concentricShapes():
    nathanael.circle(radius=6, extent=360, steps=3)
    nathanael.circle(radius=6, extent=360, steps=10)

def makeTriangle():
    for i in range(3):
        nathanael.right(120)
        for j in range(10):
            concentricShapes()
            nathanael.forward(5)

nathanael.penup()
nathanael.goto(0, -300)
nathanael.pendown()

for i in range (20):
    if nathanael.ycor() < 50:
        nathanael.right((i+1)*10)
        makeTriangle()
        for j in range(50):
            nathanael.forward(10)
            concentricShapes()
            if nathanael.xcor() < 0:
                nathanael.right(30)
            else:
                nathanael.left(45)
            nathanael.backward(50)
    else:
        for j in range(10):
            makeTriangle()
            nathanael.right(120)
            nathanael.forward(10)

turtle.done()