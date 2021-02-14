from turtle import Screen, Turtle

x_direction = [0, -20, -40]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in x_direction:
            self.add_segment(position)

    def add_segment(self, position):
        part = Turtle(shape="square")
        part.penup()
        part.color("white")
        part.goto(position, 0)
        self.segments.append(part)

    def increase_snake(self):
        self.add_segment(self.segments[-1].position()[0])

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_no - 1].xcor()
            y_pos = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].setposition(x_pos, y_pos)
        self.head.forward(20)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
