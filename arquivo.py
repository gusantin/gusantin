#abrir um arquivo para escrita
with open('arquivo.txt', 'w') as file:
    file.write("Olá Mundo")

# abrir um arquivo para leitura e escrita
with open('arquivo.txt' , 'r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteúdo')
