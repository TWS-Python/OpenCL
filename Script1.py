import tkinter as tk
import random
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

x, y = 200, 10
dx, dy = random.uniform(-5, 5), random.uniform(-5, 5)
speed_dx, speed_dy = random.uniform(0.8, 1.2), random.uniform(0.8, 1.2)
ticks = 0
last_time = 0
fps = 0

def update():
    global x, y, dx, dy, speed_dx, speed_dy, ticks, last_time, fps
    canvas.delete("all")

    # Draw ball
    canvas.create_oval(x-10, y-10, x+10, y+10, fill="black")

    x += int(dx * speed_dx)
    y += int(dy * speed_dy)

    # Boundary conditions to keep the ball within the frame
    if x >= 390:
        x = 390
        dx = -dx
    elif x <= 10:
        x = 10
        dx = -dx

    if y >= 390:
        y = 390
        dy = -dy
    elif y <= 10:
        y = 10
        dy = -dy

    ticks += 1
    current_time = time.time()
    if current_time - last_time >= 1:  # Update FPS every second
        fps = ticks
        ticks = 0
        last_time = current_time
        canvas.itemconfig(fps_text, text=f"FPS: {fps}")
        debug()  # Print debug stats along with FPS

    canvas.after(20, update)

def debug():
    print("Stats:")
    print(f"x: {x}, y: {y}")
    print(f"dx: {dx}, dy: {dy}")
    print(f"speed_dx: {speed_dx}, speed_dy: {speed_dy}")
    print(f"fps: {fps}")

def fps_stats():
    canvas.itemconfig(fps_text, text=f"FPS: {fps}")

fps_text = canvas.create_text(380, 10, anchor="ne", text="FPS: 0", fill="red")
update()

root.mainloop()
