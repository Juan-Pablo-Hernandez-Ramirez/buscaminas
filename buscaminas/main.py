# Package import
from tkinter import *

# Screen settings
screen = Tk()
screen.attributes("-fullscreen", True)
screen.config(bg="gray90")

# Buttons
close_button = Button(screen, command=screen.destroy, width=5, text="x", bg="red", fg="white")
close_button.place(x=1330, y=0)



screen.mainloop()