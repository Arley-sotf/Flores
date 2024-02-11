import turtle
t = turtle.Turtle()
t.pensize(3)

turtle.bgcolor("black")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.pencolor("#8B0000")
t.fillcolor("red")

go(24, 280)

t.begin_fill()
t.seth(120)
t.circle(30,120)
t.end_fill()

go(0, 275)

t.begin_fill()
t.seth(135)
t.circle(50,65)
t.circle(10,75)
t.forward(20)
t.end_fill()

go(-48, 255)

t.begin_fill()
t.seth(45)
t.circle(-110,55)
t.circle(-15,75)
t.seth(250)
t.forward(20)
t.end_fill()

go(-70, 200)

t.begin_fill()
t.goto(-70, 227.5)
t.seth(130)
t.circle(50,55)
t.circle(15,75)
t.seth(290)
t.forward(10)
t.end_fill()

go(60, 200)

t.begin_fill()
t.goto(60, 227.5)
t.seth(50)
t.circle(-50,55)
t.circle(-15,75)
t.seth(250)
t.forward(10)
t.end_fill()

go(12, 210)

t.begin_fill()
t.goto(12, 245)
t.seth(135)
t.circle(110,55)
t.circle(8,100)
t.seth(275)
t.circle(50,40)
t.seth(300)
t.circle(-30,45)
t.seth(270)
t.forward(30)
t.end_fill()

go(-53, 100)

t.begin_fill()
t.goto(-53, 200)
t.seth(60)
t.circle(-160,55)
t.circle(-12,60)
t.seth(260)
t.circle(-50,30)
t.seth(255)
t.circle(60,45)
t.end_fill()

go(0, 100)

t.begin_fill()
t.seth(90)
t.circle(130,65)
t.seth(158)
t.forward(52)
t.seth(230)
t.circle(10,90)
t.seth(310)
t.circle(-140,25)
t.seth(270)
t.circle(100,85)
t.end_fill()

go(-10, 100)

t.begin_fill()
t.seth(90)
t.circle(-130,65)
t.seth(22)
t.forward(52)
t.seth(310)
t.circle(-10,90)
t.seth(230)
t.circle(140,25)
t.seth(270)
t.circle(-100,85)
t.end_fill()

t.pencolor("#196F3D")
t.fillcolor("green")

go(15, -5)

t.begin_fill()
t.seth(70)
t.circle(-90, 60)
t.seth(300)
t.forward(10)
t.seth(20)
t.forward(35)
t.seth(280)
t.forward(10)
t.seth(0)
t.forward(25)
t.seth(258)
t.forward(25)
t.seth(325)
t.forward(10)
t.seth(240)
t.forward(25)
t.seth(325)
t.forward(10)
t.seth(250)
t.circle(-85, 110)
t.end_fill()

go(15, -35)
t.seth(40)
t.circle(-210, 25)
t.seth(21)
t.circle(140, 26)

go(10, 70)

t.begin_fill()
t.seth(10)
t.circle(90, 70)
t.seth(215)
t.forward(60)
t.seth(135)
t.forward(50)
t.seth(225)
t.forward(50)
t.seth(145)
t.forward(65)
t.seth(280)
t.circle(90, 70)
t.seth(290)
t.circle(-320, 50)
t.seth(310)
t.forward(22)
t.seth(56)
t.circle(320, 53)
t.end_fill()

t.hideturtle()