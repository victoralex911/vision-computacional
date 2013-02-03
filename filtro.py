import Tkinter
import Image, ImageTk
from sys import argv

file = argv[1]

im = Image.open(file).convert("RGB")
original = im
(x,y) = im.size

def b_and_w(scale):
    for i in range(x):
        for j in range(y):
            (r,g,b)=original.getpixel((i, j))
            mini = max((r,g,b))
            if(mini<scale):
                mini = 0
            else:
                mini = 255
            im.putpixel((i,j), (mini,mini,mini))

def grayscale(tipo):
    for i in range(x):
        for j in range(y):
            (r,g,b)=original.getpixel((i, j))
            if tipo == "min":
                gray = min((r,g,b))
            if tipo == "max":
                gray = max((r,g,b))
            if tipo == "r":
                gray = r
            if tipo == "g":
                gray = g
            if tipo == "b":
                gray = b
            if tipo == "prom":
                gray = (r+g+b)/3
            im.putpixel((i,j), (gray,gray,gray))

def blur(maxiter):
    iter = 0
    while iter < maxiter:
        for i in range(x):
            for j in range(y):
                prom = []
                k=0
                (r,g,b)=original.getpixel((i, j))
                if(i-1>=0):
                    (rn,gn,bn)=original.getpixel((i-1, j))
                    prom.append(max((rn,gn,bn)))
                    k+=1
                if(i+1<x):
                    (rs,gs,bs)=original.getpixel((i+1, j))
                    prom.append(max((rs,gs,bs)))
                    k+=1
                if(j+1<y):
                    (re,ge,be)=original.getpixel((i, j+1))
                    prom.append(max((re,ge,be)))
                    k+=1
                if(j-1>=0):
                    (ro,go,bo)=original.getpixel((i, j-1))
                    prom.append(max((ro,go,bo)))
                    k+=1
                promedio = 0;
                for valor in prom:
                    promedio+=valor
                promedio=promedio/k
                im.putpixel((i,j), (promedio,promedio,promedio))
        iter+=1

def color_blur(maxiter):
    iter = 0
    while iter < maxiter:
        for i in range(x):
            for j in range(y):
                promr = []
                promg = []
                promb = []
                k=0
                (r,g,b)=original.getpixel((i, j))
                if(i-1>=0):
                    (rn,gn,bn)=original.getpixel((i-1, j))
                    promr.append(rn)
                    promg.append(gn)
                    promb.append(bn)
                    k+=1
                if(i+1<x):
                    (rs,gs,bs)=original.getpixel((i+1, j))
                    promr.append(rs)
                    promg.append(gs)
                    promb.append(bs)
                    k+=1
                if(j+1<y):
                    (re,ge,be)=original.getpixel((i, j+1))
                    promr.append(re)
                    promg.append(ge)
                    promb.append(be)
                    k+=1
                if(j-1>=0):
                    (ro,go,bo)=original.getpixel((i, j-1))
                    promr.append(ro)
                    promg.append(go)
                    promb.append(bo)
                    k+=1
                promedior = 0
                promediog = 0
                promediob = 0
                for valor in promr:
                    promedior+=valor
                for valor in promg:
                    promediog+=valor
                for valor in promb:
                    promediob+=valor
                promedior=promedior/k
                promediog=promediog/k
                promediob=promediob/k
                im.putpixel((i,j), (promedior,promediog,promediob))
        iter+=1

if(argv[2]=="BW" or argv[2]=="bw"):
    if(len(argv)==4):
        b_and_w(int(argv[3]))
        im.save("BW_"+file)
    else:
        print "Introduzca la escala de blanco y negro como parametro."
if(argv[2]=="G" or argv[2]=="g"):
    if(len(argv)==4):
        grayscale(argv[3])
        im.save("G_"+file)
    else:
        print "Introduzca el tipo de escala de gris (min, max, r, g, b, prom)."
if(argv[2]=="B" or argv[2]=="b"):
    if(len(argv)==4):
        blur(int(argv[3]))
        im.save("B_"+file)
    else:
        print "Introduzca el numero de iteraciones de blur como parametro."
if(argv[2]=="CB" or argv[2]=="cb"):
    if(len(argv)==4):
        color_blur(int(argv[3]))
        im.save("CB_"+file)
    else:
        print "Introduzca el numero de iteraciones de blur como parametro."
ventana = Tkinter.Tk()
im2 = ImageTk.PhotoImage(im)
Tkinter.Label(ventana, image=im2).pack()

ventana.mainloop()
