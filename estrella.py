from turtle import *
def dibujar_estrella(n):
    a=n
    while a>0:
        a-=2
    if a==-1:
        begin_fill()
        while True:
            forward(100)
            left(180+(180/n))
            if abs(pos()) < 1:
                break
        done()
    elif a==0:
        begin_fill
        while True:
            forward(100)
            left((180+(180/(n/2))))
            if abs(pos()) < 1:
                break
        done()
