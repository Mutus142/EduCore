from login.user import login_user
from login.cadastro import cad_user

def main():

    while True:

        print("Bem vindo ao EduCore!")

        print('''
1 - Fazer Login
2 - Cadastrar - se
        ''')

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Valor invalido!")
            return

        if escolha == 1:
            login_user()

        elif escolha == 2:
            cad_user()

        else:
            print("Escolha invalida!")


if __name__ == "__main__":
    main()