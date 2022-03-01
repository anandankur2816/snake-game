from turtle import Turtle
# turtle_speed = 0
x_pos = [(0,0), (-40,0), (-20,0)]

class Snake:
    def __init__(self):
        self.all_t = []
        self.wr = Turtle()
        self.wr.penup()
        self.wr.hideturtle()
        self.score = 0
        self.screen_write()
        self.create_snake()
        self.head = self.all_t[0]

    def create_snake(self):
        for _ in x_pos:
           self.add_segment(_)

    def add_segment(self,position):
        t = Turtle()
        # t.speed(turtle_speed)
        t.penup()
        t.color('white')
        t.shape('square')
        t.goto(position)
        self.all_t.append(t)

    def move(self):
        cp = (0, 0)
        for _ in self.all_t:
            if cp == (0, 0):
                cp = _.pos()
                # _.left(90)
                _.forward(20)
            else:
                prev = _.pos()
                _.goto(cp)
                cp = prev
        # for i in range(len(self.all_t)-1,0,-1):
        #     self.all_t[i].goto(self.all_t[i-1].pos())
        # self.head.fd(20)

    def up(self):
        # print(self.head.heading())
        if self.head.heading() == 270.0:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90.0:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0.0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180.0:
            pass
        else:
            self.head.setheading(0)

    def screen_write(self):
        self.wr.goto(0,270)
        self.wr.color("white")
        self.wr.write(arg=f"Score:{self.score}", move=True, align="center",
                      font=("Arial", 20, "normal"))

    def score_update(self):
        self.wr.clear()
        self.score += 1
        self.screen_write()

    def game_over(self):
        self.go=Turtle()
        self.go.color("white")
        self.go.goto(0,0)
        self.go.write(arg=f"GAME OVER. Final Score:{self.score}", move=True, align="center",
                      font=("Arial", 30, "normal"))



    def c(self):
        self.all_t[0].clear()
