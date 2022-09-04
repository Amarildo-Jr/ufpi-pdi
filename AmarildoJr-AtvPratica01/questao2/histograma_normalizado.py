from PIL import Image
from grafico import grafico
from histograma import histograma

def histograma_normalizado(imagem):
    h_normalizado = histograma(imagem)
    im = Image.open(imagem)
    for i in range(0, len(h_normalizado)):
        h_normalizado[i] /= im.width*im.height
    return h_normalizado

if __name__ == "__main__":

    hn = histograma_normalizado("lena_gray.bmp")

    intensidades = []
    for i in range (0, len(hn)):
        intensidades.append(i)

    grafico(intensidades, hn, "Histograma Normalizado \"lena_gray.png\"", 'histograma-normalizado.png')