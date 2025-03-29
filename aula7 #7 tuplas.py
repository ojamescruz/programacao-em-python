# vazia

tupla=()

# exemplo de uma tupla

tupla=(1,2,3,6,9,45,1,14,4)


# incluindo dados numa tupla

print('incluindo dados numa tupla')       
x=tuple(range(1,51))
print(x)

cpfs=(12656565,6565989592,165994946,1656595959)
cpfs = cpfs + tupla
print(cpfs)
print()

# transformando tupla em lista

print('transformando tupla em lista')
tupla=(1,2,3,69,705,9)
l=list(tupla)
print(l)
print()

# transformando lista em tupla

print('transformando lista em tupla')
t=tuple(l)
print(t)
print()


# # min max len sum 