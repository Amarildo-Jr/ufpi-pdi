from PIL import Image, ImageChops
from numpy import log2

def transformacao_linear(imagem, c , b):
    im = Image.open(imagem)
    im_saida = Image.new(mode = "L", size = (im.width, im.height))
    for i in range(0, im.height):
        for j in range(0, im.width):
            im_saida.putpixel((i, j), (c * im.getpixel((i, j)) + b))
    im_saida.save("questao4/letra-a.png")

def transformacao_logaritmica(imagem, c):
    im = Image.open(imagem)
    im_saida = Image.new(mode = "L", size = (im.width, im.height))
    for i in range(0, im.height):
        for j in range(0, im.width):
            im_saida.putpixel((i, j), round(c * log2(im.getpixel((i, j)) + 1)))
    im_saida.save("questao4/letra-b.png")

def transformacao_potencia(imagem, c, b):
    im = Image.open(imagem)
    im_saida = Image.new(mode = "L", size = (im.width, im.height))
    for i in range(0, im.height):
        for j in range(0, im.width):
            im_saida.putpixel((i, j), round (c * (im.getpixel((i, j)) + 1) ** b))
    im_saida.save("questao4/letra-c.png")

def transformacao(imagem, operacao, c, b):
    if operacao == 'a':
        transformacao_linear(imagem, c, b)
    elif operacao == 'b':
        transformacao_logaritmica(imagem, c)
    elif operacao == 'c':
        transformacao_potencia(imagem, c, b)

# transformacao("lena_gray.bmp", 'a', 1, 1)
    # c=0, b=0; c=1, b=0; c=1, b=1; c=1, b=50; c=1, b=-50; c=-1, b=100; c=2, b=100;

# transformacao("lena_gray.bmp", 'b', 1, 0)
    # c=0; c=1; c=2; c=4; c=8; c=16; c=32; c=64

transformacao("lena_gray.bmp", 'c', 1, 0.67)
    # c=0, b=...; c=1, b=0.2; c=1, b=0.4; c=1, b=0.67; c=1, b=1; c=1, b=1.5; c=2, b=1; c=3, b=1





# lena_gray = "lena_gray.bmp"
# lena_gray_transf = "questao4/letra-c.png"

# diferenca_lg = ImageChops.subtract (Image.open(lena_gray_transf), Image.open(lena_gray))
# diferenca_lg.save("questao4/diferenca-transf-lena_gray.bmp")