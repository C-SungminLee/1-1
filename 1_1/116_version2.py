#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# Create Spider body

spider.pensize(40)
spider.circle(20)

# Configure Spider leg

leg_amount = 8
leg_length= 70

# Spider leg

leg_angle = 360 / leg_amount
spider.pensize(5)
incrementing_counter= 0
while (incrementing_counter< leg_amount):
  spider.goto(0,20)
  spider.setheading(leg_angle*incrementing_counter)
  spider.forward(leg_length)
  incrementing_counter= incrementing_counter+ 1
spider.hideturtle()

leg_amountn = trtl.Screen()