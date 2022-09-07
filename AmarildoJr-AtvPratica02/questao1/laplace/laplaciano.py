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

def filtro_laplaciano(image):
    # filtro = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    # filtro = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
    # filtro = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    filtro = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

    imagem_saida = Image.new("L", image.size)

    px = imagem_saida.load()

    min = 255
    max = 0

    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            # Soma entre o produto do filtro e a imagem
            sum = 0
            for i in range(3):
                for j in range(3):
                    sum += image.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
                    if (sum < min):
                        min = sum
                    if (sum > max):
                        max = sum
            px[x, y] = int (sum)

    print(f"min = {min} e max = {max}")
    return normalizar(imagem_saida)

if __name__ == "__main__":
    image = Image.open("lena_gray.bmp")
    new_image = filtro_laplaciano(image)
    new_image.save("questao1/laplace/laplaciano--4.jpg")