from PIL import Image

def max_intensidade(imagem):
    max = 0
    for x in range(imagem.width):
        for y in range(imagem.height):
            if imagem.getpixel((x, y)) > max:
                max = imagem.getpixel((x, y))
    return max

def uniao(image1, image2):

    if image1.size > image2.size:
        image2.resize(image1.size)
    elif image2.size > image1.size:
        image1.resize(image2.size)
    
    image3 = Image.new('L', image1.size)

    intensidade_max = max_intensidade(image1)

    px1 = image1.load()
    px2 = image2.load() 

    for x in range(image3.width):
        for y in range(image3.height):
            if px1[x, y] == intensidade_max or px2[x, y] == intensidade_max:
                image3.putpixel((x, y), intensidade_max)
    
    return image3

def intersecao(image1, image2):
    if image1.size > image2.size:
        image2.resize(image1.size)
    elif image2.size > image1.size:
        image1.resize(image2.size)
    
    image3 = Image.new('L', image1.size)

    intensidade_max = max_intensidade(image1)

    px1 = image1.load()
    px2 = image2.load() 

    for x in range(image3.width):
        for y in range(image3.height):
            if px1[x, y] == intensidade_max and px2[x, y] == intensidade_max:
                image3.putpixel((x, y), intensidade_max)
    
    return image3

def diferenca(image1, image2):
    if image1.size > image2.size:
        image2.resize(image1.size)
    elif image2.size > image1.size:
        image1.resize(image2.size)

    image3 = Image.new('L', image1.size)
    intensidade_max = max_intensidade(image1)

    px1 = image1.load()
    px2 = image2.load() 

    for x in range(image3.width):
        for y in range(image3.height):
            image3.putpixel((x, y), px1[x, y] - px2[x, y])

    return image3

if __name__ == "__main__":
    #Uniao
    # image1 = Image.open("questao3/quadrilatero.bmp").convert('L')
    # image2 = Image.open("questao3/triangulo.bmp").convert('L')
    # image3 = uniao(image1, image2)
    # image3.save("questao3/uniao_quadr_triang.jpg")

    #Intersecao
    image1 = Image.open("questao3/circulo.bmp").convert('L')
    image2 = Image.open("questao3/triangulo.bmp").convert('L')
    image3 = intersecao(image1, image2)
    image3.save("questao3/intersecao_circ_triang.jpg")

    #Diferenca
    # image1 = Image.open("questao3/quadrilatero.bmp").convert('L')
    # image2 = Image.open("questao3/triangulo.bmp").convert('L')
    # image3 = diferenca(image1, image2)
    # image3.save("questao3/diferenca_quad_tria.jpg")