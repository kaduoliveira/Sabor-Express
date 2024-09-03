'''
#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Insira um numero para determinar se par ou impar: ' ))

if numero % 2 == 0:
    print('Número PAR')
else:
    print('Número IMPAR')
'''
'''
#Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.

idade = int(input('Digite a sua idade para classificação: '))

if idade<=12:
    print("Criança")
elif 13<=idade<=18:
    print('Adolescente')
elif idade>18:
    print('Adulto')
else:
    print('Valor inválido')
'''
'''
#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome = str(input('Insira o seu nome: '))
senha = str(input('Digite a sua senha: '))

if nome == 'adm' and senha == '123':
    print('Acesso PERMITIDO')
else:
    print('Acesso NEGADO')
'''

#1 - Para criar um dicionário com informações de uma pessoa, você pode utilizar a seguinte solução:

pessoa = {'nome':'Laura', 'idade':9, 'Cidade':'Maceió'}

print(pessoa) #vai retornar todo o dicionario tal qual eu o defini
print(pessoa['Cidade']) #retorna apenas o atributo Cidade

#2 - Para fazer a atualização de um valor, adicionar um item e remover uma informação, você pode usar o seguinte raciocínio:

pessoa['idade'] = 12 #muda somente o atributo definido

pessoa['Pofissao'] = 'estudante' #adicção de mais um atributo
print(pessoa)
#{'nome': 'Laura', 'idade': 12, 'Cidade': 'Maceió', 'Pofissao': 'estudante'}
del pessoa['Cidade'] #removendo um atributo
print(pessoa)
#{'nome': 'Laura', 'idade': 12, 'Pofissao': 'estudante'}

#3 - Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:
import math
print()
for i in range(1, 6): #começa no espaço 1 e vai até o 6, faltou definir o passo
    i = i**2
    numeros_quadrados = {i}
    print(int(math.sqrt(i)), f'² = {i}')

#4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:
print()
if 'Cidade' in pessoa:
    print('Atributo encontrado')
else:
    print('atributo não encontrado')

#5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
print()
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
