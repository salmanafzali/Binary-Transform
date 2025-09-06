# import librarys
import tkinter as tk
from tkinter.ttk import *
from tkinter import PhotoImage, messagebox, font
from sys import maxsize
import string


# for converting number
class Converting:
    # for 16 basis and 10 number upp
    def more(self, number):
        more_ten = string.ascii_uppercase
        for i in range(10, 16):
            if number == i:
                return more_ten[number - 10]

    # for integer basis 10 convert to other basis
    def integer_convert(self, number, base):
        result = []     # for save values

        basis = int(number)
        while True:
            # operations
            division = int(basis / base)
            remaining = int(basis % base)

            basis = division

            if remaining <= 9:
                result.append(remaining)
            else:
                more = self.more(remaining)
                result.append(more)

            if division < base:
                if division <= 9:
                    result.append(division)
                    break
                else:
                    more = self.more(division)
                    result.append(more)
                    break

        return " ".join(str(num) for num in result[::-1])

    # for decimal basis 10 convert to other basis
    def decimal_convert(self, number, base):
        result = []          # save values

        flt_number = number % 1          # for separate decimal on integer
        for i in range(4):
            # operations
            mult = flt_number * base

            flt_number = mult % 1

            if int(mult) <= 9:
                result.append(int(mult))
            else:
                more = self.more(int(mult))
                result.append(more)

        return " ".join(str(num) for num in result[::-1])

    # for check value and select operation basis 10
    def decimal_integer(self, number):
        check_decimal = number % 1
        if str(check_decimal)[2] == "0":
            base_2 = self.integer_convert(number, 2)      # basis 2 converting
            base_8 = self.integer_convert(number, 8)      # basis 8 converting
            base_16 = self.integer_convert(
                number, 16)      # basis 16 converting

            return base_2, base_8, base_16

        else:
            # basis 2 converting
            base_2_int = self.integer_convert(number, 2)
            base_2_flt = self.decimal_convert(number, 2)
            base_2_decimal = base_2_int + " / " + base_2_flt

            # basis 8 converting
            base_8_int = self.integer_convert(number, 8)
            base_8_flt = self.decimal_convert(number, 8)
            base_8_decimal = base_8_int + " / " + base_8_flt

            # basis 16 converting
            base_16_int = self.integer_convert(number, 16)
            base_16_flt = self.decimal_convert(number, 16)
            base_16_decimal = base_16_int + " / " + base_16_flt

            return base_2_decimal, base_8_decimal, base_16_decimal

    def binary():
        pass


# check the integer entry value
def dec_int():
    convert = Converting()

    try:
        number = float(dec_int_number.get())
        base_2, base_8, base_16 = convert.decimal_integer(number)

        input_num_show.config(text=int(number))
        conv_2_show.config(text=base_2)
        conv_8_show.config(text=base_8)
        conv_16_show.config(text=base_16)

    except ValueError:
        messagebox.showerror("ارور", "لطفا مقدار عدد صحیح را درست وارد کنید")

# check the vinary entry value
def binary():
    convert = Converting()
    
    try:
        bin_num = binary_number.get()
        base = int(binary_select.get())

    except:
        messagebox.showerror("ارور", "در وارد کردن مقدار باینری یا انتخاب مبنا دقت کنید")



# create frontend
window = tk.Tk()
window.geometry('600x500')
window.title("تبدیل مبنا")
window.maxsize(600, 500)

# upload image
main_img = PhotoImage(file="Untitled-1.png")
Label(window, image=main_img).place(x=0, y=0)

# show converting base 10 integer number
input_num = tk.Label(window, text="عدد وارد شده = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
input_num.place(x=30, y=30)
input_num_show = tk.Label(window, text="", bg='skyblue', font=("", "12"))
input_num_show.place(x=123, y=30)

conv_2 = tk.Label(window, text="تبدیل به 2 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_2.place(x=47, y=80)
conv_2_show = tk.Label(window, text="", bg='skyblue', font=("", "12"), wraplength=230)
conv_2_show.place(x=123, y=80)

conv_8 = tk.Label(window, text="تبدیل به 8 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_8.place(x=47, y=130)
conv_8_show = tk.Label(window, text="", bg='skyblue', font=("", "12"))
conv_8_show.place(x=123, y=130)

conv_16 = tk.Label(window, text="تبدیل به 16 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_16.place(x=39, y=180)
conv_16_show = tk.Label(window, text="", bg='skyblue', font=("", "12"))
conv_16_show.place(x=123, y=180)

dec_int_number = Entry(window, font=("", "14"), background='darkblue')
dec_int_number.place(x=30, y=250, width=170)

# show converting base other number
conv_10_base = tk.Label(window, text="تبدیل به 10 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_10_base.place(x=354, y=30)
conv_10_base_show = tk.Label(window, text="", bg='skyblue', font=("", "12"))
conv_10_base_show.place(x=435, y=30)

conv_2_base = tk.Label(window, text="تبدیل به 2 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_2_base.place(x=362, y=80)
conv_2_base_show = tk.Label(window, text="", bg='skyblue', font=("", "12"), wraplength=160)
conv_2_base_show.place(x=435, y=80)

conv_8_base = tk.Label(window, text="تبدیل به 8 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_8_base.place(x=362, y=130)
conv_8_base_show = tk.Label(window, text="", bg='skyblue', font=("", "12"))
conv_8_base_show.place(x=435, y=130)

conv_16_base = tk.Label(window, text="تبدیل به 16 = ", bg='skyblue', font=font.Font(size=12, weight='bold'))
conv_16_base.place(x=354, y=180)
conv_16_base_show = tk.Label(window, text="", bg='skyblue', font=("", "12"))
conv_16_base_show.place(x=435, y=180)

binary_number = Entry(window, font=("", "14"))
binary_number.place(x=345, y=250, width=170)

binary_select = tk.StringVar()
binary_options = ["مبنا", "2", "8", "16"]
OptionMenu(window, binary_select, *binary_options).place(x=520, y=250, width=60)

# Button Convert
tk.Button(window, text="تبدیل عدد صحیح", command=dec_int, bg='skyblue').place(
    x=50, y=330, width=120, height=50)
tk.Button(window, text="تبدیل عدد باینری", command=binary, bg='skyblue').place(
    x=370, y=330, width=120, height=50)

window.mainloop()
