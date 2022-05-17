import math
import os
from drawers import imageTextDrawer as itd
from utils import textProcessor as tp
from PIL import Image, ImageColor

from utils.numberPostControler import attNumberFromFile, generateNameOfFile

TAMANHO = (500, 500)
COR = ImageColor.getrgb('#d16711')
OUTPUT_DIR = './outputs/'
NUMERO_POST = attNumberFromFile()
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#Cria uma nova imagem com os parâmetros
def montTextOnImages(TAMANHO, COR, NUMERO_POST, text):
    generatedName = NUMERO_POST
    NOME_ARQUIVO = (OUTPUT_DIR + f'{generatedName}.png', 'PNG')
    qtd_char_max = 39
    text_write_list = tp.brokeText(text, qtd_char_max)
    qtd_lines = len(text_write_list)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    if qtd_lines <= 1:
        pillow_img = Image.new('RGB', TAMANHO, color=COR)

        itd.drawTextOnImage(pillow_img, text_write_list[0], qtd_char_max)
        itd.drawNumberOfImage(pillow_img, NUMERO_POST)

        #Salva a imagem criada no caminho por parâmetro
        pillow_img.save(*NOME_ARQUIVO)
        pillow_img.show()

    elif qtd_lines > 1 and qtd_lines < tp.MAX_LINES_FOR_IMAGE:
        final_text = ""
        for line in text_write_list:
            final_text += line + "\n"
            
        pillow_img = Image.new('RGB', TAMANHO, color=COR)

        qtd_char_max = 39

        itd.drawTextOnImage(pillow_img, final_text, qtd_char_max)
        itd.drawNumberOfImage(pillow_img, NUMERO_POST)

        #Salva a imagem criada no caminho por parâmetro
        pillow_img.save(*NOME_ARQUIVO)
        pillow_img.show()
    
    else:
        loops = math.ceil(qtd_lines/tp.MAX_LINES_FOR_IMAGE)
        for i in range(0, loops):
            generatedName = generateNameOfFile(NUMERO_POST, i)
            final_text = ""
            pillow_img = Image.new('RGB', TAMANHO, color=COR)
            qtd_char_max = 39
            NOME_ARQUIVO = (OUTPUT_DIR + f'{generatedName}.png', 'PNG')

            for line in text_write_list[11*i : 11*i+11]:
                final_text += line + "\n"          
            
            itd.drawTextOnImage(pillow_img, final_text, qtd_char_max)
            itd.drawNumberOfImage(pillow_img, generatedName)            
            pillow_img.save(*NOME_ARQUIVO)
            pillow_img.show()

pillow_img = montTextOnImages(TAMANHO, COR, NUMERO_POST, text)