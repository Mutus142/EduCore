import time    
from alunos.menu import alunos

while True:

    def menu():
        print("Bem vindo ao menu!")

        print('''
        1 - Gerenciamento de Alunos
        2 - Gerenciamento de Notas
        3 - Gerenciamento de Turmas
        4 - Estatisticas Gerais
        5 - Sair
         ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("invalido!")
            continue

        if escolha == 1:
            alunos()

        elif escolha == 2:
            notas()

        elif escolha == 3:
            turmas()

        elif escolha == 4:
            estatisticas()

        elif escolha == 5:
            print("Saindo...")
            break

        else:
            print("Opção invalida!")
            continue
        