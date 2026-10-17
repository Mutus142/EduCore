
from database.conector import conectar_banco
import psycopg
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

        try:
            user = str(input(" > Usuário: "))
        except ValueError:
            print("[ERRO] Usuário inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT usuario FROM usuarios WHERE usuario = %s AND situacao = TRUE",
                    (user,)
                )

                resultado = cursor.fetchone()

                if resultado is None:
                    print("\n[ERRO] Usuário não encontrado!")
                    time.sleep(2)

                    print("""
----------------------------------------
          OPÇÕES DISPONÍVEIS
----------------------------------------
 [1] Tentar novamente
 [2] Cadastrar-se
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

                    else:
                        print("[ERRO] Opção inválida!")
                        continue

                else:
                    print("\n[OK] Usuário encontrado!")
                    time.sleep(2)

                    try:
                        senha = str(input(" > Senha: "))
                    except ValueError:
                        print("[ERRO] Senha inválida!")
                        continue

                    with conectar_banco() as conexao:
                        with conexao.cursor() as cursor:
                            cursor.execute(
                                "SELECT senha FROM usuarios WHERE usuario = %s AND senha = %s",
                                (user, senha)
                            )

                            resultado2 = cursor.fetchone()

                            if resultado2 is None:
                                print("\n[ERRO] Senha incorreta!")
                                continue

                            else:
                                print("""
----------------------------------------
       LOGIN REALIZADO COM SUCESSO!
----------------------------------------
""")
                                time.sleep(2)

                                menu()
                                return
