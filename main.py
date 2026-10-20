
from login.user import login_user
from login.cadastro import cad_user


def main():

    while True:

        print("""
========================================
           EDUCORE | INÍCIO
========================================
 [1] Fazer login
 [2] Cadastrar-se
========================================
""")

        try:
            escolha = int(input(" > Escolha uma opção: "))
        except ValueError:
            print("[ERRO] Opção inválida!")
            return

        if escolha == 1:
            login_user()

        elif escolha == 2:
            cad_user()

        else:
            print("[ERRO] Opção inválida!")


if __name__ == "__main__":
    main()
