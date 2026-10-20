
from database.conector import conectar_banco
import time
from menu.menu import menu


def cad_user():

    while True:

        print("""
========================================
          EDUCORE | CADASTRO
========================================
""")

        nome_user = input(" > Nome completo: ").strip()

        if not nome_user:
            print("[ERRO] Nome inválido!")
            continue

        user = input(" > Usuário: ").strip()

        if not user:
            print("[ERRO] Usuário inválido!")
            continue

        senha = input(" > Digite sua senha: ")

        if not senha.strip():
            print("[ERRO] Senha inválida!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:

                cursor.execute(
                    "SELECT usuario FROM usuarios WHERE usuario = %s",
                    (user,)
                )

                resultado = cursor.fetchone()

                if resultado is not None:
                    print(f"\n[ERRO] O usuário '{user}' já está cadastrado!")
                    print("[AVISO] Escolha outro nome de usuário.")
                    time.sleep(2)
                    continue

                cursor.execute(
                    """
                    INSERT INTO usuarios (nome, usuario, senha)
                    VALUES (%s, %s, %s)
                    """,
                    (nome_user, user, senha)
                )
                
        print("""
----------------------------------------
     USUÁRIO CADASTRADO COM SUCESSO!
----------------------------------------
""")

        time.sleep(2)

        print(f"[OK] Seja bem-vindo ao EduCore, {user}!")

        menu()
        return
