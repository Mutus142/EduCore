
import time
from alunos.menu import alunos
from notas.menu import notas


def menu():

    while True:

        print("""
========================================
          EDUCORE | MENU PRINCIPAL
========================================
 [1] Gerenciamento de Alunos
 [2] Gerenciamento de Notas
 [3] Gerenciamento de Turmas
 [4] Estatísticas Gerais
 [5] Sair
========================================
""")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
            continue

        if escolha == 1:
            alunos()

        elif escolha == 2:
            notas()

        elif escolha == 3:
            #turmas()
            print('tetse')

        elif escolha == 4:
            #estatisticas()
            print("teste")

        elif escolha == 5:
            print("[AVISO] Encerrando o menu do EduCore...")
            break

        else:
            print("[ERRO] Opção inválida!")
            continue
