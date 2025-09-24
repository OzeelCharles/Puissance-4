import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x250")
root.title("First step GigadoomChad")

image = Image.open("/Users/charles.ozeel/Desktop/Puissance4/images/giga_chad_test.jpeg")
tk_image = ImageTk.PhotoImage(image)
text_var = tk.StringVar()
text_var.set("Je t'aime Rachel")

label = tk.Label(root,
              image = tk_image)

label.pack(pady = 20)

root.mainloop()