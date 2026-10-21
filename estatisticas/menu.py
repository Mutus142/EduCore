
from estatisticas.services import total
from estatisticas.services import total_prof


def estatisticas():

    while True:

        print("""
========================================
         EDUCORE | ESTATÍSTICAS
========================================
 [1] Total de alunos
 [2] Total de professores
 [3] Voltar ao menu principal
========================================
""")

        try:
            escolha = int(input(" > Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
            continue

        if escolha == 1:
            total()

        elif escolha == 2:
            total_prof()

        elif escolha == 3:
            print("[AVISO] Retornando ao menu principal...")
            return
