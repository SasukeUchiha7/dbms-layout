

import tkinter as tk
from tkinter import filedialog, Text, ttk, messagebox
import os


# def insert_func():

top = tk.Tk()
top.title('Insert')

#canvas and frame
canvas = tk.Canvas(top, height=500, width=700, bg='#263D42')
canvas.pack()
frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# -------main--------
# Boxes
personal_box = tk.LabelFrame(
    frame, text='Personal Details', bg='white', font='Helvetica 11')
personal_box.grid(padx=10, pady=10)

address_box = tk.LabelFrame(
    frame, text='Address Details', bg='white', font='Helvetica 11')
address_box.grid(row=1, column=0, padx=10, sticky=tk.W)

travel_box = tk.LabelFrame(
    frame, text='Travelling Details', bg='white', font='Helvetica 11')
travel_box.grid(row=0, column=1, columnspan=4, padx=10, pady=20, sticky=tk.N)

btn_box = tk.LabelFrame(
    frame, text='', bg='white', font='Helvetica 11', bd='1')
btn_box.grid(row=1, column=1, padx=10, pady=10, sticky=tk.S)


# button functions---------------
flagged = False


def add():
    print('You clicked add.')
    for i in personal_info:
        if personal_info[i].get() == '':
            flagged = True
    if flagged:
        messagebox.showwarning('Warning', 'Please fill all the fields.')


def reset():
    print('You clicked reset.')
    for child in personal_box.winfo_children():
        try:
            child.delete(0, tk.END)
        except:
            pass
    for child in travel_box.winfo_children():
        try:
            child.delete(0, tk.END)
        except:
            pass
    for child in address_box.winfo_children():
        try:
            child.delete(0, tk.END)
        except:
            pass


def cancel():
    print('You clicked cancel.')
    top.destroy()


# labels------------------------
personal_labels = ['Name :', 'Age :', 'Aadhar No. :']
address_labels = ['Street :', 'Area :', 'City :',
                  'State :', 'Country :', 'Pin Code :']
travel_labels = ['From ', 'To']

# personal label
for i in range(len(personal_labels)):
    cur_label = 'label'+str(i)
    cur_label = tk.Label(personal_box, text=personal_labels[i], bg='white')
    cur_label.grid(row=i, padx=10, pady=10, sticky=tk.E)


# address labels
for i in range(len(address_labels)):
    cur_label = 'label'+str(i)
    cur_label = tk.Label(address_box, text=address_labels[i], bg='white')
    cur_label.grid(row=i, padx=10, pady=5, sticky=tk.E)

# travel labels
for i in range(len(travel_labels)):
    cur_label = 'label'+str(i)
    cur_label = tk.Label(travel_box, text=travel_labels[i], bg='white')
    cur_label.grid(row=0, column=i, padx=10)


# Entries------------------------
# variables
personal_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'aadhar': tk.StringVar(),
}

adderss_info = {
    'street': tk.StringVar(),
    'area': tk.StringVar(),
    'city': tk.StringVar(),
    'state': tk.StringVar(),
    'country': tk.StringVar(),
    'pin': tk.StringVar(),
}

travel_info = {
    'from': tk.StringVar(),
    'to': tk.StringVar(),
}

# personal entry
cnt = 0
for i in personal_info:
    cur_entry = 'entry_' + i
    cur_entry = tk.Entry(personal_box, width=18,
                         bg='#F0F0F0', textvariable=personal_info[i])
    cur_entry.grid(row=cnt, column=1, padx=10, pady=5)
    cnt += 1


# address enrty
cnt = 0
for i in adderss_info:
    cur_entry = 'entry_' + i
    cur_entry = tk.Entry(address_box, width=24, bg='#F0F0F0',
                         textvariable=adderss_info[i])
    cur_entry.grid(row=cnt, column=1, padx=10, pady=5)
    cnt += 1

# travel entry
cnt = 0
for i in travel_info:
    cur_entry = 'entry_' + i
    cur_entry = tk.Entry(travel_box, width=20, bg='#F0F0F0',
                         textvariable=travel_info[i])
    cur_entry.grid(row=1, column=cnt, padx=10, pady=10)
    cnt += 1


# buttons----------------------
add_btn = tk.Button(btn_box, text='Add', command=add)
reset_btn = tk.Button(btn_box, text='Reset', command=reset)
cancel_btn = tk.Button(btn_box, text='Cancel', command=cancel)


add_btn.grid(padx=10, ipadx=10, pady=10)
reset_btn.grid(row=0, column=1, padx=10, ipadx=10)
cancel_btn.grid(row=0, column=2, padx=10, ipadx=10)

# responsive-----------------------------------

frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)

personal_box.columnconfigure(0, weight=1)
personal_box.columnconfigure(1, weight=1)
address_box.columnconfigure(0, weight=1)
address_box.columnconfigure(1, weight=1)
travel_box.columnconfigure(0, weight=1)
travel_box.columnconfigure(1, weight=1)


top.mainloop()
