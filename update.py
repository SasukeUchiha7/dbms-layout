import tkinter as tk
from tkinter import filedialog, Text, ttk
import os


def update_func():

    top = tk.Toplevel()
    top.title('Update')

    #canvas and frame
    canvas = tk.Canvas(top, height=400, width=700, bg='#263D42')
    canvas.pack()
    frame = tk.Frame(canvas, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # ------main-------
    test_label = tk.Label(frame, text='Your are on update dialog', fg='black')
    test_label.pack()
