
from database.conector import conectar_banco
import time
from menu.menu import menu
    
while True:
    def cad_user():
        print("""
========================================
          EDUCORE | CADASTRO
========================================
""")

        try:
            nome_user = str(input("Nome completo: "))
        except ValueError:
            print("[ERRO] Nome inválido!")
            continue

        try:
            user = str(input("Usuário: "))
        except ValueError:
            print("[ERRO] Usuário inválido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select usuario from usuarios where usuario = %s", (user,)
                )

                resultado = cursor.fetchone()

                if resultado is not None:
                    print(f"\n[ERRO] O usuário '{user}' já está cadastrado!")
                    print("[AVISO] Escolha outro nome de usuário.")
                    time.sleep(2)
                    continue

                else:
                    try:
                        senha = input("Digite sua senha: ")
                    except ValueError:
                        print("[ERRO] Senha inválida!")

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "insert into usuarios (nome, usuario, senha) values(%s, %s, %s)", (nome_user, user, senha)
                )

                print("""
----------------------------------------
     USUÁRIO CADASTRADO COM SUCESSO!
----------------------------------------
""")
                time.sleep(2)

                print(f"[OK] Seja bem-vindo ao EduCore, {user}!")

                menu()
