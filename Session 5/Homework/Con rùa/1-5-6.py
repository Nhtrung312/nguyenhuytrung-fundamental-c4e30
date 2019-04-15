from turtle import *
def draw_star(x,y,length):
    up()
    setposition(x,y)
    down()
    for i in range(5):
        left(144)
        forward(length)
        i += 1
    mainloop()
length = int(input("Length = "))
x = int(input("x= "))
y = int(input("y= "))
draw_star(x,y,length)
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)