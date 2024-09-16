import tkinter as tk

def num():
    pass

sx = 10
sy = 50
w = 50
h = 60

window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)

tk.Button(window, text='Очистить', width=14, height=2, command=num).place(x=sx, y=sy)
for i in range(3):
    for j in range(3):
        tk.Button(window, text=(i*3+j+1), width=2, height=2, command=num).place(x=sx+j*w, y=sy+(i+1)*h)

tk.Button(window, text='0', width=14, height=2, command=num).place(x=sx, y=sy+4*h)

key = 0;
for op in ['/', '*', '-', '+']:
    tk.Button(window, text=op, width=2, height=2, command=num).place(x=sx+3*w, y=sy+key*h)
    key += 1;

tk.Button(window, text='=', width=2, height=2, command=num).place(x=sx+3*w, y=sy+4*h)

tk.Text(width=25, height=1, bg="black", fg='white', wrap=tk.NONE).pack()

window.mainloop()