from tkinter import *

root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

sqr = {
    'a' : 20
}
rctg = {
    'x':43,
    'y':20
}
space = 3

for sth in range(1):
    num = int(input('pocet dlazdic: '))

    if num % 2 == 1:
        print('cislo neni sude')
        break
    Barva = input('barva: ')

    for i in range(4):
        Main_Y = 46*i
        Start_X = 0

        for a in range(num):
            X_offset = sqr['a'] + space
            canvas.create_rectangle(Start_X + X_offset*a, Main_Y, Start_X + X_offset*a + sqr['a'], Main_Y + sqr['a'], fill=Barva)

        Main_Y += 23

        for b in range(int(num/2)):
            X_offset = rctg['x'] + space
            canvas.create_rectangle(Start_X + X_offset*b, Main_Y, Start_X + X_offset*b + rctg['x'], Main_Y + rctg['y'], fill=Barva)

root.mainloop()
        