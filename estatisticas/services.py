from database.conector import conectar_banco
import time

def alunos_est():
    while True

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                "select count(*) from alunos where ativo = 'True' ", 
            )

            resultado = cursor.fetchall()

            print(f"Total de Alunos: {resultado}")

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

