import time
from food import Food
from turtle import Screen
from snake import Snake
screen = Screen()
screen.setup(600, 600)
# high_score = int(open("high_score.txt").read())
# print(high_score)
screen.bgcolor('black')
# screen.screensize(600, 600, "black")
screen.title("SnakeX Ninja")
screen.tracer(0)
food=Food()
snake = Snake()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
# all_t = snake.all_t
screen.update()
Score = 0
snake.screen_write()
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.screen_write()
    # cnt += 1
    #Comparing contact with food
    # print(snake.head.distance(food))
    if snake.head.distance(food) <15:
        snake.score_update()
        food.pos()
        snake.add_segment(snake.all_t[-1].position())

    if snake.head.position()[0]>=310.0 or snake.head.position()[0]<=-310 \
            or snake.head.position()[1]>=310 or snake.head.position()[1]<=-310:
        snake.game_over()
        is_game_on=False
        break
    # cnt=0
    for p in snake.all_t[1:]:
        if snake.head.distance(p) < 10:
            # print(snake.head.distance(p),cnt, snake.head.pos(), p.pos())
            snake.game_over()
            is_game_on=False

screen.exitonclick()
