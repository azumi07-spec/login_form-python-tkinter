import tkinter as tk
from tkinter import messagebox, font


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo("LOGIN SUCCESSFULLY", "Welcome Admin!")
    else:
        messagebox.showerror("LOGIN FAILED!", "Invalid Username or Password!")


def round_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    """Draw a rounded rectangle on a canvas."""
    points = [
        x1 + r, y1, x2 - r, y1, x2, y1,
        x2, y1 + r, x2, y2 - r, x2, y2,
        x2 - r, y2, x1 + r, y2, x1, y2,
        x1, y2 - r, x1, y1 + r, x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


# Main Window
root = tk.Tk()
root.title("Login Form")
root.geometry("350x500")
root.configure(bg="#082A22")
root.resizable(False, False)


# Fonts (uses the first one your laptop has, so it never breaks)
def pick_font(*choices):
    available = font.families()
    for name in choices:
        if name in available:
            return name
    return "Helvetica"


TITLE_FONT = pick_font("Pacifico", "Cooper Black", "Berlin Sans FB Demi",
                       "Comic Sans MS")
BODY_FONT = pick_font("Trebuchet MS", "Segoe UI", "Verdana")

# Card: rounded corners + raised look (a shadow drawn behind it)
W, H = 320, 380
canvas = tk.Canvas(root, width=W, height=H, bg="#082A22", highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor="center")

round_rect(canvas, 10, 12, W - 4, H - 2, 30, fill="#04170F")                 # shadow
round_rect(canvas, 4, 4, W - 10, H - 10, 30, fill="#C8EBD2",
           outline="#EAF8EF", width=2)                                       # card

# Everything inside the card sits in this frame
card = tk.Frame(canvas, bg="#C8EBD2")
canvas.create_window(157, 187, window=card, width=250, height=320)

# Title
title_label = tk.Label(
    card, 
    text="USER LOGIN", 
    font=(TITLE_FONT, 20, "bold"),
    bg="#C8EBD2", 
    fg="#0E3825"
    )
title_label.pack(pady=(10, 20))

# Username (label and entry share the same left edge)
username_label = tk.Label(
    card, 
    text="Username", 
    font=(BODY_FONT, 11, "bold"),
    bg="#C8EBD2", 
    fg="#12402A"
)
username_label.pack(anchor="w")

username_entry = tk.Entry(
    card, 
    font=(BODY_FONT, 12), 
    bd=1, 
    relief="solid"
)
username_entry.pack(fill="x", pady=(2, 12), ipady=4)

# Password
password_label = tk.Label(
    card, 
    text="Password", 
    font=(BODY_FONT, 11, "bold"),
    bg="#C8EBD2", 
    fg="#12402A"
)
password_label.pack(anchor="w")

password_entry = tk.Entry(
    card,
    font=(BODY_FONT, 12), 
    show="*", 
    bd=1,
    relief="solid"
)
password_entry.pack(fill="x", pady=(2, 0), ipady=4)

# Login Button (pushed lower, raised look)
login_button = tk.Button(
    card, 
    text="LOG IN", 
    font=(TITLE_FONT, 13, "bold"),
    bg="#547B1E", 
    fg="white",
    activebackground="#3F5B15", 
    activeforeground="white",
    relief="raised", 
    bd=4, 
    cursor="hand2", 
    command=login
)
login_button.pack(fill="x", pady=(35, 0), ipady=3)

# Press Enter to login
root.bind("<Return>", lambda event: login())

# Run
root.mainloop()
