from turtle import *
import random
import time

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("Ultimate Love 💖")
screen.tracer(0)

t = Turtle()
t.hideturtle()
t.speed(0)

# Draw heart function
def heart(size, color_name):
    t.color(color_name)
    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size/2, 200)
    t.right(140)
    t.circle(size/2, 200)
    t.forward(size)
    t.end_fill()
    t.setheading(0)

# Floating mini hearts
mini_hearts = []

for _ in range(15):
    m = Turtle()
    m.hideturtle()
    m.speed(0)
    m.penup()
    m.goto(random.randint(-300, 300), random.randint(-300, -50))
    m.color("pink")
    mini_hearts.append(m)

# Animation loop
size = 100
grow = True

while True:
    t.clear()
    t.penup()
    t.goto(0, -50)
    t.pendown()

    # Beating effect
    if grow:
        size += 2
        if size > 120:
            grow = False
    else:
        size -= 2
        if size < 100:
            grow = True

    heart(size, "deeppink")

    # Sparkles
    for _ in range(20):
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.dot(random.randint(2,5), random.choice(["white", "pink", "red"]))

    # Floating hearts movement
    for m in mini_hearts:
        y = m.ycor()
        m.clear()
        m.goto(m.xcor(), y + random.randint(2,5))
        m.dot(10, "hotpink")
        if m.ycor() > 300:
            m.goto(random.randint(-300, 300), -300)

    # Love text
    t.penup()
    t.goto(0, -180)
    t.color("white")
    t.write("LOVE FOREVER ❤️", align="center", font=("Arial", 20, "bold"))

    screen.update()
    time.sleep(0.03)
