from drawers.imageTextDrawer import montTextOnImages
from utils.textReader import readTextsFromFile
from utils.numberPostControler import attNumberFromFile

TAMANHO = (500, 500)
NUMERO_POST = attNumberFromFile()
texts = readTextsFromFile()

if texts:
    for text in texts:
        pillow_img = montTextOnImages(TAMANHO, NUMERO_POST, text)