import tkinter as tk
from tkinter import filedialog, Text, ttk
from PIL import Image, ImageTk
# from insert import insert_func
# from update import update_func
# from query import query_func
import os

root = tk.Tk()
root.title('Database')

# canvas and frame
canvas = tk.Canvas(root, height=400, width=700, bg='#263D42')
canvas.pack()
frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Home image
image = Image.open('DBMS_logo.png')
resized = image.resize((300, 225), Image.ANTIALIAS)
wall = ImageTk.PhotoImage(resized)

# // styles for buttons
style = ttk.Style()
style.map("C.TButton",
          foreground=[('pressed', 'red'), ('active', 'blue')],
          background=[('pressed', '!disabled', 'black'), ('active', 'white')]
          )

# Labels-----------
wall_box = tk.Label(frame, image=wall, bd='0')
btn_box = tk.LabelFrame(frame, text='Choose the Operation',
                        fg='#213B42', bd='0', font='Helvetica 13')

# button funcitons
def insert():
    # insert_func()
    pass

def update():
    # update_func()
    pass

def query():
    # query_func()
    pass


# buttons
insert_btn = ttk.Button(btn_box, text='Insert',style='C.TButton', command=insert)
query_btn = ttk.Button(btn_box, text='Query', style='C.TButton', command=query)
update_btn = ttk.Button(btn_box, text='Update',style='C.TButton', command=update)


# //layouts-----------------
wall_box.pack(side=(tk.LEFT), fill=tk.X, padx=10)
btn_box.pack(side=(tk.RIGHT), fill=tk.X, padx=15, ipadx=10)

insert_btn.pack(padx=10, pady=20, ipadx=10)
query_btn.pack(padx=10, pady=20, ipadx=10)
update_btn.pack(padx=10, pady=20, ipadx=10)

root.mainloop()
