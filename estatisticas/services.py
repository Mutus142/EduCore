from database.conector import conectar_banco
import time

def total():
    while True

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                "select count(*) from alunos where ativo = 'True' ", 
            )

            resultado = cursor.fetchall()

            print(f"Total de Alunos: {resultado[0]}")

            time.sleep(2)

            print('''
            O que voce quer fazer agora:
            1 - Total de Professor
            2 - Voltar ao menu principal
            ''')

            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("invalido!")
                continue

            if opcao == 1:
                total_prof()

            elif opcao == 2:
                print("Voltando...")
                return

            else:
                print("Invalido!")


def total_prof():

    while True:

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select count(*) from usuarios where situacao = 'True' ",
                )

                resultado = cursor.fetchall()

                print(f"Total de Professores: {resultado[0]}")

                time.sleep(2)

                print('''
                O que voce quer fazer agora?
                1 - Total de Alunos
                2 - Voltar ao menu principal
                ''')

                try:
                    escolha = int(input("Escolha uma opção: "))
                except ValueError:
                    print("Invalido!")
                    continue

                if escolha == 1:
                    total()

                elif escolha == 2:
                    print("Voltando...")
                    return

                else:
                    print("Invalido!")
