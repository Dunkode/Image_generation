from drawers.imageTextDrawer import montTextOnImages
from utils.textReader import readTextsFromFile
from utils.numberPostControler import attNumberFromFile

TAMANHO = (500, 500)
texts = readTextsFromFile()

if texts:
    for text in texts:
        montTextOnImages(TAMANHO, text)