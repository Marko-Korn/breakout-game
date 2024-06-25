from turtle import Screen, Turtle


image = "./imgs/ball.gif"

screen = Screen()
screen.bgcolor('black')
screen.register_shape(image)

turtle = Turtle(shape=image)

# ...

screen.mainloop()