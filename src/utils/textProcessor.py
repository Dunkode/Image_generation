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
        separeted_texts = getTexBrokenInLines(text, max_char, qtd_cuts)#.split("\n")      
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
    forced_brokes = text.count('\n')
    return math.ceil((len(text)/max_char) + forced_brokes)
    

def getTexBrokenInLines(text, max_char, qtd_cuts):
    '''
    Essa função é o cérebro do programa.
    Aqui, recebemos o texto a ser cortado, a quantidade
    máxima de caracteres por linha e quantas linhas esse
    texto pode ser quebrado.
    '''

    '''
    final_string = ''
    qtd_char_rem = 0
    len_text_no_linebroke = len(text.strip('\n'))
    for i in range(0, (qtd_cuts + 1)):
        pos_no_linebroke = len(final_string.replace('\n', ''))

        str_aux = text[0 if len(final_string) == 0 
                        else pos_no_linebroke + qtd_char_rem: 
                        pos_no_linebroke + max_char
                        ]

        if str_aux != '':
            while True:
                if (pos_no_linebroke + len(str_aux.strip('\n'))) < len_text_no_linebroke:
                    if '\n' in str_aux:
                        cuted_string = str_aux.split('\n')
                        if len(cuted_string) > 1:
                            final_string += cuted_string[0] + '\n'
                            qtd_char_rem += 1
                            break
                    while True:
                        if str_aux[0] in (' ', ','):
                            str_aux = str_aux[1:]
                            qtd_char_rem += 1
                        break 

                    if str_aux[-1] in (' ', '.', ',', '!', '?'):
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
    '''
                
    finalStrings = list()

    qtdCharInseridos = 0
    qtdCharTotal = len(text.strip('\n'))

    for i in range(0, (qtd_cuts + 1)):
        if qtdCharInseridos < qtdCharTotal:
            txtAnalisado = text[qtdCharInseridos: qtdCharInseridos + max_char]

            if txtAnalisado != '':
                while True:
                    if '\n' in txtAnalisado:
                        txtCortado = txtAnalisado.split('\n')
                        qtdTxts = len(txtCortado)
                        
                        if qtdTxts > 2:
                            indUltimo = len(txtCortado)-1

                            for i in range(0, indUltimo):
                                finalStrings.append(txtCortado[i])
                                qtdCharInseridos += len(txtCortado[i])+1
                            
                            # txtAnalisado = txtCortado[indUltimo]
                            break
                        else:
                            qtdCharInseridos += len(txtCortado[0])+1
                            finalStrings.append(txtCortado[0])
                            # txtAnalisado = txtCortado[1]
                            break
                    else:
                        if txtAnalisado[0] == " ":
                            txtAnalisado = txtAnalisado[1:]
                            qtdCharInseridos += 1

                        if txtAnalisado[-1] in (' ', '.', ',', '!', '?', "\'", "\""):
                            qtdCharInseridos += len(txtAnalisado)
                            finalStrings.append(txtAnalisado)
                            break
                        else:
                            txtAnalisado = txtAnalisado[: len(txtAnalisado)-1]

    return finalStrings
