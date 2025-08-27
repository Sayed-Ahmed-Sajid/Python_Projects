import tkinter as tk
import math
from time import strftime, localtime

def round_rect(canvas, x1, y1, x2, y2, r=25, **kwargs):
    points = [
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

def update_clock():
    time_string = strftime("%I:%M:%S %p")
    date_string = strftime("%A, %d %B %Y")
    clock_lbl.config(text=time_string)
    date_lbl.config(text=date_string)

    now = localtime()
    sec = now.tm_sec + (now.tm_min % 1)
    minute = now.tm_min + sec / 60
    hour = (now.tm_hour % 12) + (minute / 60)

    msg_canvas.delete("all")
    if 0 <= now.tm_hour < 6:
        round_rect(msg_canvas, 10, 10, 240, 60, r=20,
                   fill="#0f172a", outline="#ff00ff", width=3)
        msg_canvas.create_text(125, 35, text="Midnight", 
                               fill="#22d3ee", font=("Segoe UI", 20, "bold"))
    elif 6 <= now.tm_hour < 12:
        msg_lbl.config(text="Morning", fg="orange", bg=bg_color)
    elif 12 <= now.tm_hour < 17:
        msg_lbl.config(text="Afternoon", fg="orange", bg=bg_color)
    elif 17 <= now.tm_hour < 20:
        msg_lbl.config(text="Evening", fg="orange", bg=bg_color)
    else:
        msg_lbl.config(text="Night", fg="orange", bg=bg_color)

    canvas.delete("hands")
    draw_hand(sec * 6, 110, "red", 1.5)
    draw_hand(minute * 6, 100, "white", 3)
    draw_hand(hour * 30, 70, "#22d3ee", 4)
    canvas.create_oval(147, 147, 153, 153, fill="#22d3ee", outline="#22d3ee", tags="hands")

    root.after(100, update_clock)

def draw_hand(angle, length, color, width):
    angle_rad = math.radians(angle - 90)
    x = 150 + length * math.cos(angle_rad)
    y = 150 + length * math.sin(angle_rad)
    canvas.create_line(150, 150, x, y, fill=color, width=width, tags="hands", capstyle=tk.ROUND)

root = tk.Tk()
root.title("Digital + Analog Clock")

hour_now = localtime().tm_hour
if 6 <= hour_now < 18:
    bg_color = "#87ceeb"
else:
    bg_color = "#0f172a"

root.configure(bg=bg_color)

clock_lbl = tk.Label(root, font=("Segoe UI", 48, "bold"), fg="#22d3ee", bg=bg_color)
clock_lbl.pack(padx=20, pady=(25, 10))

date_lbl = tk.Label(root, font=("Segoe UI", 16, "bold"),
                    fg="#e2e8f0", bg="#1e293b", padx=20, pady=10)
date_lbl.pack(pady=(0, 10))

msg_lbl = tk.Label(root, font=("Segoe UI", 20, "bold"), bg=bg_color)
msg_lbl.pack(pady=(0, 20))

msg_canvas = tk.Canvas(root, width=250, height=70, bg=bg_color, highlightthickness=0)
msg_canvas.pack(pady=(0, 20))

canvas = tk.Canvas(root, width=300, height=300, bg=bg_color, highlightthickness=0)
canvas.pack(pady=10)

canvas.create_oval(30, 30, 270, 270, outline="orange", width=5)

for i in range(1, 13):
    angle = math.radians(i * 30 - 90)
    x = 150 + 110 * math.cos(angle)
    y = 150 + 110 * math.sin(angle)
    canvas.create_text(x, y, text=str(i), fill="#e2e8f0", font=("Segoe UI", 12, "bold"))

for i in range(60):
    angle = math.radians(i * 6 - 90)
    x1 = 150 + 120 * math.cos(angle)
    y1 = 150 + 120 * math.sin(angle)
    x2 = 150 + 125 * math.cos(angle)
    y2 = 150 + 125 * math.sin(angle)
    color = "white" if i % 5 == 0 else "#555555"
    canvas.create_line(x1, y1, x2, y2, fill=color)

update_clock()
root.mainloop()
