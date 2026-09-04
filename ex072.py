
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {cont[numero]}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print('Programa finalizado!')
