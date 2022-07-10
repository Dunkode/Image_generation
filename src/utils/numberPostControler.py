from os.path import join
import string
from utils.fileManagement import readContentFromFile, verifyFile, writeDataInFile

#Diretório onde ficarão alguns dados para o programa funcionar
DIR = "data"

#Arquivo que conterá o número da postagem a ser escrita na imagem
FILE = "num_post.txt"

def attNumberFromFile():
    '''
    Função capaz de ler o número do arquivo num_post.txt
    e atualizá-lo em mais um.
    '''
    file_number = verifyFile(DIR, FILE, 0)
    oldNumber = int(readContentFromFile(file_number))
    writeDataInFile(file_number, oldNumber + 1)
    return oldNumber

def generateNameOfFile(NUMBER, index):
    '''
    Função que monta o nome do arquivo que conterá a imagem
    gerada, caso o texto usado gere mais de uma imagem.
    Ele usa uma lista contendo todas as letras do alfabeto
    em maísculo, permitindo que a frase possa ser divida
    em até 26 partes.

    NUMBER = número da postagem;
    index = a posição da imagem gerada.
    '''
    alfabeto = list(string.ascii_uppercase)
    return f"{NUMBER} - {alfabeto[index]}"
