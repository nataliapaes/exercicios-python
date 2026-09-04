from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
ordem = sorted(numeros)
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor é {ordem[4]}')
print(f'O menor valor é {ordem[0]}')
# print(max(numeros))
# print(min(numeros))
