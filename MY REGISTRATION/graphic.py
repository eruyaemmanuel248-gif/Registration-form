import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("darkblue")
pen.pensize(2)
pen.speed(10)

for i in range(5):
    pen.forward(150)
    pen.right(144)
    turtle.done()