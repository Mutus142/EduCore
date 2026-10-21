from estatisticas.services import total
from estatisticas.services import total_prof
def estatisticas():


    while True:

        print('''
        Bem vindo ao modulo de estatisticas!
        1 - Total de Alunos
        2 - Total de Professores
        3 - Voltar ao menu principal
        ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Invalido!")
            continue

        if escolha == 1:
            total()

        elif escolha == 2:            
            total_prof()

        elif escolha == 3:
            print("Voltando...")
            return