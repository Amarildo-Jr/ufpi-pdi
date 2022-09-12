from PIL import Image

def filtro_sobel(imagem):
    filtro = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    # filtro = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    imagem_saida = Image.new("L", imagem.size)
    for x in range(1, imagem.width - 1):
        for y in range(1, imagem.height - 1):
            soma = 0
            for i in range(3):
                for j in range(3):
                    soma += imagem.getpixel((x + i - 1, y + j - 1)) * filtro[i][j]
            imagem_saida.putpixel((x, y), int(soma))
    return imagem_saida

if __name__ == "__main__":
    imagem_original = Image.open("lena_gray.bmp")
    filtro_sobel(imagem_original).save("questao1/bordas/sobel_ver.jpg")