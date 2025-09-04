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
            
    def integer_convert(self, number, base):
        result = []
        
        basis = int(number)
        while True:
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
    
    def decimal_convert(self, number, base):
        result = []
        
        flt_number = number % 1
        for i in range(4):
            mult = flt_number * base
            
            flt_number = mult % 1
            
            if int(mult) <= 9:
                result.append(int(mult))
            else:
                more = self.more(int(mult))
                result.append(more)

        return " ".join(str(num) for num in result[::-1])
            

    def decimal_integer(self, number):
        check_decimal = number % 1
        if str(check_decimal)[2] == "0":
            base_2 = self.integer_convert(number, 2)      # basis 2 converting
            base_8 = self.integer_convert(number, 8)      # basis 8 converting
            base_16 = self.integer_convert(number, 16)      # basis 16 converting
            
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
