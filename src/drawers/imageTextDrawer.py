import math
import os
from os.path import join, exists
from PIL import Image, ImageFont, ImageDraw, ImageColor
from src.utils import textProcessor as tp
from src.drawers import imageTextDrawer as itd
from src.utils.numberPostControler import attNumberFromFile, generateNameOfFile
from src.utils.fileManagement import PATH_OUTPUT, PATH_FONT
import src.utils.logUtil as log

#Pasta onde serão salvas as imagens
OUTPUT_DIR = PATH_OUTPUT

#Fonte usada para gerar as imagens
FONT_DIR = join(PATH_FONT, 'TIMESI.TTF')

#Quantidade máxima de caracteres por linha
QTD_MAX_CHAR = 41

#Quantidade máxima de linhas por imagem
MAX_LINES_FOR_IMAGE = 13

#Cor de fundo da imagem
IMAGE_BACKGROUND_COLOR = ImageColor.getrgb('#d16711')

#Cor da fonte usada
COLOR_FONT = '#000000'

def drawTextOnImage(pillow_img, text_write):
    """
    Função utilizada para escrever texto em uma imagem.

    pillow_img= Instância de PIL.Image
    text_write= Texto a ser escrito na instância acima
    """
    width = 20
    height = calculateHeight(pillow_img.size[1], text_write)
    draw = ImageDraw.Draw(pillow_img)
    
    font  = ImageFont.truetype(FONT_DIR, 60)

    
    draw.text((width, height), 
          text_write, 
          font=font, 
          fill=COLOR_FONT)

def drawNumberOfImage(pillow_img, number):
    """
    Função utilizada para escrever a numeração do post.

    pillow_img= Instância de PIL.Image
    number= numeração a ser escrita na instância acima
    """
    width = 788
    height = 300
    draw = ImageDraw.Draw(pillow_img)
    font  = ImageFont.truetype('./fonts/TIMESBI.TTF', 62)

    
    draw.text((width - len(str(number)) * 2, (height//2)), 
                f'~{number}', 
                font=font, 
                fill=COLOR_FONT)

def calculateHeight(height, text):
    """
    Função utilizada para calcular a altura do texto a ser escrito

    height= Altura da imagem
    text= Texto que será escrito na imagem
    """
    qtd_lines = tp.calculeLineBrokes(text, QTD_MAX_CHAR)
    height = height//2

    if (qtd_lines > 8):
        for i in range(0, qtd_lines - 8):
            if i < 3:
                height -= 77
        return height

    else:
        return height


def montTextOnImages(TAMANHO, text):
    """
    Função utilizada para gerar a quantidade necessária de imagens.

    TAMANHO= dimensões da imagem
    COR= cor do fundo da imagem
    NUMERO_POST= numeração da imagem
    text= texto a ser escrito
    """

    if not exists(FONT_DIR):
        raise Exception("A fonte a ser usada não foi localizada no diretório.")
    
    NUMERO_POST = attNumberFromFile()
    NOME_ARQUIVO = (join(OUTPUT_DIR, f'{NUMERO_POST}.jpeg'), 'jpeg')
    text_write_list = tp.brokeText(text, QTD_MAX_CHAR)
    qtd_lines = len(text_write_list)


    #Se tem apenas uma linha a ser desenhada na imagem
    if qtd_lines <= 1:
        pillow_img = Image.new('RGB', TAMANHO, color=IMAGE_BACKGROUND_COLOR)

        itd.drawTextOnImage(pillow_img, text_write_list[0])
        itd.drawNumberOfImage(pillow_img, NUMERO_POST)

        #Salva a imagem criada no caminho por parâmetro
        pillow_img.save(*NOME_ARQUIVO)
        log.info(f"Imagem {NOME_ARQUIVO[0]} gerada.")
        
        # pillow_img.show()

    #Se tem mais de uma e menos que o máximo de linhas por imagem
    elif qtd_lines > 1 and qtd_lines <= MAX_LINES_FOR_IMAGE:
        final_text = ""
        for line in text_write_list:
            final_text += line + "\n"
            
        pillow_img = Image.new('RGB', TAMANHO, color=IMAGE_BACKGROUND_COLOR)

        itd.drawTextOnImage(pillow_img, final_text)
        itd.drawNumberOfImage(pillow_img, NUMERO_POST)

        #Salva a imagem criada no caminho por parâmetro
        pillow_img.save(*NOME_ARQUIVO)
        log.info(f"Imagem {NOME_ARQUIVO[0]} gerada.")

        # pillow_img.show()
    
    #Se tem mais do máximo de linhas por imagem
    #gerando uma imagem a cada MAX_LINES_FOR_IMAGE linhas de texto
    else:
        loops = math.ceil(qtd_lines/MAX_LINES_FOR_IMAGE)
        for i in range(0, loops):
            generatedName = generateNameOfFile(NUMERO_POST, i)
            final_text = ""
            pillow_img = Image.new('RGB', TAMANHO, color=IMAGE_BACKGROUND_COLOR)
            NOME_ARQUIVO = (join(OUTPUT_DIR, f'{generatedName}.jpeg'), 'jpeg')

            for line in text_write_list[(MAX_LINES_FOR_IMAGE * i) : ((MAX_LINES_FOR_IMAGE * i) + MAX_LINES_FOR_IMAGE)]:
                final_text += line + "\n"
            
            itd.drawTextOnImage(pillow_img, final_text)
            itd.drawNumberOfImage(pillow_img, generatedName)
            pillow_img.save(*NOME_ARQUIVO, keep=100)
            log.info(f"Imagem {generatedName} gerada.")
            
            # pillow_img.show()