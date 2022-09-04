from PIL import Image

def imagem_fronteira(imagem, adjacencia):
    cores = {4:(10, 131, 127, 255), 8:(241, 57, 109, 255)}
    im = Image.open(imagem)
    im_saida = Image.new(mode = "RGB", size = (im.width, im.height), color = (0, 0, 0))

    nome_arquivo = f"folha-fronteira-adj{adjacencia}.png"

    px = im.load()
    for i in range(0, im.height):
        for j in range(0, im.width):
            if px[i, j] == (255, 255, 255, 255):
                if px[i, j + 1] == (0, 0, 0, 255) or px[i, j - 1] == (0, 0, 0, 255) or px[i + 1, j] == (0, 0, 0, 255) or px[i - 1, j] == (0, 0, 0, 255):
                    im_saida.putpixel((i, j), cores[adjacencia])
                    # im_saida.putpixel((i, j), (255, 255, 255, 255))
                elif adjacencia == 8:
                        if px[i + 1, j + 1] == (0, 0, 0, 255) or px[i - 1, j - 1] == (0, 0, 0, 255) or px[i + 1, j - 1] == (0, 0, 0, 255) or px[i - 1, j + 1] == (0, 0, 0, 255):
                            im_saida.putpixel((i, j), cores[adjacencia])
                            # im_saida.putpixel((i, j), (255, 255, 255, 255))
    im_saida.save(f"questao1/{nome_arquivo}")
    

imagem_fronteira("folha.png", 8)
imagem_fronteira("folha.png", 4)