# import librarys
import tkinter as tk
from tkinter.ttk import *
from tkinter import PhotoImage, messagebox
from sys import maxsize
import string


# for converting number
class Converting:
    pass


def integer():
    pass

def binary():
    pass

# create frontend
window = tk.Tk()
window.geometry('550x420')
window.title("تبدیل مبنا")
window.maxsize(550, 420)

# upload image
# main_img = PhotoImage(file="ed-1.png")
# Label(window, image=main_img).place(x=0, y=0)

# converting base 10 integer number
input_num = Label(window, text="عدد وارد شده = ", font=("", "12")).place(x=31, y=30)
conv_2 = Label(window, text="تبدیل به 2 = ", font=("", "12")).place(x=47, y=80)
conv_8 = Label(window, text="تبدیل به 8 = ", font=("", "12")).place(x=47, y=130)
conv_16 = Label(window, text="تبدیل به 16 = ", font=("", "12")).place(x=39, y=180)
dec_int_number = Entry(window, font=("", "14"), background='darkblue')
dec_int_number.place(x=30, y=230, width=170)

# converting base other number
conv_10_base = Label(window, text="تبدیل به 10 = ", font=("", "12")).place(x=354, y=30)
conv_2_base = Label(window, text="تبدیل به 2 = ", font=("", "12")).place(x=362, y=80)
conv_8_base = Label(window, text="تبدیل به 8 = ", font=("", "12")).place(x=362, y=130)
conv_16_base = Label(window, text="تبدیل به 16 = ", font=("", "12")).place(x=354, y=180)
binary_number = Entry(window, font=("", "14"))
binary_number.place(x=345, y=230, width=170)

# Button Convert
Button(window, text="تبدیل عدد صحیح", command=integer).place(x=50, y=280, width=120, height=50)
Button(window, text="تبدیل عدد باینری", command=binary).place(x=370, y=280, width=120, height=50)

window.mainloop()