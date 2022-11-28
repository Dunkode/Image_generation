from os.path import join, exists
from os import mkdir, getcwd
import src.utils.logUtil as log

PATH_DATA = join(getcwd(), 'data')
PATH_OUTPUT = join(getcwd(), 'outputs')
PATH_INPUT = join(getcwd(), 'inputs')
PATH_FONT = join(getcwd(), 'fonts')

def verifyFile(dir_name, file_name=None, initial_value = ""):
    '''
    Função usada para verificar se um diretório existe.
    Se ele não existir, será criado.
    Podemos passar por parâmetro o nome de um arquivo
    que pode ser criado dentro dessse diretório.
    Também é possível apontar um valor inicial para
    esse arquivo.

    dir_name = caminho de diretório a se analisar;
    file_name = arquivo que pode ser criado no diretório informado;
    initial_value = um valor inicial pré-definido que pode ser
    inserido no arquivo.
    '''
    directory = join(dir_name, file_name) if file_name else dir_name

    if not exists(dir_name):
        mkdir(dir_name)
        log.info(f"Diretório {dir_name} criado.")
    
    if file_name:
        if not exists(directory):
            writeDataInFile(directory, initial_value)
            log.info(f"Arquivo {directory} criado com o valor inicial {initial_value}.")      

    return directory

def writeDataInFile(file_directory, data):
    '''
    Função para escrever dados em um arquivo.

    file_directory = caminho do arquivo;
    data = dados a serem escritos.
    '''
    with open(file_directory, "w") as opened_file:
        opened_file.write(str(data))

def readContentFromFile(file_directory):
    '''
    Função para ler dados em um arquivo.

    file_directory = caminho do arquivo;
    '''
    with open(file_directory, "r", encoding='utf-8') as opened_file:
        return opened_file.read()
    

def verifySystemPaths():
    '''
    Função para verificar se as pastas necessárias para 
    rodar o sistema existem.
    Se elas não existirem, serão criadas.
    '''
    
    if not exists(PATH_DATA):
        mkdir(PATH_DATA)
        log.info(f"Diretório {PATH_DATA} criado.")
    
    if not exists(PATH_OUTPUT):
        mkdir(PATH_OUTPUT)
        log.info(f"Diretório {PATH_OUTPUT} criado.")
    
    if not exists(PATH_INPUT):
        mkdir(PATH_INPUT)
        log.info(f"Diretório {PATH_INPUT} criado.")

    if not exists(PATH_FONT):
        mkdir(PATH_FONT)
        log.info(f"Diretório {PATH_FONT} criado.")

    log.info("Diretórios base verificados com suceso.")