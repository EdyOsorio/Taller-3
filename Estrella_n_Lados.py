import turtle
a=int(input('Igrese el numero de lados de la estrella: '))
t=turtle.Pen()
t.reset()
#pares
m=180+(180/a)
c=(a-2)*(180/a)
if a%2==0:
    for x in range (a):
        t.left(c)
        t.forward(100)

#impares
else:
    for x in range (a):
        t.forward(100)
        t.left(m)

turtle.getscreen()._root.mainloop()
