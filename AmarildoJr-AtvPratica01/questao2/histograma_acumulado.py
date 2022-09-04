from PIL import Image
from grafico import grafico
from histograma import histograma

def histograma_acumulado(imagem):
    h_acumulado = histograma(imagem)
    for i in range(1, len(h_acumulado)):
        h_acumulado[i] += h_acumulado[i-1]
    return h_acumulado

if __name__ == "__main__":
    ha = histograma_acumulado("lena_gray.bmp")

    intensidades = []
    for i in range (0, len(ha)):
        intensidades.append(i)

    grafico(intensidades, ha, "Histograma Acumulado \"lena_gray.png\"", 'histograma-acumulado.png')