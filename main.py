import gui

line1 = ''


def clear_button():
    global line1
    line1 = ''
    gui.result_label.config(text='0')


gui.clear_button.config(command=clear_button)


def button_1():
    global line1
    line1 += '1'
    gui.result_label.config(text=line1)


gui.button_1.config(command=button_1)


def button_2():
    global line1
    line1 += '2'
    gui.result_label.config(text=line1)


gui.button_2.config(command=button_2)


def button_3():
    global line1
    line1 += '3'
    gui.result_label.config(text=line1)


gui.button_3.config(command=button_3)


def button_4():
    global line1
    line1 += '4'
    gui.result_label.config(text=line1)


gui.button_4.config(command=button_4)


def button_5():
    global line1
    line1 += '5'
    gui.result_label.config(text=line1)


gui.button_5.config(command=button_5)


def button_6():
    global line1
    line1 += '6'
    gui.result_label.config(text=line1)


gui.button_6.config(command=button_6)


def button_7():
    global line1
    line1 += '7'
    gui.result_label.config(text=line1)


gui.button_7.config(command=button_7)


def button_8():
    global line1
    line1 += '8'
    gui.result_label.config(text=line1)


gui.button_8.config(command=button_8)


def button_9():
    global line1
    line1 += '9'
    gui.result_label.config(text=line1)


gui.button_9.config(command=button_9)


def button_0():
    global line1
    line1 += '0'
    gui.result_label.config(text=line1)


gui.button_0.config(command=button_0)


def parenthese_on_button():
    global line1
    line1 += '('
    gui.result_label.config(text=line1)


gui.parenthese_on_button.config(command=parenthese_on_button)


def parenthese_off_button():
    global line1
    line1 += ')'
    gui.result_label.config(text=line1)


gui.parenthese_off_button.config(command=parenthese_off_button)


def dot_button():
    global line1
    line1 += '.'
    gui.result_label.config(text=line1)


gui.dot_button.config(command=dot_button)


def minus_button():
    global line1
    line1 += '-'
    gui.result_label.config(text=line1)


gui.minus_button.config(command=minus_button)


def plus_button():
    global line1
    line1 += '+'
    gui.result_label.config(text=line1)


gui.plus_button.config(command=plus_button)


def divide_button():
    global line1
    line1 += '/'
    gui.result_label.config(text=line1)


gui.divide_button.config(command=divide_button)


def percentage_button():
    global line1
    line1 += '%'
    gui.result_label.config(text=line1)


gui.percentage_button.config(command=percentage_button)


def multiply_button():
    global line1
    line1 += '*'
    gui.result_label.config(text=line1)


gui.multiply_button.config(command=multiply_button)


def equal_button():
    global line1
    line2 = eval(line1)
    line1 += '\n\n' + str(line2)
    result = line1
    gui.result_label.config(text=result)
    line1 = ''


gui.equal_button.config(command=equal_button)


gui.main_window.mainloop()
