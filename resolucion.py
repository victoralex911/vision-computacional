import math
from sys import argv

pixeles = argv[1]
proporcion = argv[2]

def sacar_resolucion(pixeles, proporcion):
    propx , propy = proporcion.split(':')
    pix = ""
    for i in range(len(pixeles)):
        if(pixeles[i].isdigit()):
            pix+=pixeles[i]
    print pix, propx, propy
    propx = (int(pix)/int(propx))*1024
    propy = (int(pix)/int(propy))*1024
    print pix, propx, propy
sacar_resolucion(pixeles,proporcion)
