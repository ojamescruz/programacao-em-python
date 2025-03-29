lista = [1,2,3,6,5,5,6]

# Adicionar

# Append: adiciona 1 dado no final da lista
print('Método 1')
lista.append(50)
print(lista)
print()

# Insert: é necessário informar dois argumentos: a posição onde o valor será inserido e o valor a ser inserido
print('Método 2')
lista.insert(0,200)
print(lista)
print()

# += : adiciona uma lista de valores ao final de uma lista já existente
print('Método 3')
lista += (10,2,5,6,6,4,5,5,5)
print(lista)
print()

# extend: adiciona uma lista ou tupla de valores ao final de uma lista já existente
print('Método 4')
lista.extend([10,2,5,6,6,4,5,5,5])
print(lista)
print()


# pop: deletar um valor de uma lista (o último ou aquela posição que desejar)
print('Método 1')
lista.pop()
print(lista)
print()

print('Método 2')
lista.pop(0)
print(lista)
print()


# remove: deleta o valor que eu escolher
print('Método 3')
lista.remove(3)
print(lista)
print()


# del: remove
print('Método 4')
del lista[2]
print(lista)
print()

# verificar a lista
print('Verificações dos dados da lista')
print()

lista = [1,2,3,6,5,5,6]
soma=sum(lista)
print('A somatória dos dados da lista é igual a: ',soma)
print()

tamanho=len(lista)
print('A lista possui este tamanho: ',tamanho)
print()

menor=min(lista)
maior=max(lista)
print('O maior valor da lista é:', maior)
print('O menor valor da lista é:', menor)
print()


# limpar a lista
lista.clear()
print('A lista atualizada é: ', lista)
print()

# organizar a lista

print('Organiza em ordem crescente:')
lista = [10,2,33,65,5,51,6]
lista.sort()
print(lista)

print('Inverte a ordem contida anteriormente:')
lista = [10,2,33,65,5,51,6]
lista.reverse()
print(lista)

print('Organiza em ordem decrescente:')
lista = [10,2,33,65,5,51,6]
lista.sort(reverse=True)
print(lista)


# adicionar caracteres entre valores
print('Incluir caracteres entre valores')
lista1 = ['10','2','33','65','5','51','6']
d=', '
x=d.join(lista1)
print(x)
print()