from src.drawers.imageTextDrawer import montTextOnImages
from src.utils.textReader import readTextsFromFile, renameUsedFile
from src.utils.numberPostControler import attNumberFile
from src.utils.fileManagement import verifySystemPaths
import src.utils.logUtil as log

TAMANHO = (1080, 1080)
verifySystemPaths()
texts = readTextsFromFile()

if texts:
    for text in texts:
        try:
            montTextOnImages(TAMANHO, text['text'])
            renameUsedFile(text['file'])
            attNumberFile()
        except Exception as error:
            log.erro(error.args)