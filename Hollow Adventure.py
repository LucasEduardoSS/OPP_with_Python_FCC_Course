from random import randint, choice
from time import sleep


def ataque_inimigo():
    danos = 0
    # Definem os valores de dano dos ataques do inimigo em questão
    if inimigo['Nome'] == 'Semi Hollow':
        danos = [randint(10, 15), randint(20, 30)]

    elif inimigo['Nome'] == 'Hollow':
        danos = [randint(15, 25), randint(25, 40), randint(55, 70)]

    # Calcula e atribui o valor de dano ao ataque do inimigp
    damage_ini = {'Ataque': choice(inimigo['Ataques']).copy()}
    damage_ini['Dano'] = danos[damage_ini['Ataque']['cod']]
    damage_ini['Dano'] -= (damage_ini['Dano'] * (jogador['Defesa']/100))

    # Impede que ataque cure o jogador
    if damage_ini['Dano'] < 0:
        damage_ini['Dano'] = 0

    # Imprime os dados do ataque inimigo
    jogador['Vida'] -= damage_ini['Dano']
    print(f'O inimigo usou {damage_ini["Ataque"]["Nome"]}...'), sleep(1)
    print(f'Você recebeu {damage_ini["Dano"]:.2f} pontos de dano do inimigo!'), sleep(1)


# Função de Defesa
def defesa(x):
    if x == 0:
        return 0
    defence = jogador['Defesas'][x - 1]['Valor']
    jogador['Defesa'] += defence
    print(f'\nVocê aumentou sua defesa em {defence} pontos.'), sleep(1)
    if x == 3:
        ataque(1)
    jogador['Defesa'] = 15


# Função de Ataque
def ataque(x):
    danos = [randint(20, 25), randint(25, 45), randint(65, 90)]
    if x == 0:
        return 0
    damage = danos[x - 1]
    damage -= (damage * (inimigo['Defesa']/100))
    inimigo['Vida'] -= damage
    print(f'\nVocê deu {damage:.2f} pontos de dano no inimigo!'), sleep(1)


# Função que imprime um título
def titulo(text):
    print('-' * 50, f'\n{text:^50}'), print('-' * 50)


# Aumenta o valor da defesa do inimigo
def endurecer_casca(x):
    inimigos[x]["Defesa"] += 10


count = inimigo = o1 = count1 = 0

jogador = {
    'Nome': 'Tiburcio',
    'Vida': 100,
    'Ataques': [
        {'Nome': 'Ataque Fraco', 'Dano': 0},
        {'Nome': 'Ataque Forte', 'Dano': 0},
        {'Nome': 'Ataque Especial', 'Dano': 0}
    ],
    'Defesas': [
        {'Nome': 'Escudo', 'Valor': 20},
        {'Nome': 'Esquivar', 'Valor': 100},
        {'Nome': 'Refletir', 'Valor': 100}
    ],
    'Defesa': 15
}

inimigos = [
    # Semi Hollow
    {
        'Nome': 'Semi Hollow',
        'Vida': 100,
        'Ataques': [
            {'Nome': 'Ataque Fraco', 'cod': 0},
            {'Nome': 'Ataque Forte', 'cod': 1}
        ],
        'Defesa': 10,
        'Peso': 2
    },

    # Hollow
    {
        'Nome': 'Hollow',
        'Vida': 120,
        'Ataques': [
            {'Nome': 'Ataque Fraco', 'cod': 0},
            {'Nome': 'Ataque Forte', 'cod': 1},
            {'Nome': 'Ataque Especial', 'cod': 2}
        ],
        'Habilidade Especial': {'Nome': 'Endurecer Casca'},
        'Defesa': 20,
        'Peso': 3
    }
]

# Código Principal
titulo("Hollow Knight")

# jogador['Nome'] = str(input('Digite o nome do seu personagem: '))
while jogador['Vida'] > 0:
    # Escolhe o primeiro inimigo
    if count == 0:
        inimigo = inimigos[0].copy()

    # Escolhe um inimigo aleatorio
    elif count > 0:
        inimigo = choice(inimigos).copy()
        while inimigo['Peso'] > count:
            inimigo = choice(inimigos).copy()

    # Mostra qual inimigo apareceu
    print(f'Um {inimigo["Nome"]} apareceu!')

    # Inicia o combate
    while inimigo['Vida'] > 0:
        # Mostra a vida do inimigo
        print(f'\nVida do inimigo: {inimigo["Vida"]:.2f}')
        print(f'Vida do Jogador: {jogador["Vida"]:.2f}')
        sleep(1)

        # Mostra o menu de ações do jogador
        while True:
            # Mostra as opções de combate
            print('''
O que irá fazer? 
1 - Atacar...
2 - Defender...
3 - Fugir
4 - Suicidar-se
            ''')

            o1 = int(input('> '))

            #  * ATAQUES * Mostra o menu de ataques do jogador
            if o1 == 1:
                # Mostra as opções de ataque
                print('''
Que ataque irá usar?
1 - Ataque Fraco
2 - Ataque Forte
3 - Ataque Especial
0 - Cancelar Ataque
            ''')

                o1_1 = int(input('> '))

                # Executa o ataque do jogador
                ataque(o1_1)

                if o1_1 != 0:
                    break

            # * DEFESAS * Mostra as opções de defesa
            elif o1 == 2:
                # Mostra as opções de defesa
                print('''
Que defesa irá usar?
1 - Escudo
2 - Desviar
3 - Refletir
0 - Calcelar Defesa
''')

                o1_1 = int(input('> '))

                # Executa a defesa do jogador
                defesa(o1_1)

                if o1_1 != 0:
                    break

            # Encerra o combate
            elif o1 == 3 or o1 == 4:
                break

        # Encerra o combate
        if o1 == 3 or o1 == 4:
            print()
            break

        # Mostra ao jogador que ele matou o inimigo e a EXP ganha
        if inimigo['Vida'] <= 0:
            print(f'Você matou o {inimigo["Nome"]}!'), sleep(1)
            print(f'Você recebeu {randint(0, 100)} pontos de EXP!'), sleep(1), print()
            count1 += 1
            break

        # Excuta o ataque do inimigo
        ataque_inimigo()

        if jogador['Vida'] <= 0:
            print('\nVocê morreu!', '\nGame Over'), sleep(1)
            break

    # Soma ao contador o peso do inimigo enfrentado
    count += inimigo['Peso']

    inimigo.clear()

    if o1 == 4:
        print('Você escolheu a saída mais fácil.')
        break

print(f'Você matou {count1} inimigo(s).')
