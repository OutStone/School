import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=300)
canvas.pack()

def julincina_zed (Pocet_cihel, Barva):
    for a in range(0,3):
        posunuti_y = a*75 
        for b in range(0, Pocet_cihel):
            canvas.create_rectangle(b*75, 280-posunuti_y, 70+b*75, 280-20-posunuti_y, fill=Barva)
            canvas.create_rectangle(15+b*75, 280-25-posunuti_y, 15+b*75+70, 280-25-20-posunuti_y, fill=Barva)
            canvas.create_rectangle(30+b*75, 280-50-posunuti_y, 30+b*75+70, 280-50-20-posunuti_y, fill=Barva)

julincina_zed (5, "orange")

root.mainloop()