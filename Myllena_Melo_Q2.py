'''
Faça um programa que permite cadastrar pessoas com os seguintes
dados: nome e idade. Grave esses dados em um arquivo de txt.
O sistema ainda terá opção de cadastrar um nova pessoa e de listar as
pessoas que estão gravadas no arquivo.
Ao cadastrar uma nova pessoa, não deve apagar os registros
anteriores.
'''

cadastrados=list()
escolha=str

cadastrados.append(str(input('Insira o nome: ')))
cadastrados.append(int(input('Insira a idade: ')))
with open ('cadastro.txt','w') as arquivo:
    for cadastro in cadastrados:
        arquivo.write(str(cadastro) + '\n')
escolha = str(input('''Deseja: 
    1-cadastrar nova pessoa
    2-listar pessoas cadastradas
     Digite sua escolha: '''))
while True:
    if (escolha == '1'):
        cadastrados.append(str(input('Insira o nome: ')))
        cadastrados.append(int(input('Insira a idade: ')))   
        with open ('cadastro.txt','a') as arquivo:
            for cadastro in cadastrados:
                arquivo.write(str(cadastro) + '\n')
        escolha = str(input('''Deseja: 
        1-cadastrar nova pessoa
        2-listar pessoas cadastradas
        Digite sua escolha: '''))
        if (escolha == '2'):
            print ('Cadastrados:')
            for cadastro in cadastrados:
                print(cadastro, end=",")
        if (escolha != '1') and (escolha != '3'):
            break
