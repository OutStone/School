from tkinter import *
import math
import os

root = Tk()
root.geometry("700x500")
root.title('Pyramida')

canvasSize = {
    'width' : 700,
    'height' : 500
}

canvas = Canvas(root, width=canvasSize['width'], height=canvasSize['height'])
canvas.pack()

def translate(value):
    return canvasSize['height'] - value

while True:
    
    param = int(input('pocet pater pyramidy: '))
    canvas.delete('all')

    rectSize = 2
    startPos = {
        'x' : 10,
        'y' : 30
    }

    toDraw = param*(param+1)/2
    behindMe = 0

    for j in range(param):

        ##loading bar
        os.system('cls')
        fraction = behindMe/toDraw

        num = math.floor(20*fraction)
        print('='*num + '-'*(20-num))

        onLine = param-j
        for i in range(onLine):

            Start = {
                'x' : startPos['x'] + i*rectSize + j*rectSize/2,
                'y' : translate(startPos['y'] + j*rectSize)
            }

            canvas.create_rectangle(Start['x'], Start['y'], Start['x'] + rectSize, Start['y'] + rectSize, fill='red')
            # print(i)
            behindMe += 1
    
    os.system('cls')
    print('='*20)