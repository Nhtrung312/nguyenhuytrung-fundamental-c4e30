from turtle import *
mau = ['red','blue','brown','yellow','grey']
i = 0

for i in range(len(mau)):
    begin_fill()
    color(mau[i])
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    
    i += 1
    end_fill()
mainloop() 