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

def filtro_laplaciano(imagem):
    filtro = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    # filtro = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]

    # filtro = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    # filtro = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

    imagem_saida = Image.new("L", imagem.size)

    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            # Soma entre o produto do filtro e a imagem
            soma = 0
            for i in range(3):
                for j in range(3):
                    soma += imagem.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
            if (filtro[len(filtro) // 2][len(filtro) // 2] < 0):
                soma = -soma
            imagem_saida.putpixel((x, y), imagem.getpixel((x, y)) + soma)

    return imagem_saida

if __name__ == "__main__":
    
    imagem = Image.open("lena_gray.bmp")
    imagem_laplaciano = filtro_laplaciano(imagem)
    imagem_laplaciano.save("questao1/laplace/laplaciano+8.jpg")
