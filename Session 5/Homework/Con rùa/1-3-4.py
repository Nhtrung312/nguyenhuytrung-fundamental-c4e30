from turtle import *
def draw_square(length,colors):
    for i in range(4) :
        color(colors)
        
        forward(length)
        left(90)
        i +=1
l = int(input(" nhập cạnh :"))
cl = str(input('nhập màu :'))
draw_square(l,cl)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
