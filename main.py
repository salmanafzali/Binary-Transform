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
window.geometry('600x450')
window.title("تبدیل مبنا")

# upload image
main_img = PhotoImage(file="ed-1.png")
Label(window, image=main_img).place(x=0, y=0)

# converting base 10 integer number
tk.Label(window, text="عدد مبنای 10 را وارد کنید", font=("", "13")).place(x=65, y=25)
dec_int_number = Entry(window, font=("", "14"), background='darkblue').place(x=30, y=50)
# Show converting
input_num = Label(window, text="عدد وارد شده = ", font=("", "12")).place(x=31, y=120)
conv_2 = Label(window, text="تبدیل به 2 = ", font=("", "12")).place(x=47, y=170)
conv_8 = Label(window, text="تبدیل به 8 = ", font=("", "12")).place(x=47, y=230)
conv_16 = Label(window, text="تبدیل به 16 = ", font=("", "12")).place(x=39, y=280)

# converting base other number
Label(window, text="مقدار خود را وارد کنید", font=("", "13")).place(x=390, y=25)
binary_number = Entry(window, font=("", "14")).place(x=345, y=50)
conv_10_base = Label(window, text="تبدیل به 10 = ", font=("", "12")).place(x=354, y=120)
conv_2_base = Label(window, text="تبدیل به 2 = ", font=("", "12")).place(x=362, y=170)
conv_8_base = Label(window, text="تبدیل به 8 = ", font=("", "12")).place(x=362, y=230)
conv_16_base = Label(window, text="تبدیل به 16 = ", font=("", "12")).place(x=354, y=280)

# Button Convert
Button(window, text="تبدیل عدد صحیح", command=integer).place(x=75, y=340, width=120, height=50)
Button(window, text="تبدیل عدد باینری", command=binary).place(x=390, y=340, width=120, height=50)

window.mainloop()