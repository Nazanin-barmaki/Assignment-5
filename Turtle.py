import turtle
polygon = turtle.Turtle
y = turtle.color()
t = turtle.Turtle()
x = turtle.Screen()

x_sides = int(input('enter the number you want for sides:'))

while True:
    x_color = input('choose one of this colors(pink , magenta  , purple , light green , dark blue):')

    if x_color == 'pink' or x_color == 'magenta' or x_color == 'purple' or x_color == 'light green' or x_color == 'dark blue' :
        polygon.color(x_color)
        break

for i in range(x_sides):
    turtle.color(x_color[turtle.color])
    turtle.forward(30)
    
    
turtle.done()