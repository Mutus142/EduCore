

def estatisticas():


    while True:

        print('''
        Bem vindo ao modulo de estatisticas!
        1 - Alunos aprovados e reprovados
        2 - Total de Alunos
        3 - Total de Professores
        4 - Voltar ao menu principal
        ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Invalido!")
            continue

        if escolha == 1:
            alunos_est()

        elif escolha == 2:
            total()

        elif escolha == 3:
            total_prof()

        elif escolha == 4:
            print("Voltando...")
            return