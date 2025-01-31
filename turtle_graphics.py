import turtle as t

print("Uppgift 1")
def rectangle(side):
    # Upprepa 4 gånger
    for x in range(4):
        t.forward(side)
        t.left(90)

print("Uppgift 2")
def move_next(side):
    t.penup()
    t.forward(2 * side)
    t.pendown()

#for x in range(5):
#    rectangle(20)
#    move_next(20)

print("Uppgift 3")
def circle(steps, size, angle):
    for x in range(steps):
        t.forward(size)
        t.right(angle)

#circle(36, 20, 10)

print("uppgift 4")
def P(size):
    t.left(90)
    t.forward(size)
    t.right(90)
    circle(18,5,10)
    t.penup()
    t.right(90)
    t.backward(size/2)
    t.right(90)
    t.pendown()


def Y(size):
    t.left(90)
    t.forward(size * 0.5)
    t.left(45)
    t.forward(size / 2)
    t.penup()
    t.backward(size / 2)
    t.pendown()
    t.right(90)
    t.forward(size / 2)
    t.penup()
    t.backward(size / 2)
    t.left(45)
    t.backward(size / 2)
    t.right(90)

def T(size):
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size/2)
    t.backward(size)
    t.forward(size/2)
    t.left(90)
    t.forward(size)
    t.left(90)

def H(size):
    t.left(90)
    t.forward(size)
    t.backward(size/2)
    t.left(90)
    t.backward(size / 2)
    t.left(90)
    t.forward(size/2)
    t.backward(size)
    t.left(90)

def O(size):
        for x in range(36):
            t.forward(size/10)
            t.right(10)
        t.penup()
        t.right(90)
        t.forward(size)
        t.left(90)

def N(size):
    t.left(90)
    t.forward(size)
    t.right(140)
    t.forward(size*1.2)
    t.left(140)
    t.forward(size)


P(100)
move_next(50)
Y(100)
move_next(50)
T(100)
move_next(50)
H(100)
move_next(50)
O(100)
move_next(50)
N(100)


# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()

