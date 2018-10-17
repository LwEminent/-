from tkinter import *
from tkinter.ttk import *
import math
import sys


def my_frame(master):
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w


def exit():
    sys.exit()
    return exit


def my_button(master, text, command):
    w = Button(master, text=text, command=command, width=6)
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return w


def back(text):
    if len(text) > 0:
        return text[:-1]
    else:
        return text


def sin(text):
    sin = math.sin(math.radians(text))
    return sin


def cos(text):
    cos = math.cos(math.radians(text))
    return cos


def tan(text):
    tan = math.tan(math.radians(text))
    return tan


def asin(text):
    asin = math.asin(math.radians(text))
    return asin


def acos(text):
    acos = math.acos(math.radians(text))
    return acos


def atan(text):
    atan = math.atan(math.radians(text))
    return atan


def sec(text):
    sec = 1 / (math.cos(math.radians(text)))
    return sec


def csc(text):
    csc = 1 / (math.sin(math.radians(text)))
    return csc


def calc(text):
    try:
        if sep_flag.get() == 0:
            return eval(del_sep(text))
        else:
            return add_sep(str(eval(del_sep(text))))
    except (SyntaxError, ZeroDivisionError, NameError):
        return "语法错误或分母不能为0或找不到变量名，请重新输入"


def add_sep(text):
    dot_index = text.find('.')
    if dot_index > 0:
        text_head = text[:dot_index]
        text_tail = text[dot_index:]
    elif dot_index < 0:
        text_head = text
        text_tail = ''
    else:
        text_head = ''
        text_tail = text
    list_ = [char for char in text_head]
    length = len(list_)
    tmp_index = 3
    while length - tmp_index > 0:
        list_.insert(length - tmp_index, ',')
        tmp_index += 3
    list_.extend(text_tail)
    new_text = ''
    for char in list_:
        new_text += char
    return new_text


def del_sep(text):
    return text.replace(',', '')


def Math():
    lw = Tk()
    lw.geometry("300x100+600+300")
    lw.title("数学三角函数计算")
    style = Style()
    style.configure('TButton', padding=5)
    a = my_frame(lw)
    b = my_frame(lw)
    c = my_frame(lw)
    my_button(a, 'sin', lambda t=text: t.set(sin(float(t.get()))))
    my_button(a, 'cos', lambda t=text: t.set(cos(float(t.get()))))
    my_button(a, 'tan', lambda t=text: t.set(tan(float(t.get()))))
    my_button(b, 'asin(1-57.3)', lambda t=text: t.set(asin(float(t.get()))))
    my_button(b, 'acos(1-57.3)', lambda t=text: t.set(acos(float(t.get()))))
    my_button(b, 'atan', lambda t=text: t.set(atan(float(t.get()))))
    my_button(c, 'sec', lambda t=text: t.set(sec(float(t.get()))))
    my_button(c, 'csc', lambda t=text: t.set(csc(float(t.get()))))
    lw.mainloop()


def zs():
    lw = Tk()
    lw.geometry("300x100+600+300")
    lw.title("指数函数计算")
    r = StringVar()
    style = Style()
    style.configure('TButton', padding=5)
    ety=Entry(lw, textvariable=r).pack(expand=YES, fill=BOTH, padx=2, pady=4)

    a = my_frame(lw)
    b = my_frame(lw)
    my_button(a, '2', lambda t=text: t.set(float(t.get()) * float(t.get())))
    my_button(a, '3', lambda t=text: t.set(float(t.get()) * float(t.get()) * float(t.get())))
    my_button(a, 'n', lambda t=text: t.set(float(t.get())**(float(r.get()))))
    my_button(b, '（）½', lambda t=text: t.set(pow(float(t.get()), 0.5)))
    my_button(b, '（）⅓', lambda t=text: t.set(pow(float(t.get()), 1 / 3)))
    lw.mainloop()


wind = Tk()
wind.title("计算器")
wind.geometry("400x500+500+100")
main_menu = Menu(wind)
calc_menu = Menu(main_menu, tearoff=0)
calc_menu.add_command(label='三角函数计算', command=Math)
calc_menu.add_command(label='指数计算', command=zs)
calc_menu.add_command(label='退出', command=exit)
main_menu.add_cascade(label='计算', menu=calc_menu)
text = StringVar()
sep_flag = IntVar()
sep_flag.set(0)
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_checkbutton(label='显示千位分隔符', variable=sep_flag, command=lambda t=text: t.set(add_sep(t.get())))
main_menu.add_cascade(label='视图', menu=view_menu)
wind['menu'] = main_menu
Entry(wind, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)
style = Style()
style.configure('TButton', padding=4)
fedit = my_frame(wind)
my_button(fedit, 'Clear', lambda t=text: t.set(''))
my_button(fedit, 'Backspace', lambda t=text: t.set(back(t.get())))
my_button(fedit, '±', lambda t=text: t.set('-(' + t.get() + ')'))
my_button(fedit, 'e', lambda t=text: t.set(math.e))
for key in ('789/', '456*', '123-', '0.+='):
    fsymb = my_frame(wind)
    for char in key:
        if char == '=':
            my_button(fsymb, char, lambda t=text: t.set(calc(t.get())))
        else:
            my_button(fsymb, char, lambda t=text, c=char: t.set(t.get() + c))
wind.mainloop()
