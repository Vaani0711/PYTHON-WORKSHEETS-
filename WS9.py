
import tkinter as tk

root = tk.Tk()
root.title("Robot Control Panel")
root.geometry("500x400")
root.configure(bg="yellow")

root.mainloop()


import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# small circle to represent point
canvas.create_oval(98, 98, 102, 102, fill="black")

root.mainloop()



import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

points = [20, 50, 100, 120, 180, 90, 250, 150]
canvas.create_line(points, fill="blue", width=3)

root.mainloop()



import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

point = canvas.create_oval(10, 140, 20, 150, fill="red")
x_speed = 2

def move_point():
    canvas.move(point, x_speed, 0)
    canvas.after(20, move_point)

move_point()
root.mainloop()


import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_rectangle(100, 100, 250, 180, fill="gray")

canvas.create_oval(110, 180, 150, 220, fill="black")
canvas.create_oval(200, 180, 240, 220, fill="black")

root.mainloop()



import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

robot = canvas.create_oval(180, 130, 220, 170, fill="blue")  # small circle

def move(dx, dy):
    canvas.move(robot, dx, dy)

tk.Button(root, text="Up", command=lambda: move(0, -10)).pack()
tk.Button(root, text="Down", command=lambda: move(0, 10)).pack()
tk.Button(root, text="Left", command=lambda: move(-10, 0)).pack()
tk.Button(root, text="Right", command=lambda: move(10, 0)).pack()

root.mainloop()




import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=350, bg="white")
canvas.pack()

r = 15
ball = canvas.create_oval(200-r, 150-r, 200+r, 150+r, fill="red")

dx, dy = 3, 3

def animate():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= 500:
        dx = -dx
    if y1 <= 0 or y2 >= 350:
        dy = -dy

    canvas.after(20, animate)

animate()
root.mainloop()




import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

x, y = 50, 200
target_x = 450
velocity = 2

robot = canvas.create_oval(x-10, y-10, x+10, y+10, fill="green")

def move_robot():
    global x
    if x < target_x:
        x += velocity
        canvas.coords(robot, x-10, y-10, x+10, y+10)
        canvas.after(20, move_robot)

move_robot()
root.mainloop()





import tkinter as tk
import math

root = tk.Tk()
root.title("Four-Bar Mechanism")

canvas = tk.Canvas(root, width=700, height=500, bg="white")
canvas.pack()

# Given
A = (150, 300)
D = (400, 300)

L2 = 120   # crank
L3 = 150   # coupler
L4 = 130   # rocker
theta = math.radians(30)

# Compute B (end of crank)
Bx = A[0] + L2 * math.cos(theta)
By = A[1] - L2 * math.sin(theta)
B = (Bx, By)

# Compute C (intersection of two circles)
# Circle 1: center B radius L3
# Circle 2: center D radius L4

def circle_intersection(x0,y0,r0, x1,y1,r1):
    dx = x1 - x0
    dy = y1 - y0
    d = math.hypot(dx, dy)
    a = (r0*r0 - r1*r1 + d*d) / (2*d)
    h = math.sqrt(abs(r0*r0 - a*a))

    xm = x0 + a * dx/d
    ym = y0 + a * dy/d

    xs1 = xm + h * dy/d
    ys1 = ym - h * dx/d

    xs2 = xm - h * dy/d
    ys2 = ym + h * dx/d

    return (xs1, ys1), (xs2, ys2)

C1, C2 = circle_intersection(B[0], B[1], L3, D[0], D[1], L4)

C = C1   # choose first intersection

# Draw joints
r = 5
def draw_point(P, color):
    canvas.create_oval(P[0]-r, P[1]-r, P[0]+r, P[1]+r, fill=color)

draw_point(A, "red")
draw_point(B, "blue")
draw_point(C, "green")
draw_point(D, "black")

# Draw links (different colors)
canvas.create_line(A[0], A[1], B[0], B[1], width=4, fill="blue")    # crank
canvas.create_line(B[0], B[1], C[0], C[1], width=4, fill="green")  # coupler
canvas.create_line(C[0], C[1], D[0], D[1], width=4, fill="orange") # rocker
canvas.create_line(A[0], A[1], D[0], D[1], width=4, fill="red")    # ground

root.mainloop()



import tkinter as tk

root = tk.Tk()
root.title("Robot Path Drawer")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Robot
x, y = 300, 200
robot = canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")

path_lines = []

def move(dx, dy):
    global x, y

    new_x = x + dx
    new_y = y + dy

    # Draw path line
    line = canvas.create_line(x, y, new_x, new_y, fill="black")
    path_lines.append(line)

    # Move robot
    canvas.move(robot, dx, dy)

    x, y = new_x, new_y

def key_press(event):
    if event.keysym == "Up":
        move(0, -5)
    elif event.keysym == "Down":
        move(0, 5)
    elif event.keysym == "Left":
        move(-5, 5)
    elif event.keysym == "Right":
        move(5, 0)

root.bind("<KeyPress>", key_press)

def reset_path():
    for line in path_lines:
        canvas.delete(line)
    path_lines.clear()

tk.Button(root, text="RESET", command=reset_path, font=("Arial", 14)).pack(pady=10)

root.mainloop()
