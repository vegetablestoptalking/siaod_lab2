from ring import RingList as ring_list
from tree import *
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from LinkedList import List as lst

a = ring_list()
data = ring_list()
tree = None


def unique():
    global a
    new_lst = ring_list()
    for i in range(len(a)):
        if not new_lst.find(a[i]):
            new_lst.append(a[i])
    return len(new_lst)


def append_in_rlist():
    global a
    a.append(txt.get())


def print_list():
    scr.insert(INSERT, '-----------ЛИСТ----------\n')
    scr.insert(INSERT, str(a) + '\n')
    scr.insert(INSERT, '-------------------------\n')


def append_in_tree():
    global tree
    temp = txt.get()
    data.append(temp)
    tree = insert(tree, temp)


def clean_tree():
    global tree
    global data
    tree = None
    data = lst()


def clean_list():
    global a
    a = ring_list()


def print_tree():
    scr.insert(INSERT, '-----------TREE----------\n')
    scr.insert(INSERT, str(data) + '\n')
    scr.insert(INSERT, '-------------------------\n')


def print_unique_tree():
    scr.insert(INSERT, '------second problem------\n')
    scr.insert(INSERT, str(tree) + '\n')
    scr.insert(INSERT, '-------------------------\n')

def print_unique_list():
    scr.insert(INSERT, '------first problem------\n')
    scr.insert(INSERT, str(unique()) + '\n')
    scr.insert(INSERT, '-------------------------\n')




window = Tk()
window.title("Лабораторная работа 2")
window.geometry('800x350')
txt = Entry(window, width=30)
txt.grid(column=2, row=0)
scr = scrolledtext.ScrolledText(window, width=40, height=10)
scr.grid(column=1, row=0)
btn_append_list = Button(window, text="Добавить в список",command=append_in_rlist)
btn_append_list.grid(column=1, row=1)
btn_clear_list = Button(window, text="Очистить список", command=clean_list)
btn_clear_list.grid(column=1, row=2)
btn_print_list = Button(window, text="Вывод списка", command=print_list)
btn_print_list.grid(column=1, row=3)

btn_append_list = Button(window, text="Добавить в дерево", command=append_in_tree)
btn_append_list.grid(column=2, row=1)
btn_clear_list = Button(window, text="Очистить дерево", command=clean_tree)
btn_clear_list.grid(column=2, row=2)
btn_print_list = Button(window, text="Вывод дерева", command=print_tree)
btn_print_list.grid(column=2, row=3)

btn_un_lst = Button(window, text="Задание 1", command=print_unique_list)
btn_un_lst.grid(column=3, row=1)
btn_un_tree = Button(window, text="Задание 2", command=print_unique_tree)
btn_un_tree.grid(column=3, row=2)

window.mainloop()
