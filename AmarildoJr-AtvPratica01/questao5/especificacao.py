from tkinter import image_names
from PIL import Image, ImageChops
import numpy as np
import sys
sys.path.insert(0, "questao2")
sys.path.insert(1, "questao3")

from equalizacao import equalizar
from histograma import histograma
from grafico import grafico

def especificar_histograma(imagem_entrada, imagem_especificada):
    im = Image.open(imagem_entrada)
    im_saida = Image.new(mode = "L", size = im.size)
    hist = equalizar((imagem_entrada))
    hist_esp = equalizar((imagem_especificada))
    histograma_final = []
   
    arr = np.array(hist)
    for i in hist_esp:
        difference_array = np.absolute(arr-i)
        index = difference_array.argmin()
        histograma_final.append(arr[index])
    
    for i in range (im.size[0]):
        for j in range (im.size[1]):
            im_saida.putpixel((i, j), int (histograma_final[im.getpixel((i, j))]))
    im_saida.save(f"questao5/especificacao-{imagem_entrada}")
    return histograma_final

im = Image.open("lena_gray.bmp")
im1 = Image.open("image1.png")
h1 = histograma("lena_gray.bmp")
especificar_histograma("image1.png", "lena_gray.bmp")
h = histograma("questao5/especificacao-image1.png")
intensidades = []
for i in range (0, len(h1)):
    intensidades.append(i)
grafico(intensidades, h1, "Histograma \"lena_gray.png\"", 'hist-lena.png')
intensidades = []
for i in range (0, len(h)):
    intensidades.append(i)
grafico(intensidades, h, "Histograma Especificado \"image1.png\"", 'hist-especificado-image1.png')
