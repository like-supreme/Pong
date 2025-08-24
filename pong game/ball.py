"""pong oyunundaki topun oluşacağı sınıf ve hareket fonksiyonları 
"""
from turtle import Turtle
import random
import time
X_POS = 0
Y_POS = 0
TOP_BOUND = 280
BOTTOM_BOUND = -280
MAX_SPEED = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(X_POS , Y_POS)
        self.x_move = random.choice([-10 , 10])
        self.y_move = random.choice([-10 , 10])

    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x , self.new_y)
        if self.ycor() > TOP_BOUND or self.ycor() < BOTTOM_BOUND:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(X_POS , Y_POS)
        self.bounce_x()
        self.x_move = random.choice([-10 , 10])
        self.y_move = random.choice([-10 , 10])
        time.sleep(0.5)
    
    def increase_speed(self):
        if abs(self.x_move) < MAX_SPEED:
            self.x_move *= 1.02
        if abs(self.y_move) < MAX_SPEED:
            self.y_move *= 1.02
