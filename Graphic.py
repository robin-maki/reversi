import turtle

GRID_SIZE = 80
STONE_SIZE = 60

turtle.hideturtle()
turtle.speed(0)
turtle.up()
for i in range(9):
    turtle.goto((i - 4) * GRID_SIZE, GRID_SIZE * -4)
    turtle.down()
    turtle.goto((i - 4) * GRID_SIZE, GRID_SIZE * 4)
    turtle.up()
for i in range(9):
    turtle.goto(GRID_SIZE * -4, (i - 4) * GRID_SIZE)
    turtle.down()
    turtle.goto(GRID_SIZE * 4, (i - 4) * GRID_SIZE)
    turtle.up()
def drawStone(x, y, color):
    turtle.goto((x - 3.5) * GRID_SIZE, (y - 3.5) * GRID_SIZE)
    turtle.dot(STONE_SIZE, color)
