# Criando listas e carregando dados de listas


# Tipo inteiro

lista = [10,2,3030,2,2,3] 
v=lista[-6]
print(v)


lista = [10,2,3030,2,2,3] 
v=lista[4]
print(v)

# Tipo texto

nomes=[]

nome1 = input  ('Digite seu nome: ')
nome2 = input  ('Digite seu nome: ')
nome3 = input  ('Digite seu nome: ')


nomes = [nome1, nome2, nome3]
print('3º Nome: ', nomes[2])
print('1º Nome: ', nomes[0])
print('2º Nome: ', nomes[1])
print()

# Substituir dados dentro dos índices


print('Números originais')
lista_numeros=[1,2,6,9,1,3]
print(lista_numeros)
print()


print('Números alterados')
lista_numeros[0]=200
lista_numeros[3]=500
lista_numeros[5]=400
print(lista_numeros)
print()

# Operações matemáticas com listas

print('1ª Opção:')
lista=[10,20,30,40]
n1=lista[0]
n2=lista[1]
n3=lista[2]

soma = n1+n2+n3
print(soma)
print()


print('2ª Opção:')
lista=[10,20,30,40]
print(lista[0:3])
print(sum(lista[0:3]))

