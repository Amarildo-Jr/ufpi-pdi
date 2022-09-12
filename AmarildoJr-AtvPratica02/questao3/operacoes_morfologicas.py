from PIL import Image

def max_intensidade(imagem):
    max = 0
    for x in range(imagem.width):
        for y in range(imagem.height):
            if imagem.getpixel((x, y)) > max:
                max = imagem.getpixel((x, y))
    return max

def uniao(imagem1, imagem2):
    if imagem1.size > imagem2.size:
        imagem2.resize(imagem1.size)
    elif imagem2.size > imagem1.size:
        imagem1.resize(imagem2.size)
    
    imagem3 = Image.new('L', imagem1.size, "black")

    intensidade_max = max_intensidade(imagem1)

    px1 = imagem1.load()
    px2 = imagem2.load() 

    for x in range(imagem3.width):
        for y in range(imagem3.height):
            if px1[x, y] == intensidade_max or px2[x, y] == intensidade_max:
                imagem3.putpixel((x, y), intensidade_max)
    
    return imagem3

def intersecao(imagem1, imagem2):
    if imagem1.size > imagem2.size:
        imagem2.resize(imagem1.size)
    elif imagem2.size > imagem1.size:
        imagem1.resize(imagem2.size)
    
    imagem3 = Image.new('L', imagem1.size)

    intensidade_max = max_intensidade(imagem1)

    px1 = imagem1.load()
    px2 = imagem2.load() 

    for x in range(imagem3.width):
        for y in range(imagem3.height):
            if px1[x, y] == intensidade_max and px2[x, y] == intensidade_max:
                imagem3.putpixel((x, y), intensidade_max)
    
    return imagem3

def diferenca(imagem1, imagem2):
    if imagem1.size > imagem2.size:
        imagem2.resize(imagem1.size)
    elif imagem2.size > imagem1.size:
        imagem1.resize(imagem2.size)

    imagem3 = Image.new('L', imagem1.size)

    px1 = imagem1.load()
    px2 = imagem2.load() 

    for x in range(imagem3.width):
        for y in range(imagem3.height):
            imagem3.putpixel((x, y), px1[x, y] - px2[x, y])

    return imagem3

if __name__ == "__main__":
    #Uniao
    # imagem1 = Image.open("questao3/quadrilatero.bmp").convert('L')
    # imagem2 = Image.open("questao3/triangulo.bmp").convert('L')
    # imagem3 = uniao(imagem1, imagem2)
    # imagem3.save("questao3/uniao_quadr_triang.jpg")

    #Intersecao
    imagem1 = Image.open("questao3/circulo.bmp").convert('L')
    imagem2 = Image.open("questao3/triangulo.bmp").convert('L')
    imagem3 = intersecao(imagem1, imagem2)
    imagem3.save("questao3/intersecao_circ_triang.jpg")

    #Diferenca
    # imagem1 = Image.open("questao3/quadrilatero.bmp").convert('L')
    # imagem2 = Image.open("questao3/triangulo.bmp").convert('L')
    # imagem3 = diferenca(imagem1, imagem2)
    # imagem3.save("questao3/diferenca_quad_tria.jpg")