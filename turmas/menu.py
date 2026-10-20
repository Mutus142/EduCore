

def turmas():

    while True:

        print("Menu do modulo de turmas!")

        print('''
        Escolha uma opção:
        1 - Adicionar Turma
        2 - Editar Turma
        3 - Remover Turma
        ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Invalido!")
            continue

        if escolha == 1:
            add_turma()

        elif escolha == 2:
            editar_turma()

        elif escolha == 3:
            remover_turma()

        elif escolha == 4:
            print("Voltando...")
            return

        else:
            print("Escolha invalida!")
            continue