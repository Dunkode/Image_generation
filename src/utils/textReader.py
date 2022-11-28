from glob import glob
from os.path import join
from os import rename
import src.utils.fileManagement as fm
import src.utils.logUtil as log

INPUT_DIR = fm.PATH_INPUT

def readTextsFromFile():
    input_file = fm.verifyFile(INPUT_DIR)
    input_search_pattern = join(input_file, "*.txt")

    list_texts = []

    for text_file in glob(input_search_pattern):
        if "_used" not in text_file:
            list_texts.append(fm.readContentFromFile(text_file))
            rename(text_file, text_file + "_used")
            log.info(f"Texto do arquivo {text_file} carregado.")

    return list_texts
