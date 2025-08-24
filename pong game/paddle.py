from turtle import Turtle
class Paddle:
    def __init__(self , xpos):
        self.paddle = Turtle()
        self.segments = []
        self.xpos = xpos
        self.ypos = -40
        self.create_paddle()
    def create_paddle(self):
        for i in range(5):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.xpos , self.ypos)
            self.segments.append(new_segment)
            self.ypos += 20    
    def move_up(self):
        top_segment = self.segments[-1]
        if top_segment.ycor() < 280:
            for segment in self.segments:
                new_coor = segment.ycor() + 20
                segment.goto(self.xpos , new_coor)
    def move_down(self):
        top_segment = self.segments[0]
        if top_segment.ycor() > -280:
            for segment in self.segments:
                new_coor = segment.ycor() - 20
                segment.goto(self.xpos , new_coor)


            


        



