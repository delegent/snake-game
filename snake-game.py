import turtle
import random
import time

delay = 0.1
score = 0
highestscore = 0

#sanke bodies
bodies = []

#creating the screen canvas
s = turtle.Screen()
s.title("Vision Games")
s.bgcolor("white")
#s.bordercolor("white")
s.setup(width = 700,height=700)
#s.resizable(False,False)

#reaste the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("black")
food.fillcolor("black")
food.penup()
food.ht()
food.goto(0,300)
food.st()

#score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(-320,320)
sb.write("Score:0 | Heighest Score : 0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction = "stop"
def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)
    
#event handdling
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

#mainlop
while True:
    s.update()#updation of the sreen
    if head.xcor()>340:
        head.setx(-340)
    if head.xcor()<-340:
        head.setx(340)
    if head.ycor()>340:
        head.sety(-340)
    if head.ycor()<-340:
        head.sety(340)


    if head.distance(food)<20:
        x = random.randint(-340,340)
        y = random.randint(-340,340)
        food.goto(x,y)

        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("black")
        body.fillcolor("black")
        bodies.append(body)

        score+=10
        delay-=.001

        if score>highestscore:
            highestscore=score
        sb.clear()
        sb.write(f"Score {score} | Heighest Score : {highestscore}")

    for i in range(len(bodies)-1,0,-1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
    move()

    #checking collosion with the same body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.diretion = "stop"

            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = .1

            sb.clear()
            sb.write(f"Score {score} | Heighest Score : {highestscore}")
    time.sleep(delay)
s.mainloop()



    











































