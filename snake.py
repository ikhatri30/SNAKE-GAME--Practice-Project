import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

# Snake bodies
bodies = []

# Main screen
mainscreen = turtle.Screen()
mainscreen.title("SNAKE GAME")
mainscreen.bgcolor("lightblue")
mainscreen.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("pink")
head.fillcolor("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# Scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-280, 250)
sb.write("Score: 0 | Highest Score: 0", font=("arial", 15, "bold"))

# Function declarations
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event Handling
mainscreen.listen()
mainscreen.onkey(moveup, "Up")
mainscreen.onkey(movedown, "Down")
mainscreen.onkey(moveleft, "Left")
mainscreen.onkey(moveright, "Right")
mainscreen.onkey(movestop, "space")

# Main loop
while True:
    mainscreen.update()
    # Check collision with border
    if head.xcor() > 280:
        head.setx(-280)
    if head.xcor() < -280:
        head.setx(280)
    if head.ycor() > 280:
        head.sety(-280)
    if head.ycor() < -280:
        head.sety(280)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("pink")
        bodies.append(body)

        # Increase score
        score += 10

        # Change delay
        delay -= 0.01

        # Update highest score
        if score > highestscore:
            highestscore = score
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score, highestscore), font=("arial", 15, "bold"))

    # Move the snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake's body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            delay = 0.1

            # Update scoreboard
            sb.clear()
            sb.write("Score: {} | Highest Score: {}".format(score, highestscore), font=("arial", 15, "bold"))

    time.sleep(delay)

mainscreen.mainloop()
