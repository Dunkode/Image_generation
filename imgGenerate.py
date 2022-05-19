from PIL import ImageColor
from drawers.imageTextDrawer import montTextOnImages
from utils.textReader import readTextsFromFile
from utils.numberPostControler import attNumberFromFile, generateNameOfFile

TAMANHO = (500, 500)
COR = ImageColor.getrgb('#d16711')
NUMERO_POST = attNumberFromFile()
texts = readTextsFromFile()
# text = 

for text in texts:
    pillow_img = montTextOnImages(TAMANHO, COR, NUMERO_POST, text)