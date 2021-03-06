import math

def brokeText(text, max_char):
    '''
    Aqui, é feita a quebra do texto passado por parâmetro
    e essa quebra é feita a partir do parâmetro max_char.
    É retornado uma lista, onde têm-se as quebras.
    As quebras são feitas de maneira 'inteligente', pois
    respeita virgulas e pontos, mas isso está detalhado na
    função getTextBrokenInLines.

    text = texto a ser quebrado;
    max_char = quantidade máxima de caracteres.
    '''
    separeted_texts = []

    if len(text) > max_char:
        qtd_cuts = calculeLineBrokes(text, max_char)        
        separeted_texts = getTexBrokenInLines(text, max_char, qtd_cuts).split("\n")      
        return separeted_texts

    else:
        separeted_texts.append(text)
        return separeted_texts

def calculeLineBrokes(text, max_char):
    '''
    Através dos parâmetros, é retornada a quantidade
    de quebras que o texto deverá ter.
    Acontece um arredondamento para cima, pois como
    estamos lidando com texto, arredondar para baixo
    ocasionaria perdas.

    text = texto base;
    max_char = quantidade máxima de caracteres.
    '''
    return math.ceil(len(text)/max_char)
    

def getTexBrokenInLines(text, max_char, qtd_cuts):
    '''
    Essa função é o cérebro do programa.
    Aqui, recebemos o texto a ser cortado, a quantidade
    máxima de caracteres por linha e quantas linhas esse
    texto pode ser quebrado.
    '''
    final_string = ''
    qtd_char_rem = 0
    for i in range(0, qtd_cuts + 1):
        pos_no_linebroke = len(final_string.replace('\n', ''))

        str_aux = text[0 if len(final_string) == 0 
                        else pos_no_linebroke + qtd_char_rem: 
                        pos_no_linebroke + max_char
                        ]

        if str_aux != '':
            while True:
                if (len(final_string) + len(str_aux)) < len(text):
                    while True:
                        if str_aux[0] in (' ', ','):
                            str_aux = str_aux[1:]
                            qtd_char_rem += 1
                        break 

                    if str_aux[-1] in (' ', '.', ',', '!'):
                        final_string += str_aux[: len(str_aux)] + '\n'
                        break
                    else:
                        str_aux = str_aux[: len(str_aux) - 1]
                else:
                    if str_aux[0] == ' ':
                        str_aux = str_aux[1:]
                        qtd_char_rem += 1

                    final_string += str_aux
                    break
                
    return final_string
