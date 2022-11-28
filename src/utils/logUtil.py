COLOR_INFO = "\033[1;32m"
COLOR_WARNING = '\033[1;33m'
COLOR_ERRO = '\033[1;31m'
RESET = '\033[m'


def info(str):
    print(f"{COLOR_INFO}[INFO]{RESET} {str}")

def warning(str):
    print(f"{COLOR_WARNING}[WARNING]{RESET} {str}")

def erro(str):
    print(f"{COLOR_ERRO}[ERRO]{RESET} {str}")