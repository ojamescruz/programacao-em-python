# entrada - processamento - saída
#TIPO DE DADOS PRIMITIVOS

#print() - imprimir algo no ambiente de teste (mostrar)
print('Olá mundo!')

#type

#dado do tipo inteiro
print(type(20))

#dado do tipo float
print(type(2.5))

#dado do tipo texto
print(type('Texto'))

#dado do tipo booleano
print(type(True))

#sinais aritméticos - (+ soma, - subtração, * multiplicação, / divisão)

#teste 1 (operações básicas com sinais aritméticos)
print (10+2)
print (10-2)
print (10*2)
print (10/2)

#teste 2 (combinação de 3 tipos de dados (texto, inteiro e float) e operação básica com sinais aritméticos)
print ('O resultado da equação 10+2 é:', 10+2)
print ('O resultado da equação 10-2 é:', 10-2)
print ('O resultado da equação 10*2 é:', 10*2)
print ('O resultado da equação 10/2 é:', 10/2)

#input - gerar uma entrada do usuário

#teste 3 (uso da função "input")
print(input('Digite um valor:'))

#teste 4 (uso da funçao "input" para operação básica aritmética)
print(int(input('Digite um número: ')) + int(input('Digite outro número: ')))



# Criação de variáveis
# nome do espaço é número
# = (atribuição)
# 10 é o valor que está guardado lá dentro
# não pode: caracteres especiais, conter números no início ou meio
# a linguagem diferencia letras maiúsculas e minúsculas
# elas são únicas

numero = 10



#Calcular a soma de dois números (num1 e num2)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
soma = num1 + num2

print (soma)
