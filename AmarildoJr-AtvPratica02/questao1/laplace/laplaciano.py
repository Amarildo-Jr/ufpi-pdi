from PIL import Image

def max_intensidade(imagem):
    max = 0
    for x in range(imagem.width):
        for y in range(imagem.height):
            if imagem.getpixel((x, y)) > max:
                max = imagem.getpixel((x, y))
    return max

def min_intensidade(imagem):
    min = 255
    for x in range(imagem.width):
        for y in range(imagem.height):
            if imagem.getpixel((x, y)) < min:
                min = imagem.getpixel((x, y))
    return min

def normalizar(imagem):
    max = max_intensidade(imagem)
    min = min_intensidade(imagem)

    imagem_normalizada = Image.new("L", imagem.size)

    px = imagem.load()

    for x in range(imagem.width):
        for y in range(imagem.height):
            imagem_normalizada.putpixel((x, y), int((px[x, y] - min)))
    
    px = imagem_normalizada.load()
    max = max_intensidade(imagem_normalizada)
    for x in range(imagem.width):
        for y in range(imagem.height):
            imagem_normalizada.putpixel((x, y), int(255 * (px[x, y] / max)))
    
    imagem_normalizada.save("questao1/laplace/normalizada.jpg")
    return imagem

def soma(imagem1, imagem2):
    imagem_saida = Image.new("L", imagem1.size)

    px = imagem_saida.load()

    for x in range(imagem1.width):
        for y in range(imagem1.height):
            px[x, y] = imagem1.getpixel((x, y)) + imagem2.getpixel((x, y))
    
    return imagem_saida

def filtro_laplaciano(imagem, filtro):

    imagem_saida = Image.new("L", imagem.size)

    px = imagem_saida.load()

    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            # Soma entre o produto do filtro e a imagem
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += imagem.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
            if (filtro[len(filtro) // 2][len(filtro) // 2] < 0):
                sum = -sum
            imagem_saida.putpixel((x, y), imagem.getpixel((x, y)) + sum)

    return imagem_saida

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
    
    filtro = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    # filtro = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]

    # filtro = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    # filtro = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    
    # imagem = Image.open("lena_gray.bmp")
    # imagem_laplaciano = filtro_laplaciano(imagem, filtro)
    # imagem_laplaciano.save("questao1/laplace/laplaciano+8.jpg")

    # imagem = Image.open("questao1/laplace/laplaciano-4.jpg")
    # imagem1 = Image.open("questao1/laplace/laplaciano+4.jpg")
    # imagem_original = Image.open("lena_gray.bmp")

    # imagem_diferenca = diferenca(imagem1, imagem)
    # imagem_diferenca.save("questao1/laplace/diferenca.jpg")