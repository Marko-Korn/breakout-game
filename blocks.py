from turtle import Turtle


class Blocks:
    def __init__(self):
        self.all_blocks = []
        self.block_count = 0
        self.blocks_removed = 0
        self.create_blocks()

    def create_blocks(self):
        colors = ["#95275d", "#181925", "#296d92"]
        y_positions = [250, 200, 150]
        for color, y in zip(colors, y_positions):
            for x in range(-470, 470, 90):
                self.add_block((x, y), color)

    def add_block(self, position, color):
        block = Turtle()
        block.shape("square")
        block.color(color)
        block.shapesize(stretch_wid=2, stretch_len=4.2)
        block.penup()
        block.goto(position)
        self.all_blocks.append(block)
        self.block_count += 1

    def detect_collision(self, ball):
        for block in self.all_blocks:
            if ball.distance(block) < 50:
                ball.bounce_y()
                block.hideturtle()
                self.all_blocks.remove(block)
                self.blocks_removed += 1
                return True
        return False

    def get_block_count(self):
        return self.block_count

    def get_blocks_removed(self):
        return self.blocks_removed
