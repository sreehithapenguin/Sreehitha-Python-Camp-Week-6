import turtle, random

sc=turtle.Screen()

t1=turtle.Turtle()
t1.shape("turtle")
t1.fillcolor("aqua")
t1.speed(0)
t1.up()
t1.goto(0,0)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.fillcolor("light green")
t2.speed(0)
t2.up()
t2.goto(50,50)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.fillcolor("light pink")
t3.speed(0)
t3.up()
t3.goto(-50,-50)

t4 = turtle.Turtle()
t4.hideturtle()
t4.up()
t4.goto(0,105)

t5 = turtle.Turtle()
t5.hideturtle()

score = 0

def goforward():
    if t2.distance(t1)<15:
        friend()
    if t1.xcor()<100 and t1.xcor()>-100 and t1.ycor()<100 and t1.ycor()>-100:
        t1.forward(5)
    else:
        t1.backward(5)
        t1.right(180)

def gobackward():
    if t2.distance(t1)<15:
        friend()
    if t1.xcor()<100 and t1.xcor()>-100 and t1.ycor()<100 and t1.ycor()>-100:
        t1.backward(5)
    else:
        t1.forward(5)
        t1.right(180)

def turnleft():
    t1.left(30)

def turnright():
    t1.right(30)

def wall():
    turtle.up()
    turtle.goto(-100,-100)
    turtle.down()
    turtle.goto(-100,100)
    turtle.goto(100,100)
    turtle.goto(100,-100)
    turtle.goto(-100,-100)

def enemy():
    t3.setheading(t3.towards(t1))
    t3.forward(0.5)
    if t3.distance(t1)<15:
        gameover()
    sc.ontimer(enemy,10)

def gameover():
    t5.write("Game Over!", align="center",font=("Arial",24,"bold"))
    t4.write("Score: "+str(score))
    exit()

def friend():
    global score
    t4.clear()
    score = score+1
    t4.write("Score: "+str(score))
    randx= random.randint(-100,100)
    randy=random.randint(-100,100)
    t2.goto(randx,randy)
    
sc.onkey(turnleft, 'Left')
sc.onkey(turnright, 'Right')
sc.onkey(goforward, 'Up')
sc.onkey(gobackward, 'Down')


def main():
    sc.listen()
    wall()
    enemy()
    sc.mainloop()

main()








    













