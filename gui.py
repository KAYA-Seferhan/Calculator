import tkinter
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon_path = resource_path("icon.ico")

main_window = tkinter.Tk()
main_window.title("Calculator")
main_window.geometry("600x700")
main_window.iconbitmap(icon_path)
main_window.config(background="#242424")

result_frame = tkinter.Frame(main_window)
result_frame.place(x=5, y=5, width=590, height=190)
result_frame.config(highlightthickness=1, highlightbackground='grey', background="#242424")

result_label = tkinter.Label(result_frame, text="0")
result_label.config(background='#242424', foreground='white', font=('Arial', 30, 'bold'), anchor='ne')
result_label.place(x=1, y=1, width=586, height=186)

key_frame = tkinter.Frame(main_window)
key_frame.place(x=5, y=200, width=590, height=495)
key_frame.config(highlightthickness=1, highlightbackground='grey', background="#242424")

button_1 = tkinter.Button(key_frame, text="1")
button_1.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_1.grid(row=3, column=0, padx=8, pady=8)

button_2 = tkinter.Button(key_frame, text="2")
button_2.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_2.grid(row=3, column=1, padx=8, pady=8)

button_3 = tkinter.Button(key_frame, text="3")
button_3.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_3.grid(row=3, column=2, padx=8, pady=8)

button_4 = tkinter.Button(key_frame, text="4")
button_4.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_4.grid(row=2, column=0, padx=8, pady=8)

button_5 = tkinter.Button(key_frame, text="5")
button_5.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_5.grid(row=2, column=1, padx=8, pady=8)

button_6 = tkinter.Button(key_frame, text="6")
button_6.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_6.grid(row=2, column=2, padx=8, pady=8)

button_7 = tkinter.Button(key_frame, text="7")
button_7.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_7.grid(row=1, column=0, padx=8, pady=8)

button_8 = tkinter.Button(key_frame, text="8")
button_8.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_8.grid(row=1, column=1, padx=8, pady=8)

button_9 = tkinter.Button(key_frame, text="9")
button_9.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_9.grid(row=1, column=2, padx=8, pady=8)

button_0 = tkinter.Button(key_frame, text="0")
button_0.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
button_0.grid(row=4, column=1, padx=8, pady=8)

minus_button = tkinter.Button(key_frame, text="-")
minus_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
minus_button.grid(row=2, column=3, padx=8, pady=8)

plus_button = tkinter.Button(key_frame, text="+")
plus_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
plus_button.grid(row=3, column=3, padx=8, pady=8)

divide_button = tkinter.Button(key_frame, text="÷")
divide_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
divide_button.grid(row=0, column=3, padx=8, pady=8)

percentage_button = tkinter.Button(key_frame, text="%")
percentage_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
percentage_button.grid(row=0, column=2, padx=8, pady=8)

parenthese_on_button = tkinter.Button(key_frame, text="(")
parenthese_on_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
parenthese_on_button.grid(row=0, column=0, padx=8, pady=8)

parenthese_off_button = tkinter.Button(key_frame, text=")")
parenthese_off_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
parenthese_off_button.grid(row=0, column=1, padx=8, pady=8)

clear_button = tkinter.Button(key_frame, text="C")
clear_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
clear_button.grid(row=4, column=0, padx=8, pady=8)

multiply_button = tkinter.Button(key_frame, text="x")
multiply_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
multiply_button.grid(row=1, column=3, padx=8, pady=8)

dot_button = tkinter.Button(key_frame, text=".")
dot_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
dot_button.grid(row=4, column=2, padx=8, pady=8)

equal_button = tkinter.Button(key_frame, text="=")
equal_button.config(width=5, height=1, background='#242424', foreground='white', font=('Arial', 30, 'bold'))
equal_button.grid(row=4, column=3, padx=8, pady=8)
