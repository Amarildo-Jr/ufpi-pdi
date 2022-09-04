from PIL import Image

def mascara_media(image, mascara):
    n = 0

    for mascara_i in range(len(mascara)):
        for mascara_j in range(len(mascara[0])):
            n += mascara[mascara_i][mascara_j] 

    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += image.getpixel((x + i - 1, y + j - 1)) * mascara[i][j]
            px[x, y] = int (sum / n)

    return imagem_saida

def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        return (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2
    else:
        return lista[len(lista) // 2]

def mascara_mediana(image):
    imagem_saida = Image.new("L", image.size)
    
    px = image.load()
    px_saida = imagem_saida.load()

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            lista = []
            for i in range(3):
                for j in range(3):
                    lista.append(px[x + i - 1, y + j - 1])
            imagem_saida.putpixel((x, y), mediana(lista))
    
    return imagem_saida


if __name__ == "__main__":
    image = Image.open("lena_ruido.bmp")

    # mascara = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    # mascara = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # mascara = [[1, 3, 1], [3, 16, 3], [1, 3, 1]]
    # mascara = [[0, 1, 0], [1, 4, 1], [0, 1, 0]]

    # imagem_media = mascara_media(image, mascara)
    # imagem_media.save("questao2/media-8.jpg")

    # imagem_suavizada = Image.open("questao2/mediana3x.jpg")
    # imagem_mediana = mascara_mediana(imagem_suavizada)
    # imagem_mediana.save("questao2/mediana4x.jpg")
