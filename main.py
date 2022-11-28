from src.drawers.imageTextDrawer import montTextOnImages
from src.utils.textReader import readTextsFromFile
from src.utils.fileManagement import verifySystemPaths
import src.utils.logUtil as log

TAMANHO = (500, 500)
verifySystemPaths()
texts = readTextsFromFile()

if texts:
    for text in texts:
        try:
            montTextOnImages(TAMANHO, text)
        except Exception as error:
            log.erro(error.args)