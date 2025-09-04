# import librarys
import tkinter as tk
from tkinter.ttk import *
from tkinter import PhotoImage, messagebox
from sys import maxsize
import string


# for converting number
class Converting:
    def more(self, number):
        more_ten = string.ascii_uppercase
        for i in range(10, 16):
            if number == i:
                return more_ten[number - 10]

    def decimal_integer(self, number):
        basis_2 = []
        basis_8 = []
        basis_16 = []

        check_decimal = number % 1
        if str(check_decimal)[2] == "0":
            basis_2_num = int(number)
            while True:
                division = int(basis_2_num / 2)
                remaining = int(basis_2_num % 2)

                basis_2.append(remaining)

                basis_2_num = division

                if division < 2:
                    basis_2.append(division)
                    break

            basis_8_num = int(number)
            while True:
                division = int(basis_8_num / 8)
                remaining = int(basis_8_num % 8)

                basis_8.append(remaining)

                basis_8_num = division

                if division < 8:
                    basis_8.append(division)
                    break

            basis_16_num = int(number)
            while True:
                division = int(basis_16_num / 16)
                remaining = int(basis_16_num % 16)

                basis_16_num = division

                if remaining <= 9:
                    basis_16.append(remaining)
                else:
                    more = self.more(remaining)
                    basis_16.append(more)

                if division < 16:
                    if division <= 9:
                        basis_16.append(division)
                        break
                    else:
                        more = self.more(division)
                        basis_16.append(more)
                        break

            b_2 = " ".join(str(num) for num in basis_2[::-1])
            b_8 = " ".join(str(num) for num in basis_8[::-1])
            b_16 = " ".join(str(num) for num in basis_16[::-1])

            return b_2, b_8, b_16

        else:
            print("True")


def dec_int():
    convert = Converting()
    try:
        number = float(dec_int_number.get())
    except ValueError:
        messagebox.showerror("ارور", "لطفا مقدار عدد صحیح را درست وارد کنید")

    base_2, base_8, base_16 = convert.decimal_integer(number)

    input_num_show.config(text=int(number))
    conv_2_show.config(text=base_2)
    conv_8_show.config(text=base_8)
    conv_16_show.config(text=base_16)


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

# show converting base 10 integer number
input_num = Label(window, text="عدد وارد شده = ", font=("", "12"))
input_num.place(x=30, y=30)
input_num_show = Label(window, text="", font=("", "12"))
input_num_show.place(x=123, y=30)

conv_2 = Label(window, text="تبدیل به 2 = ", font=("", "12"))
conv_2.place(x=47, y=80)
conv_2_show = Label(window, text="", font=("", "12"))
conv_2_show.place(x=123, y=80)

conv_8 = Label(window, text="تبدیل به 8 = ", font=("", "12"))
conv_8.place(x=47, y=130)
conv_8_show = Label(window, text="", font=("", "12"))
conv_8_show.place(x=123, y=130)

conv_16 = Label(window, text="تبدیل به 16 = ", font=("", "12"))
conv_16.place(x=39, y=180)
conv_16_show = Label(window, text="", font=("", "12"))
conv_16_show.place(x=123, y=180)

dec_int_number = Entry(window, font=("", "14"), background='darkblue')
dec_int_number.place(x=30, y=230, width=170)

# show converting base other number
conv_10_base = Label(window, text="تبدیل به 10 = ",font=("", "12"))
conv_10_base.place(x=354, y=30)
conv_10_base_show = Label(window, text="1",font=("", "12"))
conv_10_base_show.place(x=435, y=30)

conv_2_base = Label(window, text="تبدیل به 2 = ",font=("", "12"))
conv_2_base.place(x=362, y=80)
conv_2_base_show = Label(window, text="1",font=("", "12"))
conv_2_base_show.place(x=435, y=80)

conv_8_base = Label(window, text="تبدیل به 8 = ",font=("", "12"))
conv_8_base.place(x=362, y=130)
conv_8_base_show = Label(window, text="1",font=("", "12"))
conv_8_base_show.place(x=435, y=130)

conv_16_base = Label(window, text="تبدیل به 16 = ",font=("", "12"))
conv_16_base.place(x=354, y=180)
conv_16_base_show = Label(window, text="1",font=("", "12"))
conv_16_base_show.place(x=435, y=180)

binary_number = Entry(window, font=("", "14"))
binary_number.place(x=345, y=230, width=170)

# Button Convert
Button(window, text="تبدیل عدد صحیح", command=dec_int).place(
    x=50, y=280, width=120, height=50)
Button(window, text="تبدیل عدد باینری", command=binary).place(
    x=370, y=280, width=120, height=50)

window.mainloop()
