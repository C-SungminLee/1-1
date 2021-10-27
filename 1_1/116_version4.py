#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# Create Spider body

spider.pensize(40)
spider.circle(20)

# Configure Spider leg

leg_amount = 4
leg_length= 70

# Spider leg

leg_angle = -90 / leg_amount
spider.pensize(5)
incrementing_counter= 0
while (incrementing_counter< leg_amount):
  spider.goto(0,20)
  spider.setheading(leg_angle*incrementing_counter-45)
  spider.forward(leg_length)
  incrementing_counter= incrementing_counter+ 1
spider.hideturtle()

leg_amount = 4

leg_angle = 90 / leg_amount
incrementing_counter= 4
while (incrementing_counter< leg_amount + 4):
  spider.goto(0,20)
  spider.setheading(leg_angle*incrementing_counter-45)
  spider.forward(leg_length)
  incrementing_counter= incrementing_counter+ 1
spider.hideturtle()

# Create Spider Eyes
spider.penup()
spider.goto(-20,10)
spider.pendown()
spider.pencolor("red")
spider.pensize(5)
spider.circle(1)
spider.penup()
spider.goto(-20,30)
spider.pendown()
spider.circle(1)

leg_amountn = trtl.Screen()