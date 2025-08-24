from turtle import Turtle , Screen
screen = Screen()
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.default_game_ender = 5
        self.winning_score = int(screen.textinput("Game End Score", f"At what score should the game end? (Default: {self.default_game_ender})"))
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0 , 280)
        self.update_scoreboard()
        
    def check_game_over(self):
        if self.score_l == self.winning_score:
            self.goto(0,0)
            self.write(f"Left side wins with {self.score_l} / {self.score_r}" , align="center" , font=('Arial' , 16 , 'normal'))
            return True
        elif self.score_r == self.winning_score:
            self.goto(0,0)
            self.write(f"Right side wins with {self.score_r} / {self.score_l}" , align="center", font=('Arial' , 16 , 'normal'))
            return True
        return False
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-50 , 270)
        self.write(f"{self.score_l}", align="center" , font=('Arial' , 16 , 'normal'))
        self.goto(50 , 270)
        self.write(f"{self.score_r}", align="center" , font=('Arial' , 16 , 'normal'))
    
    def increase_l_score(self):        
        self.score_l += 1
        self.update_scoreboard()
        
        
    def increase_r_score(self):        
        self.score_r += 1
        self.update_scoreboard()

