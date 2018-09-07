
import turtle

def getPoint() :
    x = int(input("Enter x coordinate\n"))
    y = int(input("Enter y coordinate\n"))
    list = [x,y]
    return list 

def displayPoint(point) :

    screen =  turtle.Screen()
    py = turtle.Turtle()
    py.color("blue")
    py.forward(point[0])
    py.left(90)
    py.forward(point[1])
    screen.exitonclick()



# def updatePoint(point) :
#     x = int(input("Enter new x coordinate\n"))
#     y = int(input("Enter new y coordinate\n"))

#     newscreen =  turtle.Screen()
#     newpy = turtle.Turtle()
#     newpy.color("blue")
#     newpy.forward(x)
#     newpy.left(90)
#     newpy.forward(y)
    


def main():
    point = []

    while True :
        choice = input("Enter your choice 1.Create a point  2.Display point 3.Exit\n")
        if choice == "1" :
           point = getPoint() 

        elif choice == "2" :
            displayPoint(point)
    
        elif choice == "3" :
            exit()
        
        else :
            print("choose a valid choice")

if __name__ == '__main__' :
    main()
