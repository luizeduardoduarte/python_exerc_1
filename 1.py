'''
Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo
com o valor digitado destancando utilizando outra cor de fonte.
'''

nome = input('Qual eh seu nome?\n')
cor = {'limpa':'\033[m', 'azul':'\033[1;36m'}
print('Ola {}{}{}! Prazer em te conhecer!' .format(cor['azul'], nome , cor['limpa']))