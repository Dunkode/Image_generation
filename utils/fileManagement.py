from os.path import join, exists
from os import mkdir

def verifyFile(dir_name, file_name=None, initial_value = ""):
    directory = join(dir_name, file_name) if file_name else dir_name

    if not exists(dir_name):
        mkdir(dir_name)
    
    if file_name:
        if not exists(directory):
            writeDataInFile(directory, initial_value)      

    return directory

def writeDataInFile(file_directory, data):
    with open(file_directory, "w") as opened_file:
        opened_file.write(str(data))

def readContentFromFile(file_directory):
    with open(file_directory, "r") as opened_file:
        return opened_file.read()
    
        
