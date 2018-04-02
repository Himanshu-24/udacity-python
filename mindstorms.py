import turtle

def draw_square():
                window = turtle.Screen()
                window.bgcolor("green")

                brad=turtle.Turtle()
                brad.shape("turtle")
                brad.color("black")
                for i in range (1,36):
                 brad.right(10)
                 for i in range (1,5): 
                        brad.forward(50)
                        brad.right(90)
                        
                window.exitonclick()
draw_square()
