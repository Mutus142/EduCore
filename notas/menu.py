
from notas.services import add_nota
from notas.services import editar_nota
from notas.services import ver_notas


def notas():

    while True:

        print("""
========================================
           EDUCORE | NOTAS
========================================
 [1] Adicionar nota
 [2] Editar nota
 [3] Visualizar notas de um aluno
 [4] Voltar ao menu principal
========================================
""")

        try:
            escolha = int(input(" > Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
            continue

        if escolha == 1:
            add_nota()

        elif escolha == 2:
            editar_nota()

        elif escolha == 3:
            ver_notas()
            print("[AVISO] Visualização de notas em desenvolvimento!")

        elif escolha == 4:
            print("[AVISO] Retornando ao menu principal...")
            return

        else:
            print("[ERRO] Opção inválida!")
            continue
