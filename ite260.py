import turtle

T = turtle.Turtle()
kenshin= turtle.Screen()
kenshin.bgcolor('black')
T.color("green")

a = 0
b = 0

T.speed(0)
T.penup()
T.goto(0,200)
T.pendown()
while (True):
    T.forward(a)
    T.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    T.hideturtle()
kenshin.exitonclick()
turtle.done 