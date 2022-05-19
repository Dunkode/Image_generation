from glob import glob
from os.path import join
from utils.fileManagement import readContentFromFile, verifyFile

INPUT_DIR = "./inputs/"

def readTextsFromFile():
    input_file = verifyFile(INPUT_DIR)
    input_search_pattern = join(input_file, "*.txt")

    list_texts = []

    for text_file in glob(input_search_pattern):
        list_texts.append(readContentFromFile(text_file))

    return list_texts
