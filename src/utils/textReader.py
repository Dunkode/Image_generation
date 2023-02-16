from glob import glob
from os.path import join
from os import rename
import src.utils.fileManagement as fm
import src.utils.logUtil as log
from src.utils.numberPostControler import readActualNumber

INPUT_DIR = fm.PATH_INPUT

def readTextsFromFile():
    input_file = fm.verifyFile(INPUT_DIR)
    input_search_pattern = join(input_file, "*.txt")

    text = []

    for text_file in glob(input_search_pattern):
        if "_used" not in text_file:
            txtEntry = {
                'file': '',
                'text': ''
            }
            
            txtEntry['file'] = text_file
            txtEntry['text'] = fm.readContentFromFile(text_file)
            text.append(txtEntry)
            
            log.info(f"Texto do arquivo {text_file} carregado.")

    return text

def renameUsedFile(file):
    rename(file, file + "_used_{}".format(readActualNumber()))
