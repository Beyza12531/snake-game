import turtle
import time
import random

# Ekranı kur
wn = turtle.Screen()
wn.title("Yılan Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Yılanın kafası
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Yem
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Skor
score = 0
high_score = 0

# Skor yazısı
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Skor: 0  En Yüksek Skor: 0", align="center", font=("Courier", 18, "normal"))

# Hareket fonksiyonları
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

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

# Tuşlar
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Ana oyun döngüsü
while True:
    wn.update()

    # Kenara çarpma
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Kuyruğu sil
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Skor: {}  En Yüksek Skor: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

    # Yem yeme
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Kuyruğa segment ekle
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # Skor
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Skor: {}  En Yüksek Skor: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

    # Kuyruğu hareket ettir
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Kendine çarpma
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Skor: {}  En Yüksek Skor: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

    time.sleep(0.1)

