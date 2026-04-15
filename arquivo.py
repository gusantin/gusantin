#abrir um arquivo para escrita
with open('arquivo.txt', 'w', encoding ="UTF-8") as file:
    file.write("Olá Mundo")

# abrir um arquivo para leitura e escrita
with open('arquivo.txt' , 'r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteúdo')

#abrir um arquivo para anexo
with open('arquivo.txt', 'a') as file:
    file.write('\nMais uma linha no final do arquivo')


#abre o arquivo no modo de escrita ('w')
with open('arquivo.txt', 'w') as file:
    #escreve no arquivo
    file.write('linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

#abre o arquivo no modo de leitura ('r')
with open('arquivo.txt', 'r') as file:
    #lê a primeira linha do arquivo
    linha1 = file.readline()
    #lê a segunda linha do arquivo
    linha2 = file.readline()
    #le a terceira linha do arquivo
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)



    