lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}')
# tuplas são imutáveis
# for comida in lanche:
#     print(f'eu vou comer {comida}')
# print('Comi pra caramba')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
print(c.count(5))
print(c)
print(c.index(8)) # mostra em qual posição está

# pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa)
# print(pessoa)

tupla = (1, 2, 3, 4, 5)
print(tupla[0])

dir(tuple)

cliente = ('Natália', '000.000.000-00', '000.000.0')
clientes = []
clientes.append(cliente)
