import turtle
t = turtle.Turtle()
t.speed("fastest")
t.pensize(1)
turtle.tracer(0, 0)
turtle.setup(width=500, height=500, startx=0, starty=0)
def tile(i, d):
    t.pd()
    t.begin_fill()
    for y in ([120, 60, 120, 60]):
        t.fd((4*i)/d)
        t.rt(y)
    t.end_fill()
    t.pu()
    t.fd((4*i)/d)
    
def column(i, d, r, c):
    for y in range(r):
        t.color(c[y%len(c)])
        tile(i, d)
    t.bk(4*i*(r/d))
    
def side(i, d, s, c):
    c1 = []
    for y in range(len(c)):
        c1.append(((c[y][0]*s), (c[y][1]*s), (c[y][2]*s))) 

    for y in range(d):
        if (y < (d/2)):
            column(i, d, d, c1)
            t.rt(120); t.fd((4*i)/d); t.lt(120)
        else:
            column(i, d, d//2, c1)
            t.rt(120); t.fd((4*i)/d); t.lt(120)
        c1.append(c1.pop(0))

#x, y = center positon of shape
#i = scaling factor
#d = amount of tiles (2 minimum, only even numbers)
#c = list of colors to iterate over
def shape(x, y, i, d, c):
    t.pu()
    t.setpos(x, y)
    headings = [270, 30, 150]
    shadings = [0.3, 0.6, 0.9]
    for h in range(3):
        t.setheading(headings[h])
        side(i, d, shadings[h], c)
        t.setpos(x, y) 
           
def main(i, d, c=[(0, 0, 0)]):
    for y in range(turtle.window_height()//(i*6) + 2):
        for x in range(int(turtle.window_width()//(i*5.196)) + 2):
            if (x % 2 == 1):
                shape(x*i*5.196 - (turtle.window_width()/2), 
                      y*i*6+(i*3) - (turtle.window_height()/2),
                      i, d, c)
            else:
                shape(x*i*5.196 - (turtle.window_width()/2), 
                      y*i*6 - (turtle.window_height()/2),
                      i, d, c)



main(50, 4, [(0.2, 0.2, 0.2), (0.9, 0.9, 0.9)])
turtle.update()
