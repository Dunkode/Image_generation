from glob import glob
from os.path import join
from os import rename
from utils.fileManagement import readContentFromFile, verifyFile

INPUT_DIR = "./inputs/"

def readTextsFromFile():
    input_file = verifyFile(INPUT_DIR)
    input_search_pattern = join(input_file, "*.txt")

    list_texts = []

    for text_file in glob(input_search_pattern):
        if "_used" not in text_file:
            list_texts.append(readContentFromFile(text_file))
            rename(text_file, text_file + "_used")

    return list_texts
