
from alunos.services import cad_aluno
from alunos.services import ver_aluno
from alunos.services import editar_aluno
from alunos.services import remover_aluno


def alunos():

    while True:

        print("""
========================================
           EDUCORE | ALUNOS
========================================
 [1] Cadastrar aluno
 [2] Visualizar alunos
 [3] Editar aluno
 [4] Remover aluno
 [5] Voltar ao menu principal
========================================
""")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
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
            print("[AVISO] Retornando ao menu principal...")
            return

        else:
            print("[ERRO] Opção inválida!")
            continue
