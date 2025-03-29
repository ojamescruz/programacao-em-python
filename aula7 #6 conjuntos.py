# conjunto não repete dados
conjunto={1,2,3,4,5,6,7,7,7,8}
print(conjunto)



# dicionário

print('Método 1')

pessoa1 = {
    'nome': 'Carlos',
    'idade': 45,
    'endereço': 'Rua 45',
    'e-mail': 'carlos@gmail.com'

}

print(pessoa1['nome'])
print()



print('Método 2')

pessoa2 = {
    'nome': ['Carlos'],
    'idade': [45],
    'endereço': ['Rua 45'],
    'e-mail': ['carlos@gmail.com']

}

print(pessoa2)
print()


# Listando os valores do dicionário
print('Valores')
print(pessoa2.values)
print()

# Listando os rótulos do dicionário
print('Rótulos')
print(pessoa2.keys)
print()