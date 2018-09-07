import turtle               # allows us to use the turtles library
wn = turtle.Screen()  


    #   creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
alex.forward(150)           # tell alex to move forward by 150 units
alex.left(90)               # turn by 90 degrees
alex.forward(75) 

alex.backward(19)


wn.exitonclick()


'''
import turtle

turtle.setup(800, 600)
wn = turtle.Screen()

spiral = turtle.Turtle()
spiral.color("blue")
spiral.penup()      

size = 10
for i in range(35):
  spiral.dot()                
  size = size + 2             
  spiral.forward(size)          
  spiral.right(24)

  '''