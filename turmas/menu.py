
from turmas.service import add_turma
from turmas.service import editar_turma
from turmas.service import remover_turma


def turmas():

    while True:

        print("""
========================================
           EDUCORE | TURMAS
========================================
 [1] Adicionar turma
 [2] Editar turma
 [3] Remover turma
 [4] Voltar ao menu principal
========================================
""")

        try:
            escolha = int(input(" > Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
            continue

        if escolha == 1:
            add_turma()

        elif escolha == 2:
            editar_turma()

        elif escolha == 3:
            remover_turma()

        elif escolha == 4:
            print("[AVISO] Retornando ao menu principal...")
            return

        else:
            print("[ERRO] Opção inválida!")
            continue
