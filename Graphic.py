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
for i in range(8):
    for j in range(8):
        turtle.goto((i - 3.5) * GRID_SIZE, (j - 3.5) * GRID_SIZE)
        if (i + j) % 2 == 0:
            turtle.dot(STONE_SIZE, 'red')
        else:
            turtle.dot(STONE_SIZE, 'blue')

input()