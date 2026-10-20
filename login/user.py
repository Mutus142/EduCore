
from database.conector import conectar_banco
from getpass import getpass
import time
from menu.menu import menu
from login.cadastro import cad_user


def login_user():

    while True:

        print("""
========================================
            EDUCORE | LOGIN
========================================
""")

        user = input(" > Usuário: ").strip()

        if not user:
            print("[ERRO] Usuário inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT senha
                    FROM usuarios
                    WHERE usuario = %s AND situacao = TRUE
                    """,
                    (user,)
                )

                resultado = cursor.fetchone()

        # Conexão encerrada antes da navegação.

        if resultado is None:

            print("\n[ERRO] Usuário não encontrado!")
            time.sleep(2)

            print("""
----------------------------------------
          OPÇÕES DISPONÍVEIS
----------------------------------------
 [1] Tentar novamente
 [2] Cadastrar-se
 [0] Voltar
----------------------------------------
""")

            try:
                escolha = int(input(" > Escolha uma opção: "))
            except ValueError:
                print("[ERRO] Opção inválida!")
                continue

            if escolha == 1:
                continue

            elif escolha == 2:
                cad_user()
                return

            elif escolha == 0:
                return

            else:
                print("[ERRO] Opção inválida!")
                continue

        senha = getpass(" > Senha: ")

        if senha != resultado[0]:
            print("\n[ERRO] Senha incorreta!")
            continue

        print("""
----------------------------------------
       LOGIN REALIZADO COM SUCESSO!
----------------------------------------
""")

        time.sleep(2)

        menu()
        return
