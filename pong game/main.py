from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
#==========================================
# create screen
screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
#==========================================
# create paddles
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
screen.onkey(r_paddle.move_up , "Up")
screen.onkey(r_paddle.move_down , "Down")
screen.onkey(l_paddle.move_up , "w")
screen.onkey(l_paddle.move_down , "s")
#==========================================
#create ball
new_ball = Ball()
new_score = Score() 
game_is_on = True
while game_is_on:
    screen.listen()
    time.sleep(0.05)
    screen.update()
    new_ball.move()
    for segment in r_paddle.segments:
        if new_ball.distance(segment) < 50 and new_ball.xcor() > 320:
            new_ball.bounce_x()
            new_ball.increase_speed()
    for segment in l_paddle.segments:
        if new_ball.distance(segment) < 50 and new_ball.xcor() < -320: 
            new_ball.bounce_x()
            new_ball.increase_speed()
    if new_ball.xcor() > 380: #left score +1
        new_ball.reset_position()
        new_score.increase_l_score()
        if new_score.check_game_over():
            game_is_on = False
        
        
    if new_ball.xcor() < -380: # right score +1
        new_ball.reset_position()
        new_score.increase_r_score()
        if new_score.check_game_over():
            game_is_on = False


screen.exitonclick()
