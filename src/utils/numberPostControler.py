from os.path import join
import string
import src.utils.fileManagement as fm
import src.utils.logUtil as log

#Diretório onde ficarão alguns dados para o programa funcionar
DIR = fm.PATH_DATA

#Arquivo que conterá o número da postagem a ser escrita na imagem
FILE = join(fm.PATH_DATA, "num_post.txt")

def attNumberFromFile():
    '''
    Função capaz de ler o número do arquivo num_post.txt
    e atualizá-lo em mais um.
    '''
    file_number = fm.verifyFile(DIR, FILE, 0)
    oldNumber = int(fm.readContentFromFile(file_number))
    fm.writeDataInFile(file_number, oldNumber + 1)
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
