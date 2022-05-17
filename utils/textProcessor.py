import math

MAX_LINES_FOR_IMAGE = 11

def brokeText(text, max_char):
    if len(text) > max_char:
        qtd_cuts = calculeLineBrokes(text, max_char)        
        separeted_texts = getTexBrokenInLines(text, max_char, qtd_cuts).split("\n")      
        return separeted_texts

    else:
        return separeted_texts.append(text)

def calculeLineBrokes(text, max_char):
    return math.ceil(len(text)/max_char)
    

def getTexBrokenInLines(text, max_char, qtd_cuts):
    final_string = ''
    qtd_char_rem = 0
    for i in range(0, qtd_cuts + 1):
        pos_no_linebroke = len(final_string.replace('\n', ''))

        str_aux = text[0 if len(final_string) == 0 
                        else pos_no_linebroke + qtd_char_rem: 
                        pos_no_linebroke + max_char
                        ]

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
                final_string += str_aux
                break
    return final_string
