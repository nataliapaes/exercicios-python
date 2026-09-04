brasileirao = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense',
               'Bahia', 'Cruzeiro', 'Coritiba', 'Atlético-MG', 'Bragantino', 'Corinthians', 'São Paulo', 'Botafogo', 'Vitória', 'Santos', 'Grêmio', 'Mirassol', 'Vasco', 'Internacional', 'Remo', 'Chapecoense')
print('-='*15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*15)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-='*15)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*15)
print(f'O chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição')
while True:
    time = str(input('Você deseja ver a posição de qual time? ')).strip().title()
    if time in brasileirao:
        posicao = brasileirao.index(time) + 1
        print(f'O {time} está na {posicao}ª posição.')
    else:
        print('O time informado não está na tabela ou foi digitado incorretamente')
    continuar = str(input('Deseja buscar outro time? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
    print('-='*15)


