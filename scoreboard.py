from turtle import Turtle
from blocks import Blocks


class Scoreboard(Turtle):

    def __init__(self, blocks):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 3
        self.blocks = blocks
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 370)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 20, "normal"))
        self.goto(-300, 370)
        self.write(f"Blocks: {self.blocks.get_block_count()}", align="center", font=("Courier", 20, "normal"))
        self.goto(300, 370)
        self.write(f"Blocks Removed: {self.blocks.get_blocks_removed()}", align="center",
                   font=("Courier", 20, "normal"))

    def minus_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 20, "normal"))

    def game_win(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 20, "normal"))

