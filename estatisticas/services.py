
from database.conector import conectar_banco
import time


def total():
    while True:

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select count(*) from alunos where ativo = 'True' ",
                )

                resultado = cursor.fetchone()

            print(f"""
========================================
       EDUCORE | TOTAL DE ALUNOS
========================================
 Total de alunos ativos: {resultado[0]}
========================================
""")

            time.sleep(2)

            print("""
----------------------------------------
          OPÇÕES DISPONÍVEIS
----------------------------------------
 [1] Consultar total de professores
 [2] Voltar ao menu principal
----------------------------------------
""")

            try:
                opcao = int(input(" > Escolha uma opção: "))
            except ValueError:
                print("[ERRO] Opção inválida!")
                continue

            if opcao == 1:
                total_prof()

            elif opcao == 2:
                print("[AVISO] Retornando ao menu principal...")
                return

            else:
                print("[ERRO] Opção inválida!")


def total_prof():

    while True:

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select count(*) from usuarios where situacao = 'True' ",
                )

                resultado = cursor.fetchone()

                print(f"""
========================================
     EDUCORE | TOTAL DE PROFESSORES
========================================
 Total de professores ativos: {resultado[0]}
========================================
""")

                time.sleep(2)

                print("""
----------------------------------------
          OPÇÕES DISPONÍVEIS
----------------------------------------
 [1] Consultar total de alunos
 [2] Voltar ao menu principal
----------------------------------------
""")

                try:
                    escolha = int(input(" > Escolha uma opção: "))
                except ValueError:
                    print("[ERRO] Opção inválida!")
                    continue

                if escolha == 1:
                    total()

                elif escolha == 2:
                    print("[AVISO] Retornando ao menu principal...")
                    return

                else:
                    print("[ERRO] Opção inválida!")
