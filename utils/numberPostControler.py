from os.path import join, exists
from os import mkdir
import string

DIR = "data"
FILE = "num_post.txt"
DIR_FILE = join(DIR, FILE)

def verifyFile():
    if exists(DIR_FILE):
        return DIR_FILE
    else:
        mkdir("data")
        open(DIR_FILE, "w+")
        setNumberFromFile(0)
        return DIR_FILE


def getNumberFromFile():
    with open(verifyFile(), "r") as fileNumber:
        data = fileNumber.read()
        return data

def setNumberFromFile(newNumber):
    with open(verifyFile(), "w") as fileNumber:
        fileNumber.write(str(newNumber + 1))

def attNumberFromFile():
    oldNumber = int(getNumberFromFile())
    setNumberFromFile(oldNumber)
    return oldNumber

def generateNameOfFile(NUMBER, index):
    alfabeto = list(string.ascii_uppercase)
    return f"{NUMBER} - {alfabeto[index]}"
