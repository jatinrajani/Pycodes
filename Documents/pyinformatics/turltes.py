import turtle
def tree(length,t):
     if length<1:
          return
     else:
          t.forward(10)
          tree(length-4,t)
          t.left(45)
          
          return

def main():
     t=turtle.Turtle()
     mywin=turtle.Screen()
     t.left(90)
     t.speed(1)
     tree(10,t)
     mywin.exitonclick()

main()
     
