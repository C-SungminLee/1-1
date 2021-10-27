import turtle as trtl
painter = trtl.Turtle()

radius = 125
for i in range(4):
  color_choice = input("Circle color: ")
  painter.color(color_choice)
  painter.begin_fill()
  painter.circle(radius)
  painter.end_fill()
  painter.penup()
  painter.left(90)
  painter.forward(radius)
  raidius = radius - 25
  painter.pendown()
  painter.right(90)
