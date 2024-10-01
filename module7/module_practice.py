import tkinter
import os
import time
from tkinter import filedialog, messagebox

def file_select():
    filename = filedialog.askopenfilename(initialdir='./', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '*.txt'), ('Все файлы', '*.*')))
    filetime = os.path.getmtime(filename)
    text['text'] += '\n' + filename + '\n' + 'Изменен: ' + time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

def show_info():
    info_text = "Это простой проводник.\n\n" \
                "Чтобы начать пользоваться, нажмите кнопку 'Выбрать файл'."
    messagebox.showinfo("Как пользоваться", info_text)

def show_about():
    about_text = "Автор: Андрей\n" \
                    "Версия: 1.0\n" \
                    "Это демонстрационное приложение на Python с использованием Tkinter."
    messagebox.showinfo("Информация", about_text)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x150')
window.configure(bg="black")
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=4, width=44, background="silver")
text.grid(row=1, column=1, columnspan=3)
button_select = tkinter.Button(window, text='Выбрать файл', height=2, width=20, command=file_select)
button_select.grid(row=2, column=2)
text1 = tkinter.Label(window, text=' ', height=3, width=10, background="silver")
text1.grid(row=2, column=1)
text2 = tkinter.Label(window, text=' ', height=3, width=10, background="silver")
text2.grid(row=2, column=3)

# Создание меню
menu = tkinter.Menu(window)
window.config(menu=menu)

# Добавление пункта "Info"
info_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="Как пользоваться", command=show_info)

# Добавление пункта "About"
about_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Информация", command=show_about)

window.mainloop()