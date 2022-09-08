from PIL import Image

def dilatacao(image, elemento_estruturante, centro):
    imagem_saida = Image.new("RGB", image.size, "white")

    intensidade_min = (0, 0, 0)

    for x in range(imagem_saida.width):
        for y in range(imagem_saida.height):
            if(image.getpixel((x, y)) == intensidade_min):
                for i in range(len(elemento_estruturante)):
                    for j in range(len(elemento_estruturante[i])):
                        if(elemento_estruturante[i][j] == 1):
                            try:
                                imagem_saida.putpixel((x + i - centro[0], y + j - centro[1]), intensidade_min)
                            except:
                                pass
                                
    return imagem_saida

def erosao(image, elemento_estruturante, centro):
    imagem_saida = Image.new("RGB", image.size, "white")

    intensidade_min = (0, 0, 0)
    for x in range(imagem_saida.width):
        for y in range(imagem_saida.height):
            if image.getpixel((x, y)) == intensidade_min:
                elemento_est_encontrado = True
                for i in range(len(elemento_estruturante)):
                    for j in range(len(elemento_estruturante[i])):
                        # imagem_saida.putpixel((x + i - centro[0], y + j - centro[1]), 0)
                        if elemento_estruturante[i][j] == 1:
                            valor_px = (0, 0, 0)
                            try:
                                valor_px = image.getpixel((x + i - centro[0], y + j - centro[1]))
                            except:
                                pass
                            if not valor_px == intensidade_min:
                                elemento_est_encontrado = False
                        
                if elemento_est_encontrado:
                    imagem_saida.putpixel((x, y), intensidade_min)
    return imagem_saida

def abertura(image, elemento_estruturante, centro):
    imagem_erodida = erosao(image, elemento_estruturante, centro)
    imagem_saida = dilatacao(imagem_erodida, elemento_estruturante, centro)
    return imagem_saida

def fechamento(image, elemento_estruturante, centro):
    imagem_dilatada = dilatacao(image, elemento_estruturante, centro)
    imagem_saida = erosao(imagem_dilatada, elemento_estruturante, centro)
    return imagem_saida

def somar_imagens(imagem1, imagem2):
    imagem_saida = imagem1.copy()
    pixels1 = imagem1.load()
    pixels2 = imagem2.load()

    for i in range(imagem_saida.width):
        for j in range(imagem_saida.height):
            if pixels1[i, j] != pixels2[i, j] and pixels2[i, j] == (0, 0, 0):
                imagem_saida.putpixel((i, j), pixels2[i, j])

    return imagem_saida

def diferenca(image1, image2):
    if image1.size > image2.size:
        image2.resize(image1.size)
    elif image2.size > image1.size:
        image1.resize(image2.size)

    image3 = Image.new('L', image1.size)

    px1 = image1.load()
    px2 = image2.load() 

    for x in range(image3.width):
        for y in range(image3.height):
            image3.putpixel((x, y), px1[x, y] - px2[x, y])

    return image3