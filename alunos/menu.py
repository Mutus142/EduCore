

while True:

    def alunos():
        print("bem vindo ao serviço de alunos!")

        print('''
        1 - Cadastro de Aluno
        2 - Visualizar Aluno
        3 - Editar Aluno
        4 - Remover Aluno
        5 - Voltar ao menu principal
        ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Invalido!")
            continue

        if escolha == 1:
            cad_aluno()

        elif escolha == 2:
            ver_aluno()

        elif escolha == 3:
            editar_aluno()

        elif escolha == 4:
            remover_aluno()

        elif escolha == 5:
            print("Voltando ao menu...")
            return

        else:
            print("Opção invalida!")
            continue