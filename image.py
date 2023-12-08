import tkinter as tk
import win32api
import win32con
import pywintypes
from tkinter import PhotoImage
from PIL import ImageTk, Image


def close_label():
    label.master.destroy()


root = tk.Tk()
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
bottom_margin = 30
root.configure(bg="")
background = PhotoImage(file="./Back.png")

img = Image.open("./Back.png").convert("RGBA")

w, h = img.size

left = w / 4
right = 3 * w / 4
upper = h / 4
lower = 3 * h / 4

img2 = img.crop([left, upper, right, lower])
background = ImageTk.PhotoImage(img2)


geometry = "+{}-{}".format(
    int(window_width / 2 - background.width() / 2), bottom_margin
)

label = tk.Label(
    root,
    text="Text on the screen",
    font=("Times New Roman", "80"),
    fg="black",
    bg="white",
    image=background,
)
label.master.attributes("-alpha", 0.9)
label.master.overrideredirect(True)
label.master.geometry(geometry)
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
exStyle = (
    win32con.WS_EX_COMPOSITED
    | win32con.WS_EX_LAYERED
    | win32con.WS_EX_NOACTIVATE
    | win32con.WS_EX_TOPMOST
    | win32con.WS_EX_TRANSPARENT
)
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.pack()

# Schedule the close_label function to be called after 3000 milliseconds (3 seconds)
label.master.after(3000, close_label)

label.master.mainloop()
