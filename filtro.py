import Tkinter 
import Image, ImageTk

im = Image.open('cat.jpeg').convert("RGB")
(x,y) = im.size

for i in range(x):
    for j in range(y):
        (r,g,b)=im.getpixel((i, j))
        maximo = max((r,g,b))
        im.putpixel((i,j), (maximo,maximo,maximo))
ventana = Tkinter.Tk()
im2 = ImageTk.PhotoImage(im)

Tkinter.Label(ventana, image=im2).pack()

ventana.mainloop()