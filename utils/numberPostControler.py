from os.path import join
import string
from utils.fileManagement import readContentFromFile, verifyFile, writeDataInFile

DIR = "data"
FILE = "num_post.txt"

def attNumberFromFile():
    file_number = verifyFile(DIR, FILE, 0)
    oldNumber = int(readContentFromFile(file_number))
    writeDataInFile(file_number, oldNumber + 1)
    return oldNumber

def generateNameOfFile(NUMBER, index):
    alfabeto = list(string.ascii_uppercase)
    return f"{NUMBER} - {alfabeto[index]}"
