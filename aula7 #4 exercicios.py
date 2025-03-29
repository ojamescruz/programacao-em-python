print('**Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.')
print()
lista1=list(range (2,21,2))
print(lista1)
print()

print('**Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.')
print()
numeros=list(range(1,11))
print(numeros)
print()

print('**Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`')
print()
num3=numeros[2]
print('O terceiro elemento da lista é: ',num3)
print()

print('**Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.')
print()
numeros.append(9)
print('A lista atualiazada é: ',numeros)
print()

print('**Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.')
print()
numeros.remove(5)
print('A lista atualiazada é: ',numeros)
print()

print('**Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.')
print()

# Método 1
print('Método 1:')
carros = ['Vectra', 'Astra','Golf']
concatena = carros + numeros
print(concatena)
print()

# Método 2
print('Método 2:')


print()