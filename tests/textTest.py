strn = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
qtd_cuts = 19
max_char = 41

finalStrings = list()

qtdCharInseridos = 0
qtdCharTotal = len(strn.strip('\n'))

for i in range(0, (qtd_cuts + 1)):
    txtAnalisado = strn[qtdCharInseridos: qtdCharInseridos + max_char]

    if txtAnalisado != '':
        while True:
            if '\n' in txtAnalisado:
                txtCortado = txtAnalisado.split('\n')
                qtdTxts = len(txtCortado)
                
                if qtdTxts > 2:
                    indUltimo = len(txtCortado)-1

                    for i in range(0, indUltimo):
                        finalStrings.append(txtCortado[i])
                        qtdCharInseridos += len(txtCortado[i])
                    
                    txtAnalisado = txtCortado[indUltimo]
                else:
                    qtdCharInseridos += len(txtCortado[0])
                    finalStrings.append(txtCortado[0])
                    txtAnalisado = txtCortado[1]
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
