from database.conector import conectar_banco
import time
from menu.menu import menu
    
while True:
    def cad_user():
        print("Bem vindo ao cadastro de usuario do EduCore!")

        try:
            nome_user = str(input("Nome completo: "))
        except ValueError:
            print("Invalido!")
            continue

        try:
            user = str(input("Usuário: "))
        except ValueError:
            print("Invalido!")
            continue

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "select usuario from usuarios where usuario = %s", (user,)
                )

                resultado = cursor.fetchone()

                if resultado is not None:
                    print(f"Já existe um {user} cadastrado!")
                    print("Escolha outro usuário!")
                    time.sleep(2)
                    continue

                else:
                    try:
                        senha = input("Digite sua senha: ")
                    except ValueError:
                        print("Invalido!")

        with conectar_banco() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "insert into usuarios (nome, usuario, senha) values(%s, %s, %s)", (nome_user, user, senha)
                )

                print("Usuário cadastrado!")
                time.sleep(2)

                print(f"Seja bem vindo {user}!")

                menu()