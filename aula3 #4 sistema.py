#EXEMPLO - PROFESSORA:

# input() print() variáveis  + - * / | > < >= <= !=

# sistema de notas de escola / média 

print('Sistema de notas de escola')
print()
nome1 = input('Digite o nome do aluno 1: ')
print()
nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))
nota4 = float(input('Informe a 4ª nota: '))
nota5 = float(input('Informe a 5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

aprovado = media >= 7
reprovado = media < 5
recuperacao = media >= 5 and media <7

# concatenar - juntar 

print()
print('Aluno: ', nome1)
print()
print('A média final é:', media)
print()

print('O resultado deste aluno é: ')

print('Aprovado - ', aprovado)
print('Recuperação  - ', recuperacao)
print('Reprovado - ', reprovado)
