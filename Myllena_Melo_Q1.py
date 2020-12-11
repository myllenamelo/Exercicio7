'''
Faça um programa que ajude um jogador da Mega Sena a criar palpites. O
programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1-60 para cada jogo, cadastrando tudo em uma lista composta.
Exemplo:
Quantos jogos você quer sortear? 2
Jogo 1: [4,8,10,20,26,38]
Jogo 2: [14, 20, 43, 35, 38,47]

Obs: o número não pode se repetir no mesmo jogo. Mas, não tem problema se
repetir em outro jogo.
Além de exibir na tela o resultado do palpite.
Você criar um arquivo com os mesmos resultados.
'''
import random
lista_Num = list()
lista_Num_Sorteados = list()
qnt_Jogos = 0
novalista=str

for l in range(0, 60):
    lista_Num.append(l+1)

qnt_Jogos = int(input('Quantos jogos você quer sortear?'))
for h in range(0, qnt_Jogos):
    lista_Num_Sorteados.append(random.sample(lista_Num, 6))
    print('Jogo ', h+1, ': ', sorted(lista_Num_Sorteados[h]))
    with open ('palpites.txt','w') as arquivo:
        for palpite in lista_Num_Sorteados:
            arquivo.write(str(palpite) + '\n')


    
